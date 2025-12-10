import numpy as np
from risk.greeks import delta
from pricing.monte_carlo import MonteCarloPricer

def delta_hedge(option, spot, vol_surface, r=0.01, n_paths=10000, n_steps=100):
    """
    Simulate delta-hedging P&L for a European option.
    Returns mean and std of P&L across paths.
    """
    pricer = MonteCarloPricer(option, spot, vol_surface, r)
    S_paths = pricer.simulate_paths(n_paths, n_steps)
    dt = option.maturity / n_steps

    pnl_list = []
    for path in S_paths:
        cash = 0
        position = 0
        for t in range(n_steps):
            spot_price = path[t]
            # Compute delta at current step
            option_at_step = option
            current_delta = delta(option_at_step, spot, vol_surface, r, h=0.01, n_paths=2000, n_steps=10)
            # Rebalance
            d_position = current_delta - position
            cash -= d_position * spot_price
            position = current_delta
        # Liquidate at final spot
        pnl = position * path[-1] + cash - option.payoff(path[-1])
        pnl_list.append(pnl)
    return np.mean(pnl_list), np.std(pnl_list)
