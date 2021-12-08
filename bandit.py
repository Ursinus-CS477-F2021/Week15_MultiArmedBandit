import numpy as np

class Bandit:
    def __init__(self, K, seed):
        """
        Initialize a K-arm bandit

        Parameters
        ----------
        K: int
            Number of arms
        seed: int
            Seed for repeatability 
        """
        self.K = K
        np.random.seed(seed)
        self.sigmas = np.random.rand(K)
        self.mus = 5*np.abs(np.random.randn(K))
        self.mus += 3*self.sigmas

    def pull(self, k):
        """
        Pull the kth arm

        Parameters
        ----------
        k: int
            Arm index
        """
        return max(self.mus[k] + self.sigmas[k]*np.random.randn(), 0)
    

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