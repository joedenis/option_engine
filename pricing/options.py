
import numpy as np
from abc import ABC, abstractmethod

class Option(ABC):
    def __init__(self, strike, maturity, option_type='call'):
        self.strike = strike
        self.maturity = maturity
        self.option_type = option_type

    @abstractmethod
    def payoff(self, S):
        pass

class EuropeanOption(Option):
    def payoff(self, S):
        if self.option_type == 'call':
            return np.maximum(S - self.strike, 0)
        elif self.option_type == 'put':
            return np.maximum(self.strike - S, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")
