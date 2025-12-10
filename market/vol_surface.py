

class VolSurface:
    def __init__(self, sigma):
        self.sigma = sigma

    def get_vol(self, strike=None, maturity=None):
        return self.sigma