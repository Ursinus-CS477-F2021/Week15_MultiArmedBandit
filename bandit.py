import numpy as np

class Bandit:
    def __init__(self, K, seed, change_lambda = 0):
        """
        Initialize a K-arm bandit

        Parameters
        ----------
        K: int
            Number of arms
        seed: int
            Seed for repeatability 
        change_lambda: float
            Probability that a mean will change at any given time
        """
        self.K = K
        np.random.seed(seed)
        self.sigmas = np.abs(np.random.randn(K))
        self.mus = np.random.randn(K)
        self.change_lambda = change_lambda

    def pull(self, k):
        """
        Pull the kth arm

        Parameters
        ----------
        k: int
            Arm index
        """
        res = self.mus[k] + self.sigmas[k]*np.random.randn()
        for i in range(self.K):
            if np.random.rand() < self.change_lambda:
                self.mus[i] = np.random.randn() # Change this bandit
        return res
    

def naive_maximize_reward(bandit, n_trials):
    """
    Implement a naive k-armed bandit policy which picks a random
    arm at the beginning and keeps using it

    Parameters
    ----------
    bandit: Bandit
        A K-armed bandit
    n_trials: int
        Number of pull to perform
    
    Returns
    -------
    float: 
        The amount of money made
    """
    money = 0
    k = np.random.randint(bandit.K)
    for trial in range(n_trials):
        # A naive strategy: Just pull bandit 0 every time
        money += bandit.pull(k)
    return money

def my_maximize_reward(bandit, n_trials):
    """
    Implement a smarter K-armed bandit policy

    Parameters
    ----------
    bandit: Bandit
        A K-armed bandit
    n_trials: int
        Number of pull to perform
    
    Returns
    -------
    float: 
        The amount of money made
    """
    money = 0
    ## TODO: Fill this in
    return money