#!/usr/bin/env python3
"""Quality Markets Monte Carlo — agenticeconomy.dev/quality-markets-deployment
Reproducible simulation for Paper 3 §5.5ter Table 5 + §5.5quater cartel cost.
"""
import math
import random
from statistics import median, mean

DAYS = 90
N_VERIFIERS = 1000

def detection_probability(N_quorum, dishonest_count, honest_reject_rate=0.95):
    """Probability that a dishonest verdict is detected given quorum size and dishonest count."""
    # Probability honest_reject_rate that an honest verifier rejects substandard
    # If dishonest verdict diverges from majority, detected
    # Simple model: probability all honest verifiers accept = (1 - reject_rate)^honest_count
    honest_count = N_quorum - dishonest_count
    if honest_count <= 0:
        return 0  # full cartel, no detection
    p_honest_all_accept = (1 - honest_reject_rate) ** honest_count
    p_detect = 1 - p_honest_all_accept
    return p_detect

def cartel_inequality(b, f, p, cri_avg, cri_floor, k_conv, gamma=0.6):
    """Returns (lhs, rhs, viable). Cartel viable if lhs > rhs (E[U_dishonest] > E[U_honest])."""
    rhs = p * (cri_avg - cri_floor) * gamma * k_conv
    return (b, rhs, b > rhs)

def simulate_verifier_market(rng, N_verifiers, regime):
    """Simulate N verifiers over DAYS days under given regime."""
    if regime == 'base':
        f, b, p, N_quorum = 0.10, 0.5, 0.40, 3
    elif regime == 'low_p':
        f, b, p, N_quorum = 0.10, 0.5, 0.20, 3
    elif regime == 'high_b':
        f, b, p, N_quorum = 0.10, 1.0, 0.40, 3
    
    verifiers = []
    for i in range(N_verifiers):
        # Initial CRI log-normal around 60
        cri = max(50, min(100, rng.lognormvariate(4.1, 0.2)))
        # Decision strategy: honest with probability prop to (cri - 50)/50 if no incentive to defect
        # E[U_honest] = f
        # E[U_dishonest] = b - p * (cri - 50) * gamma * k_conv
        gamma, k_conv = 0.6, 0.3
        utility_honest = f
        utility_dishonest = b - p * max(0, cri - 50) * gamma * k_conv
        rational_honest = utility_honest >= utility_dishonest
        verifiers.append({
            'cri': cri,
            'rational_honest': rational_honest,
            'is_dishonest': False,
            'caught': False,
            'fees_earned': 0.0,
        })
    
    # Simulate cases
    n_cases_per_verifier = 30  # ~3 cases / week / verifier over 90 days
    n_caught = 0
    
    for v in verifiers:
        if not v['rational_honest']:
            v['is_dishonest'] = True
            for case in range(n_cases_per_verifier):
                # On each case, dishonest verifier may be caught
                if rng.random() < p:
                    v['caught'] = True
                    n_caught += 1
                    # Lose CRI per peer-prediction signal
                    v['cri'] = max(0, v['cri'] - (v['cri'] - 50) * gamma)
                    # Net payoff: bribe minus expected loss
                    v['fees_earned'] -= max(0, v['cri'] - 50) * gamma * k_conv
                    break  # single strike
                else:
                    v['fees_earned'] += b
        else:
            v['fees_earned'] = n_cases_per_verifier * f
    
    return verifiers, n_caught

def main():
    print("QUALITY MARKETS MONTE CARLO — Paper 3 §5.5ter")
    print(f"N = {N_VERIFIERS:,} verifiers × {DAYS} days × 3 regimes\n")
    
    rng = random.Random(0x5142)  # 'QB' Quality Brand
    
    print("| Metric                        | Base  | Low-p | High-b |")
    print("|-------------------------------|-------|-------|--------|")
    
    metrics = {}
    for regime in ['base', 'low_p', 'high_b']:
        rng_r = random.Random(0x5142 + hash(regime) % 1000)
        verifiers, caught = simulate_verifier_market(rng_r, N_VERIFIERS, regime)
        
        honest_verifiers = [v for v in verifiers if v['rational_honest']]
        dishonest_verifiers = [v for v in verifiers if not v['rational_honest']]
        
        honest_frac = len(honest_verifiers) / N_VERIFIERS
        med_cri = median([v['cri'] for v in verifiers])
        honest_earnings = int(sum(v['fees_earned'] for v in honest_verifiers))
        dishonest_earnings_p50 = median([v['fees_earned'] for v in dishonest_verifiers]) if dishonest_verifiers else 0
        
        metrics[regime] = {
            'honest_frac': honest_frac,
            'med_cri': med_cri,
            'honest_earnings': honest_earnings,
            'dishonest_p50': dishonest_earnings_p50,
            'caught': caught,
            'n_verifiers': N_VERIFIERS,
        }
    
    print(f"| Honest verifications fraction | {metrics['base']['honest_frac']:.2f}  | {metrics['low_p']['honest_frac']:.2f}  | {metrics['high_b']['honest_frac']:.2f}   |")
    print(f"| Median verifier CRI day 90    | {metrics['base']['med_cri']:.0f}    | {metrics['low_p']['med_cri']:.0f}    | {metrics['high_b']['med_cri']:.0f}     |")
    print(f"| Honest verifiers' earnings    | {metrics['base']['honest_earnings']:,} | {metrics['low_p']['honest_earnings']:,} | {metrics['high_b']['honest_earnings']:,}  |")
    print(f"| Defectors' net payoff (p50)   | {metrics['base']['dishonest_p50']:.1f}  | {metrics['low_p']['dishonest_p50']:.1f}  | {metrics['high_b']['dishonest_p50']:.1f}    |")
    print(f"| Defectors caught              | {metrics['base']['caught']}    | {metrics['low_p']['caught']}    | {metrics['high_b']['caught']}      |")
    
    # Cartel cost analysis
    print("\n\nCARTEL COST ANALYSIS — Paper 3 §5.5quater")
    print("E[U_dishonest] vs E[U_honest] for k=2 cartel\n")
    print("Calibration: p_detect(k=2) ≈ 0.55, CRI_avg = 65, CRI_floor = 50, k_conv = 0.30, γ = 0.6")
    
    for k in [2, 3, 4]:
        # P_detect for k-cartel facing N=3 quorum
        # Probability ≥1 honest verifier in N-quorum (different verifiers with each case)
        # Approximation: 1 - C(M-k, N) / C(M, N) for M total population
        M = 1000
        if k <= N_VERIFIERS - 3:
            # Probability all N=3 quorum members are from the cartel
            from math import comb
            p_all_cartel = comb(k, 3) / comb(M, 3) if k >= 3 else 0
            p_detect = 1 - p_all_cartel
        else:
            p_detect = 1.0
        
        # Cartel inequality: b > p * (cri_avg - cri_floor) * gamma * k_conv
        cri_avg, cri_floor = 65, 50
        gamma, k_conv = 0.6, 0.3
        threshold_b = p_detect * (cri_avg - cri_floor) * gamma * k_conv
        print(f"  k={k}: P_detect = {p_detect:.4f}, cartel viable iff b > {threshold_b:.2f} TCK")

if __name__ == "__main__":
    main()
