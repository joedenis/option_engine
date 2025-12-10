from pricing.monte_carlo import MonteCarloPricer
from types import SimpleNamespace

def delta(option, spot, vol_surface, r=0.01, h=0.01, n_paths=50000, n_steps=100):
    spot_up = SimpleNamespace(get_price=lambda: spot.get_price() + h)
    spot_down = SimpleNamespace(get_price=lambda: spot.get_price() - h)
    price_up = MonteCarloPricer(option, spot_up, vol_surface, r).price(n_paths, n_steps)
    price_down = MonteCarloPricer(option, spot_down, vol_surface, r).price(n_paths, n_steps)
    return (price_up - price_down) / (2 * h)

def gamma(option, spot, vol_surface, r=0.01, h=0.01, n_paths=50000, n_steps=100):
    spot_up = SimpleNamespace(get_price=lambda: spot.get_price() + h)
    spot_down = SimpleNamespace(get_price=lambda: spot.get_price() - h)
    price_up = MonteCarloPricer(option, spot_up, vol_surface, r).price(n_paths, n_steps)
    price = MonteCarloPricer(option, spot, vol_surface, r).price(n_paths, n_steps)
    price_down = MonteCarloPricer(option, spot_down, vol_surface, r).price(n_paths, n_steps)
    return (price_up - 2*price + price_down) / (h**2)

def vega(option, spot, vol_surface, r=0.01, h=0.01, n_paths=50000, n_steps=100):
    vol_up = SimpleNamespace(get_vol=lambda strike=None, maturity=None: vol_surface.get_vol() + h)
    vol_down = SimpleNamespace(get_vol=lambda strike=None, maturity=None: vol_surface.get_vol() - h)
    price_up = MonteCarloPricer(option, spot, vol_up, r).price(n_paths, n_steps)
    price_down = MonteCarloPricer(option, spot, vol_down, r).price(n_paths, n_steps)
    return (price_up - price_down) / (2*h)

def theta(option, spot, vol_surface, r=0.01, h=1/365, n_paths=50000, n_steps=100):
    option_up = SimpleNamespace(strike=option.strike, maturity=option.maturity - h, option_type=option.option_type,
                                payoff=option.payoff)
    price_up = MonteCarloPricer(option_up, spot, vol_surface, r).price(n_paths, n_steps)
    price = MonteCarloPricer(option, spot, vol_surface, r).price(n_paths, n_steps)
    return (price_up - price) / h
