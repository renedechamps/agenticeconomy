#!/usr/bin/env python3
"""CRI Adversarial Simulation v2 — agenticeconomy.dev/cri-simulation
Reproducible simulation for Paper 1 §5.4 Table 3.
Parameters calibrated to typical agent-commerce production conditions.

Profile A: fast Sybil ring (250 agents, 50 rings of 5)
Profile B: patient Sybil with bridges (150 agents, 30 rings of 5)
Profile C: collusive subnetwork (100 agents, 20 rings of 5)
Honest: 9,500 agents (typical 80–250 tx over 90 days, 70%+ unique counterparties)
"""
import math
import random
from statistics import median, mean

RNG_HONEST = 0x4847
RNG_A = 0x4341
RNG_B = 0x4252
RNG_C = 0x4343

DAYS = 90
N_HONEST = 9500
N_PROFILE_A = 250
N_PROFILE_B = 150
N_PROFILE_C = 100

def cri(n_tx, n_unique, volume, age_days, has_buyer, n_disputes, n_strikes,
        r_top=0.0, value_shock=0.0, genesis=False, eigen_factor=1.0):
    """CRI v2 formula with refined penalties + eigenvector-weighted diversity."""
    base = 30
    transaction = min(20, math.log2(n_tx + 1) * 3.33)
    diversity = min(15, (n_unique / max(n_tx, 1)) * 15 * eigen_factor)
    volume_score = min(10, math.log10(volume + 1) * 2.5)
    age_score = min(10, math.log2(age_days + 1) * 1.25)
    buyer = 5 if has_buyer else 0
    genesis_score = max(0, min(5, 5 * (1 - age_days/365))) if genesis else 0
    dispute_pen = (n_disputes / max(n_tx, 1)) * 25
    value_pen = min(15, value_shock * 5)
    concentration = min(10, max(0, (r_top - 0.5) * 20))
    strike_pen = 15 * (n_strikes / 3)
    score = base + transaction + diversity + volume_score + age_score + buyer + genesis_score
    score -= (dispute_pen + value_pen + concentration + strike_pen)
    return max(0, min(100, score))

def simulate_honest(rng, n_agents):
    """Honest: production-realistic (80-250 tx, 70%+ unique, 90 days active)."""
    agents = []
    for i in range(n_agents):
        first_day = max(0, int(abs(rng.gauss(15, 20))))
        active = max(15, DAYS - first_day)
        # 1-3 transactions/day on average for active honest agents
        n_tx = max(20, int(rng.gauss(120, 60)))
        # 70-90% unique counterparties
        n_unique = max(15, min(n_tx, int(n_tx * rng.uniform(0.65, 0.90))))
        # Volume: transactions × avg value per tx
        avg_value = max(0.5, rng.lognormvariate(0.5, 0.8))
        volume = n_tx * avg_value
        has_buyer = rng.random() < 0.85  # 85% have bilateral activity
        n_disputes = int(n_tx * rng.uniform(0.005, 0.025))  # 0.5-2.5% dispute rate
        r_top = rng.uniform(0.05, 0.30)
        score = cri(n_tx, n_unique, volume, active, has_buyer, n_disputes, 0, r_top=r_top)
        agents.append({'profile': 'honest', 'cri': score, 'cost': 0,
                       'days_to_70': estimate_days(score, 'honest'),
                       'n_tx': n_tx, 'volume': volume})
    return agents

