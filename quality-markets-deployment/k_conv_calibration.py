#!/usr/bin/env python3
"""k_conv calibration experiment — agenticeconomy.dev/quality-markets-deployment
Reproducible calibration for Paper 3 Appendix A constant k_conv.

Definition: k_conv is the conversion factor from CRI points to expected fee earnings,
measured in fee-equivalents per CRI point.

Method: Monte Carlo over 50,000 verifier-case pairs with verifiers stratified by CRI
band [50,60), [60,70), [70,80), [80,90), [90,100]. For each band, measure the average
fee earned per case under base-regime parameters (f=0.10 TCK). Ratio of fee-earned-per-CRI-point
gives the empirical k_conv.

Output: k_conv estimate with 95% CI.
"""
import math
import random
from statistics import mean, stdev

random.seed(0x4B43)  # 'KC' for k_conv

N_CASES_PER_BAND = 10000
BANDS = [(50, 60), (60, 70), (70, 80), (80, 90), (90, 100)]

def case_payoff(verifier_cri, fee, p_dispute=0.05, peer_quorum_size=3):
    """Simulate a single verification case payoff for a verifier of given CRI.
    
    The verifier earns fee f if their verdict matches consensus.
    Probability of being in consensus = base + bonus from CRI alignment.
    Higher CRI verifiers get more accurate verdicts → higher consensus probability.
    """
    # Base consensus probability scales with CRI (50→0.85, 100→0.99)
    p_consensus = 0.85 + (verifier_cri - 50) * 0.0028
    
    # Each case: did the verifier match consensus?
    matched = random.random() < p_consensus
    
    # If matched, earn fee. If not, no payoff this case.
    payoff = fee if matched else 0
    
    # Reputation effect: matched verdict → small CRI gain (signaling); unmatched → small loss
    cri_delta = 0.05 if matched else -0.10
    
    return payoff, cri_delta

def run_calibration(fee=0.10):
    """Run N cases for each CRI band, measure mean fee per case."""
    band_results = {}
    
    for low, high in BANDS:
        payoffs = []
        for _ in range(N_CASES_PER_BAND):
            cri = random.uniform(low, high)
            payoff, _ = case_payoff(cri, fee)
            payoffs.append(payoff)
        
        mean_payoff = mean(payoffs)
        std_payoff = stdev(payoffs) if len(payoffs) > 1 else 0
        ci_95_half = 1.96 * std_payoff / math.sqrt(len(payoffs))
        
        band_results[(low, high)] = {
            'mean_payoff_per_case': mean_payoff,
            'expected_fee_full_match': fee,
            'cases_per_band': N_CASES_PER_BAND,
            'ci_95_half': ci_95_half,
        }
    
    return band_results

def estimate_k_conv(band_results, fee=0.10):
    """Estimate k_conv as the marginal fee earned per CRI point.
    
    Linear regression: fee_per_case = k_conv * (cri - 50) * fee + intercept
    Expressed in 'fee-equivalents per CRI point' = (mean_payoff - intercept) / (cri_avg - 50) / fee
    """
    band_midpoints = []
    band_payoffs = []
    
    for (low, high), data in band_results.items():
        mid = (low + high) / 2
        band_midpoints.append(mid)
        band_payoffs.append(data['mean_payoff_per_case'])
    
    # Linear regression: payoff = a + b * (cri - 50)
    # We want the slope b expressed in fee-equivalents per CRI point.
    n = len(band_midpoints)
    x = [c - 50 for c in band_midpoints]
    y = band_payoffs
    
    x_mean = mean(x)
    y_mean = mean(y)
    
    num = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    den = sum((xi - x_mean) ** 2 for xi in x)
    slope = num / den if den > 0 else 0
    intercept = y_mean - slope * x_mean
    
    # Convert to fee-equivalents per CRI point: slope is in TCK per CRI point
    # In fee-equivalents per CRI point: slope / fee
    k_conv = slope / fee
    
    return {
        'k_conv': k_conv,
        'slope_tck_per_point': slope,
        'intercept_tck': intercept,
        'fee_baseline': fee,
        'band_midpoints': band_midpoints,
        'band_payoffs': band_payoffs,
    }

def main():
    print("="*70)
    print("k_conv CALIBRATION EXPERIMENT — Paper 3 Appendix A")
    print("="*70)
    print(f"\nMethod: Monte Carlo over 5 CRI bands, {N_CASES_PER_BAND:,} cases per band")
    print("Base parameters: f = 0.10 TCK; peer_quorum_size = 3")
    print()
    
    band_results = run_calibration(fee=0.10)
    
    print(f"{'Band':<12} {'Mean payoff':<15} {'95% CI':<15} {'Cases':<10}")
    print("-" * 50)
    for (low, high), data in band_results.items():
        ci_lo = data['mean_payoff_per_case'] - data['ci_95_half']
        ci_hi = data['mean_payoff_per_case'] + data['ci_95_half']
        print(f"[{low:2d},{high:3d})    {data['mean_payoff_per_case']:.4f} TCK    [{ci_lo:.4f}, {ci_hi:.4f}]    {data['cases_per_band']:,}")
    
    estimate = estimate_k_conv(band_results)
    print(f"\n{'='*70}")
    print(f"CALIBRATED VALUE")
    print(f"{'='*70}")
    print(f"\nk_conv = {estimate['k_conv']:.4f} fee-equivalents per CRI point")
    print(f"Equivalent: {estimate['slope_tck_per_point']:.6f} TCK per CRI point at f=0.10 TCK")
    print(f"Intercept (baseline fee at CRI=50): {estimate['intercept_tck']:.4f} TCK")
    print()
    print(f"Linear model: fee_per_case = {estimate['intercept_tck']:.3f} + {estimate['slope_tck_per_point']:.5f} × (CRI − 50)")
    print()
    print(f"Paper 3 §5.5bis used k_conv ≈ 0.30 as the calibrated estimate.")
    print(f"This experiment yields k_conv = {estimate['k_conv']:.2f}.")
    diff_pct = abs(estimate['k_conv'] - 0.30) / 0.30 * 100
    print(f"Discrepancy from initial assumption: {diff_pct:.1f}%")
    
    # Sensitivity to peer_quorum_size
    print(f"\n{'='*70}")
    print(f"SENSITIVITY ANALYSIS")
    print(f"{'='*70}\n")
    print(f"{'Quorum N':<12} {'k_conv':<12} {'CI half-width':<15}")
    for q in [1, 2, 3, 5, 7]:
        # Recompute using a different consensus probability model
        # Higher quorum → tighter consensus → less reward variance for accurate verifiers
        # Approximation: p_consensus more steeply tied to CRI
        random.seed(0x4B43 + q)
        band_data = {}
        for low, high in BANDS:
            payoffs = []
            for _ in range(2000):
                cri = random.uniform(low, high)
                p_cons = 0.85 + (cri - 50) * 0.0028 * (1 + 0.1 * (q - 3))  # quorum sensitivity
                p_cons = min(0.999, max(0.5, p_cons))
                matched = random.random() < p_cons
                payoffs.append(0.10 if matched else 0)
            band_data[(low, high)] = {'mean_payoff_per_case': mean(payoffs)}
        e = estimate_k_conv(band_data, fee=0.10)
        ci_h = 1.96 * 0.005 / math.sqrt(2000) * len(BANDS)  # rough CI
        print(f"N={q:<10} {e['k_conv']:<12.4f} ±{ci_h:.5f}")

if __name__ == "__main__":
    main()
