# VISA full time master ph.D question.
# Complete the maxInversions function below.
def maxInversions(prices):
    count = 0
    for i in range(1, len(prices) - 1):
        small = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                small += 1
        big = 0
        for j in range(i - 1, -1, -1):
            if prices[i] < prices[j]:
                big += 1
        count += big * small
    return count
