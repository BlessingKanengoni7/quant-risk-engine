# execution/bankroll.py

def update_bankroll(bankroll, stake_fraction, odds, result):
    decimal_odds = 1 + (100 / abs(odds)) if odds < 0 else 1 + (odds / 100)
    b = decimal_odds - 1

    stake = bankroll * stake_fraction

    if result == 1:
        bankroll += stake * b
    else:
        bankroll -= stake

    return bankroll