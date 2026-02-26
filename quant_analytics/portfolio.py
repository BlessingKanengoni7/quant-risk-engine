# quant_analytics/portfolio.py

def category_summary(category_stats):
    report = {}

    for category, data in category_stats.items():
        profits = data.get("profits", [])
        results = data.get("results", [])

        total_profit = sum(profits)
        total_bets = len(results)
        wins = sum(results)

        report[category] = {
            "profit": total_profit,
            "bets": total_bets,
            "wins": wins
        }

    return report