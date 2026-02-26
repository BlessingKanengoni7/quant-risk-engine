# quant_analytics/drawdown.py

def calculate_drawdown(equity_curve):
    if not equity_curve:
        return 0

    peak = equity_curve[0]
    max_drawdown = 0

    for value in equity_curve:
        if value > peak:
            peak = value

        drawdown = (peak - value) / peak

        if drawdown > max_drawdown:
            max_drawdown = drawdown

    return max_drawdown