import csv
from execution.edge import calculate_edge, kelly_fraction
from execution.bankroll import update_bankroll
from quant_analytics.performance import calculate_roi, win_rate, sharpe_ratio
from quant_analytics.drawdown import calculate_drawdown
from quant_analytics.portfolio import category_summary


def run_engine(
    file_path,
    initial_bankroll,
    edge_threshold,
    half_kelly
):
    BANKROLL = initial_bankroll

    equity_curve = [BANKROLL]
    returns = []
    results_list = []
    category_stats = {}

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            model_prob = float(row["model_prob"])
            odds = float(row["market_odds"])
            result = int(row["result"])
            category = row["category"]

            edge = calculate_edge(model_prob, odds)

            if category not in category_stats:
                category_stats[category] = {"profits": [], "results": []}

            if edge > edge_threshold:
                kelly = kelly_fraction(model_prob, odds)
                stake_fraction = kelly * half_kelly

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

    roi = calculate_roi(initial_bankroll, BANKROLL)
    wr = win_rate(results_list)
    sharpe = sharpe_ratio(returns)
    max_dd = calculate_drawdown(equity_curve)
    category_report = category_summary(category_stats)

    return {
        "final_bankroll": BANKROLL,
        "roi": roi,
        "win_rate": wr,
        "sharpe": sharpe,
        "max_drawdown": max_dd,
        "equity_curve": equity_curve,
        "category_report": category_report
    }