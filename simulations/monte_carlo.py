import numpy as np


def simulate_independent(
    mean_a: float,
    mean_b: float,
    std_a: float = 12.0,
    std_b: float = 12.0,
    simulations: int = 10000,
):
    """
    Independent Monte Carlo simulation.
    Assumes team scores are independent.
    """

    scores_a = np.random.normal(mean_a, std_a, simulations)
    scores_b = np.random.normal(mean_b, std_b, simulations)

    margin = scores_a - scores_b
    win_prob = np.mean(margin > 0)

    return {
        "win_probability": win_prob,
        "expected_margin": np.mean(margin),
        "margin_std": np.std(margin),
        "scores_a": scores_a,
        "scores_b": scores_b,
        "margin_distribution": margin,
    }


def simulate_correlated(
    mean_a: float,
    mean_b: float,
    std_a: float = 12.0,
    std_b: float = 12.0,
    correlation: float = 0.2,
    simulations: int = 10000,
):
    """
    Monte Carlo with correlation between scores.
    Useful for pace-driven games or systemic effects.
    """

    cov_matrix = [
        [std_a**2, correlation * std_a * std_b],
        [correlation * std_a * std_b, std_b**2],
    ]

    means = [mean_a, mean_b]

    samples = np.random.multivariate_normal(means, cov_matrix, simulations)

    scores_a = samples[:, 0]
    scores_b = samples[:, 1]

    margin = scores_a - scores_b
    win_prob = np.mean(margin > 0)

    return {
        "win_probability": win_prob,
        "expected_margin": np.mean(margin),
        "margin_std": np.std(margin),
        "scores_a": scores_a,
        "scores_b": scores_b,
        "margin_distribution": margin,
    }