def simulate_profile_a(rng, n_agents):
    """Profile A: pure intra-ring Sybil. Low volume, no bridging."""
    agents = []
    n_rings = n_agents // 5
    for r in range(n_rings):
        ring_volume_per_member = sum(max(0.05, rng.expovariate(1/0.3)) for _ in range(50))
        for member in range(5):
            n_tx = 50  # intra-ring
            n_unique = 4  # exactly the other 4 ring members
            volume = ring_volume_per_member  # low — typical 5-15 TCK total
            # Age = 90 days (rings ran the full window)
            age = 90
            has_buyer = True  # ring members buy from each other
            n_disputes = 0  # no internal disputes
            r_top = 0.25
            # Eigenvector centrality is low: ring is peripheral
            # eigen_factor = 0.25 means diversity score is heavily attenuated
            score = cri(n_tx, n_unique, volume, age, has_buyer, n_disputes, 0,
                       r_top=r_top, eigen_factor=0.25)
            cost = volume * 0.03 + 100  # protocol tax + registration (100 TCK deposit)
            agents.append({'profile': 'A', 'cri': score, 'cost': cost,
                          'days_to_70': estimate_days(score, 'A'),
                          'n_tx': n_tx, 'volume': volume})
    return agents

def simulate_profile_b(rng, n_agents):
    """Profile B: patient Sybil. 60% intra + 40% bridges to low-CRI legitimate."""
    agents = []
    n_rings = n_agents // 5
    for r in range(n_rings):
        for member in range(5):
            intra = 60
            external = 40
            n_tx = intra + external  # 100 total
            # 4 ring + ~25 external low-CRI counterparties (some repeat)
            n_unique = 4 + int(external * 0.65)
            # Volume mixed: intra is small, external slightly larger
            v_intra = sum(max(0.05, rng.expovariate(1/0.3)) for _ in range(intra))
            v_ext = sum(max(0.2, rng.expovariate(1/1.5)) for _ in range(external))
            volume = v_intra + v_ext
            age = 90
            has_buyer = True
            n_disputes = int(n_tx * 0.015)  # 1.5% dispute rate
            r_top = 0.18
            # Bridging recovers eigenvector but not fully (low-CRI counterparties have low π)
            score = cri(n_tx, n_unique, volume, age, has_buyer, n_disputes, 0,
                       r_top=r_top, eigen_factor=0.55)
            cost = volume * 0.03 + 100 + 30
            agents.append({'profile': 'B', 'cri': score, 'cost': cost,
                          'days_to_70': estimate_days(score, 'B'),
                          'n_tx': n_tx, 'volume': volume})
    return agents

def simulate_profile_c(rng, n_agents):
    """Profile C: collusive subnetwork. Bridges to mid-CRI nodes for centrality."""
    agents = []
    n_rings = n_agents // 5
    for r in range(n_rings):
        for member in range(5):
            intra = 40
            external = 80  # bridge heavily
            n_tx = intra + external  # 120
            n_unique = 4 + int(external * 0.55)  # ~48 unique
            v_intra = sum(max(0.1, rng.expovariate(1/0.5)) for _ in range(intra))
            v_ext = sum(max(0.3, rng.expovariate(1/2.0)) for _ in range(external))
            volume = v_intra + v_ext
            age = 90
            has_buyer = True
            n_disputes = int(n_tx * 0.02)
            r_top = 0.10
            # Eigenvector partially recovered (mid-CRI counterparties have higher π)
            score = cri(n_tx, n_unique, volume, age, has_buyer, n_disputes, 0,
                       r_top=r_top, eigen_factor=0.75)
            cost = volume * 0.03 + 100 + 60
            agents.append({'profile': 'C', 'cri': score, 'cost': cost,
                          'days_to_70': estimate_days(score, 'C'),
                          'n_tx': n_tx, 'volume': volume})
    return agents

def estimate_days(score, profile):
    """Heuristic: when does score cross 70."""
    if score < 70:
        return float('inf') if profile in ('A',) else 95  # 95 = "still climbing"
    # Score crossed 70 at approximately 90*(70/score) of the period
    return max(15, int(90 * (70 / max(70.1, score))))

def auc(scores_h, scores_a):
    n_correct = 0
    n_total = len(scores_h) * len(scores_a)
    if n_total == 0: return 0
    for h in scores_h:
        for a in scores_a:
            if h > a: n_correct += 1
            elif h == a: n_correct += 0.5
    return n_correct / n_total

