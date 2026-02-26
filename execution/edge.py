# execution/edge.py

def implied_probability(decimal_odds):
    return 1 / decimal_odds


def calculate_edge(model_prob, decimal_odds):
    market_prob = implied_probability(decimal_odds)
    return model_prob - market_prob


def kelly_fraction(model_prob, decimal_odds):
    b = decimal_odds - 1
    q = 1 - model_prob

    kelly = ((b * model_prob) - q) / b
    return max(kelly, 0)