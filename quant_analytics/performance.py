# analytics/performance.py

import statistics


def calculate_roi(initial, final):
    return (final - initial) / initial


def win_rate(results):
    if not results:
        return 0

    wins = sum(results)
    return wins / len(results)


def sharpe_ratio(returns):
    if len(returns) < 2:
        return 0

    avg_return = statistics.mean(returns)
    std_dev = statistics.stdev(returns)

    if std_dev == 0:
        return 0

    return avg_return / std_dev