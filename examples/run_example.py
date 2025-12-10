# examples/run_example.py
from market.spot import Spot
from market.vol_surface import VolSurface
from pricing.options import EuropeanOption
from pricing.monte_carlo import MonteCarloPricer, MonteCarloPricerMultiAsset
from risk.greeks import delta, gamma, vega, theta
from backtests.delta_hedge import delta_hedge
import numpy as np

# Single asset example
spot = Spot(100)
vol = VolSurface(0.2)
option = EuropeanOption(100, 1.0, 'call')

pricer = MonteCarloPricer(option, spot, vol)
price = pricer.price(n_paths=50000, n_steps=100)
print(f"Single-Asset European Call Price: {price:.2f}")

d = delta(option, spot, vol, n_paths=5000, n_steps=50)
print(f"Delta: {d:.4f}")

pnl_mean, pnl_std = delta_hedge(option, spot, vol)
print(f"Delta Hedging P&L: Mean={pnl_mean:.2f}, Std={pnl_std:.2f}")

# Multi-asset example
from pricing.options import EuropeanOption

option_multi = EuropeanOption(100, 1.0, 'call')  # simple basket payoff: average of assets
spot_list = [100, 105]
vol_list = [0.2, 0.25]
corr_matrix = [[1.0, 0.3], [0.3, 1.0]]

pricer_multi = MonteCarloPricerMultiAsset(option_multi, spot_list, vol_list, corr_matrix)
price_multi = pricer_multi.price(n_paths=50000, n_steps=100)
print(f"Multi-Asset Basket Call Price: {price_multi:.2f}")
