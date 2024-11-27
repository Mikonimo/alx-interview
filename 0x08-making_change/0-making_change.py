#!/usr/bin/python3
"""This module contains a common interview question"""


def makeChange(coins, total):
    """
    Determine the fewes number of coins needed to meet a given total
    Args:
        coins: List of integers, the coin denominations available
        total: Integer, the total amount to be achieved
    Returns:
        Fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Initiate a list to store the minimum coins for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Basecase: 0 coins needed to make 0

    # Iterate over each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
