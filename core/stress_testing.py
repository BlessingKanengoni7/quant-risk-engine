def apply_stress(mean_a, mean_b, stress_factor_a=0.0, stress_factor_b=0.0):
    """
    Applies stress adjustments to means.
    Example: injury shock, fatigue, systemic disruption.
    """

    stressed_a = mean_a + stress_factor_a
    stressed_b = mean_b + stress_factor_b

    return stressed_a, stressed_b