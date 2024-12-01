#!/usr/bin/python3
"""This module contains a common interview question"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet
    a given total using BFS.

    :param coins: List of integers, the coin denominations
    available.
    :param total: Integer, the total amount to be achieved.
    :return: Fewest number of coins needed to meet total,
    or -1 if not possible.
    """
    if total <= 0:
        return 0

    from collections import deque

    # Remove duplicates and filter out coins larger than total
    coins = list(set(filter(lambda x: x <= total, coins)))
    if not coins:
        return -1

    # Initialize the BFS queue
    queue = deque([(0, 0)])  # Each element is a tuple
    visited = set([0])  # Keep track of visited amounts to prevent revisiting

    while queue:
        current_amount, num_coins = queue.popleft()

        # Try all possible coins
        for coin in coins:
            next_amount = current_amount + coin
            if next_amount == total:
                return num_coins + 1
            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, num_coins + 1))

    return -1
