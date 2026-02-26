# risk/kelly.py

def kelly_fraction(probability: float, decimal_odds: float) -> float:
    b = decimal_odds - 1
    q = 1 - probability
    return (b * probability - q) / b


def half_kelly(probability: float, decimal_odds: float) -> float:
    return max(0, kelly_fraction(probability, decimal_odds) / 2)