# tests/test_pricing.py
import pytest
from market.spot import Spot
from market.vol_surface import VolSurface
from pricing.options import EuropeanOption
from pricing.monte_carlo import MonteCarloPricer
from risk.greeks import delta, gamma, vega, theta

def test_monte_carlo_pricing():
    spot = Spot(100)
    vol = VolSurface(0.2)
    option = EuropeanOption(100, 1.0, 'call')
    pricer = MonteCarloPricer(option, spot, vol)
    price = pricer.price(n_paths=5000, n_steps=50)
    assert price > 0, "Price should be positive"

def test_greeks():
    spot = Spot(100)
    vol = VolSurface(0.2)
    option = EuropeanOption(100, 1.0, 'call')
    d = delta(option, spot, vol, n_paths=5000, n_steps=50)
    g = gamma(option, spot, vol, n_paths=5000, n_steps=50)
    v = vega(option, spot, vol, n_paths=5000, n_steps=50)
    t = theta(option, spot, vol, n_paths=5000, n_steps=50)
    assert all(isinstance(x, float) for x in [d, g, v, t])
