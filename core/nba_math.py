# core/nba_math.py

import numpy as np
from .distributions import normal_cdf, normal_probability_above


DEFAULT_STD = 12.0  # typical NBA team scoring std deviation


def expected_points(
    pace: float,
    off_rating: float,
    def_rating_opponent: float,
    home_advantage: float = 0.0,
    injury_adjustment: float = 0.0
) -> float:
    """
    Compute expected team points.
    Off/Def ratings are per 100 possessions.
    """
    efficiency_ratio = off_rating / def_rating_opponent
    return pace * efficiency_ratio + home_advantage + injury_adjustment


def score_difference_distribution(
    mu_home: float,
    mu_away: float,
    std_home: float = DEFAULT_STD,
    std_away: float = DEFAULT_STD
):
    """
    Return mean and std of score difference distribution.
    """
    mu_diff = mu_home - mu_away
    var_diff = std_home**2 + std_away**2
    std_diff = np.sqrt(var_diff)
    return mu_diff, std_diff


def home_win_probability(mu_home: float, mu_away: float) -> float:
    """
    Probability that home team wins.
    """
    mu_diff, std_diff = score_difference_distribution(mu_home, mu_away)
    return normal_probability_above(0, mu_diff, std_diff)


def spread_cover_probability(
    mu_home: float,
    mu_away: float,
    spread: float
) -> float:
    """
    Probability home covers spread.
    Spread is home line (e.g., -5.5).
    """
    mu_diff, std_diff = score_difference_distribution(mu_home, mu_away)
    return normal_probability_above(spread, mu_diff, std_diff)

def total_points_probability(
    mu_home: float,
    mu_away: float,
    line: float,
    std_home: float = DEFAULT_STD,
    std_away: float = DEFAULT_STD
) -> float:
    """
    Probability total points go OVER the given line.
    """
    mu_total = mu_home + mu_away
    var_total = std_home**2 + std_away**2
    std_total = np.sqrt(var_total)
    return normal_probability_above(line, mu_total, std_total)


def expected_total_points(mean_a, mean_b):
    return mean_a + mean_b

def total_points_std(std_a, std_b):
    return (std_a**2 + std_b**2) ** 0.5

from .distributions import normal_probability_above

def probability_over(line, mean_total, std_total):
    return normal_probability_above(line, mean_total, std_total)