import numpy as np
from math import erf, sqrt


def normal_cdf(x: float, mean: float = 0.0, std: float = 1.0) -> float:
    """
    Compute cumulative probability for a normal distribution.
    """
    z = (x - mean) / (std * sqrt(2))
    return 0.5 * (1 + erf(z))


def normal_probability_above(threshold: float, mean: float, std: float) -> float:
    """
    Probability that X > threshold for X ~ N(mean, std^2)
    """
    return 1 - normal_cdf(threshold, mean, std)


def normal_probability_below(threshold: float, mean: float, std: float) -> float:
    """
    Probability that X < threshold
    """
    return normal_cdf(threshold, mean, std)


def calibrate_std_from_data(historical_values):
    """
    Estimate realistic standard deviation from historical data.
    """
    return np.std(historical_values)


def analytical_win_probability(mean_margin: float, std_margin: float) -> float:
    """
    Computes win probability analytically assuming
    margin ~ Normal(mean_margin, std_margin^2)
    P(margin > 0)
    """
    return 1 - normal_cdf(0, mean_margin, std_margin)