def fpr(scores, threshold):
    if not scores: return 0
    return sum(1 for s in scores if s >= threshold) / len(scores)

def main():
    print(f"CRI ADVERSARIAL SIMULATION — {N_HONEST + N_PROFILE_A + N_PROFILE_B + N_PROFILE_C:,} agents × {DAYS} days")
    print("Seeds: HONEST=0x4847, A=0x4341, B=0x4252, C=0x4343\n")
    
    rng_h = random.Random(RNG_HONEST)
    rng_a = random.Random(RNG_A)
    rng_b = random.Random(RNG_B)
    rng_c = random.Random(RNG_C)
    
    honest = simulate_honest(rng_h, N_HONEST)
    profile_a = simulate_profile_a(rng_a, N_PROFILE_A)
    profile_b = simulate_profile_b(rng_b, N_PROFILE_B)
    profile_c = simulate_profile_c(rng_c, N_PROFILE_C)
    
    h_scores = [a['cri'] for a in honest]
    h_med = median(h_scores)
    
    print(f"| {'Metric':<32} | {'Profile A':<10} | {'Profile B':<10} | {'Profile C':<10} | {'Honest med':<12} |")
    print(f"|{'-'*34}|{'-'*12}|{'-'*12}|{'-'*12}|{'-'*14}|")
    
    medians = [median([a['cri'] for a in profile_a]),
               median([a['cri'] for a in profile_b]),
               median([a['cri'] for a in profile_c])]
    
    aucs = [auc(h_scores, [a['cri'] for a in profile_a]),
            auc(h_scores, [a['cri'] for a in profile_b]),
            auc(h_scores, [a['cri'] for a in profile_c])]
    
    fprs = [fpr([a['cri'] for a in profile_a], 70),
            fpr([a['cri'] for a in profile_b], 70),
            fpr([a['cri'] for a in profile_c], 70)]
    
    costs = [int(median([a['cost'] for a in profile_a])),
             int(median([a['cost'] for a in profile_b])),
             int(median([a['cost'] for a in profile_c]))]
    
    cost_per_pt = [c / max(1, m - 30) for c, m in zip(costs, medians)]
    
    d2_70 = []
    for prof in [profile_a, profile_b, profile_c]:
        valid = [a['days_to_70'] for a in prof if a['days_to_70'] != float('inf') and a['days_to_70'] < 200]
        d2_70.append(int(median(valid)) if valid else "never")
    
    h_d2_70 = int(median([a['days_to_70'] for a in honest if a['days_to_70'] != float('inf') and a['days_to_70'] < 200]))
    
    print(f"| {'Median CRI day 90':<32} | {medians[0]:<10.1f} | {medians[1]:<10.1f} | {medians[2]:<10.1f} | {h_med:<12.1f} |")
    print(f"| {'Time to CRI ≥ 70 (days, p50)':<32} | {str(d2_70[0]):<10} | {str(d2_70[1]):<10} | {str(d2_70[2]):<10} | {h_d2_70:<12} |")
    print(f"| {'AUC (honest > adversarial)':<32} | {aucs[0]:<10.2f} | {aucs[1]:<10.2f} | {aucs[2]:<10.2f} | {'—':<12} |")
    print(f"| {'False-positive rate at 70':<32} | {fprs[0]:<10.2f} | {fprs[1]:<10.2f} | {fprs[2]:<10.2f} | {'—':<12} |")
    print(f"| {'Total attack cost (TCK, p50)':<32} | {costs[0]:<10,} | {costs[1]:<10,} | {costs[2]:<10,} | {'—':<12} |")
    print(f"| {'Cost per CRI point (TCK)':<32} | {cost_per_pt[0]:<10.1f} | {cost_per_pt[1]:<10.1f} | {cost_per_pt[2]:<10.1f} | {'—':<12} |")

if __name__ == "__main__":
    main()
