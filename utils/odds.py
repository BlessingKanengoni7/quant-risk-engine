# utils/odds.py

def american_to_decimal(odds: float) -> float:
    if odds > 0:
        return 1 + (odds / 100)
    else:
        return 1 + (100 / abs(odds))


def decimal_to_implied_prob(decimal_odds: float) -> float:
    return 1 / decimal_odds


def american_to_implied_prob(odds: float) -> float:
    decimal = american_to_decimal(odds)
    return decimal_to_implied_prob(decimal)