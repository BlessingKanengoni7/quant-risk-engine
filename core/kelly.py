def american_to_decimal(american_odds: float) -> float:
    """
    Convert American odds to decimal odds.
    """
    if american_odds > 0:
        return 1 + (american_odds / 100)
    else:
        return 1 + (100 / abs(american_odds))


def kelly_fraction(win_probability: float, decimal_odds: float) -> float:
    """
    Full Kelly fraction.
    Returns fraction of bankroll to wager.
    """
    b = decimal_odds - 1
    p = win_probability
    q = 1 - p

    if b <= 0:
        return 0.0

    kelly = (b * p - q) / b

    return max(kelly, 0.0)  # Never bet negative


def fractional_kelly(
    win_probability: float,
    decimal_odds: float,
    fraction: float = 0.5,
) -> float:
    """
    Fractional Kelly (safer).
    Default = Half Kelly.
    """
    full = kelly_fraction(win_probability, decimal_odds)
    return full * fraction