import csv
import settings
from execution.edge import calculate_edge, kelly_fraction
from execution.bankroll import update_bankroll

from quant_analytics.performance import calculate_roi, win_rate, sharpe_ratio
from quant_analytics.drawdown import calculate_drawdown
from quant_analytics.portfolio import category_summary

INITIAL_BANKROLL = settings.INITIAL_BANKROLL
BANKROLL = INITIAL_BANKROLL
EDGE_THRESHOLD = settings.EDGE_THRESHOLD
HALF_KELLY = settings.HALF_KELLY

equity_curve = [BANKROLL]
returns = []
results_list = []

category_stats = {}

print("===== ADVANCED QUANT ENGINE =====\n")

with open("datasets/events.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        model_prob = float(row["model_prob"])
        odds = int(row["market_odds"])
        result = int(row["result"])
        category = row["category"]

        edge = calculate_edge(model_prob, odds)

        if category not in category_stats:
            category_stats[category] = {"profits": [], "results": []}

        if edge > EDGE_THRESHOLD:
            kelly = kelly_fraction(model_prob, odds)
            stake_fraction = kelly * HALF_KELLY

            previous_bankroll = BANKROLL

            BANKROLL = update_bankroll(
                bankroll=BANKROLL,
                stake_fraction=stake_fraction,
                odds=odds,
                result=result
            )

            profit = BANKROLL - previous_bankroll
            returns.append(profit / previous_bankroll)
            results_list.append(result)

            category_stats[category]["profits"].append(profit)
            category_stats[category]["results"].append(result)

        equity_curve.append(BANKROLL)

# ---- PERFORMANCE METRICS ----

roi = calculate_roi(INITIAL_BANKROLL, BANKROLL)
wr = win_rate(results_list)
sharpe = sharpe_ratio(returns)
max_dd = calculate_drawdown(equity_curve)

category_report = category_summary(category_stats)

# ---- OUTPUT ----

print("Final Bankroll:", round(BANKROLL, 2))
print("ROI:", round(roi * 100, 2), "%")
print("Win Rate:", round(wr * 100, 2), "%")
print("Sharpe Ratio:", round(sharpe, 4))
print("Max Drawdown:", round(max_dd * 100, 2), "%")

print("\n--- Category Breakdown ---")
for cat, stats in category_report.items():
    print(
        f"{cat} | Bets: {stats['bets']} | "
        f"Wins: {stats['wins']} | "
        f"Profit: {round(stats['profit'], 2)}"
    )

print("\n=====================================")