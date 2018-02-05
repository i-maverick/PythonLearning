def get_max_profit(prices):
    if len(prices) < 2:
        return None

    profit = prices[1] - prices[0]
    min_price = None
    for x in prices:
        if min_price is None:
            min_price = x
        else:
            profit = max(profit, x - min_price)
            min_price = min(min_price, x)
    return profit


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
result = get_max_profit(stock_prices_yesterday)
print(result)
