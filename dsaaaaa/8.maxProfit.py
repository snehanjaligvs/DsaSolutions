def maxProfit(prices):
    n = len(prices)
    maxProfit = 0
    minPrice = prices[0]
    for i in range(1, n):
            maxProfit = max(maxProfit, prices[i] - minPrice)
            minPrice  = min(minPrice, prices[i])
    return maxProfit

arr =  [7,1,5,3,6,4]
print(maxProfit(arr))