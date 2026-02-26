import numpy as np


def calculate_var(margin_distribution, confidence=0.95):
    """
    Value at Risk (VaR) style metric on margin.
    """
    percentile = np.percentile(margin_distribution, (1 - confidence) * 100)
    return percentile


def expected_shortfall(margin_distribution, confidence=0.95):
    """
    Conditional VaR (Expected Shortfall).
    """
    var_level = calculate_var(margin_distribution, confidence)
    losses = margin_distribution[margin_distribution <= var_level]
    return np.mean(losses)


def risk_summary(simulation_output):
    """
    Generates full risk summary dictionary.
    """
    margin = simulation_output["margin_distribution"]

    return {
        "win_probability": simulation_output["win_probability"],
        "expected_margin": simulation_output["expected_margin"],
        "margin_std": simulation_output["margin_std"],
        "VaR_95": calculate_var(margin, 0.95),
        "Expected_Shortfall_95": expected_shortfall(margin, 0.95),
    }