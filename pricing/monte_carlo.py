import numpy as np

class MonteCarloPricer:
    def __init__(self, option, spot, vol_surface, r=0.01):
        self.option = option
        self.spot = spot
        self.vol_surface = vol_surface
        self.r = r

    def simulate_paths(self, n_paths=10000, n_steps=100):
        dt = self.option.maturity / n_steps
        S_paths = np.zeros((n_paths, n_steps + 1))
        S_paths[:, 0] = self.spot.get_price()
        sigma = self.vol_surface.get_vol()
        for t in range(1, n_steps + 1):
            Z = np.random.normal(size=n_paths)
            S_paths[:, t] = S_paths[:, t-1] * np.exp((self.r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)
        return S_paths

    def price(self, n_paths=100000, n_steps=100):
        S_paths = self.simulate_paths(n_paths, n_steps)
        payoff = self.option.payoff(S_paths[:, -1])
        price = np.exp(-self.r * self.option.maturity) * np.mean(payoff)
        return price

class MonteCarloPricerMultiAsset:
    def __init__(self, option, spot_list, vol_list, corr_matrix, r=0.01):
        self.option = option
        self.spot_list = np.array(spot_list)
        self.vol_list = np.array(vol_list)
        self.corr_matrix = np.array(corr_matrix)
        self.r = r
        self.n_assets = len(spot_list)
        self.cholesky = np.linalg.cholesky(self.corr_matrix)

    def simulate_paths(self, n_paths=10000, n_steps=100):
        dt = self.option.maturity / n_steps
        S_paths = np.zeros((n_paths, n_steps + 1, self.n_assets))
        S_paths[:, 0, :] = self.spot_list
        for t in range(1, n_steps + 1):
            Z = np.random.normal(size=(n_paths, self.n_assets))
            correlated_Z = Z @ self.cholesky.T
            for i in range(self.n_assets):
                S_paths[:, t, i] = S_paths[:, t-1, i] * np.exp(
                    (self.r - 0.5 * self.vol_list[i]**2)*dt + self.vol_list[i]*np.sqrt(dt)*correlated_Z[:, i]
                )
        return S_paths

    def price(self, n_paths=100000, n_steps=100):
        S_paths = self.simulate_paths(n_paths, n_steps)
        # Take last time step, average over assets for basket payoff
        payoff = self.option.payoff(S_paths[:, -1, :])
        return np.exp(-self.r * self.option.maturity) * np.mean(payoff)
