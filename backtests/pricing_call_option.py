from market.spot import Spot
from market.vol_surface import VolSurface
from pricing.options import EuropeanOption
from pricing.monte_carlo import MonteCarloPricer
from risk.greeks import delta
from backtests.delta_hedge import delta_hedge

spot = Spot(100)
vol = VolSurface(0.2)
option = EuropeanOption(100, 1.0, 'call')

pricer = MonteCarloPricer(option, spot, vol)
price = pricer.price()
print(f"European Call Price: {price:.2f}")

d = delta(option, spot, vol)
print(f"Delta: {d:.4f}")

pnl_mean, pnl_std = delta_hedge(option, spot, vol)
print(f"Delta Hedging P&L: Mean={pnl_mean:.2f}, Std={pnl_std:.2f}")
