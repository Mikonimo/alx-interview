#!/usr/bin/python3
"""This file contains one of the common interview
questions"""


def isWinner(x, nums):
    """Determines the winner of the Prime Game

    Args:
        x (int): number of rounds
        num (list): array of n values for each round

    Returns:
        str: "Maria" if Maria wins more rounds,
            "Ben" if Ben wins more rounds
            None if a tie
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    # Sieve of Eratosthenes
    sieve = [True] * (max_n + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n+1, i):
                sieve[j] = False

    # Precompute prime counts (prefix sums)
    prime_count = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_count[i] = prime_count[i-1]
        if sieve[i]:
            prime_count[i] += 1

    m_wins = 0
    b_wins = 0

    for n in nums:
        # Determine winner of this round
        if prime_count[n] % 2 == 1:
            m_wins += 1
        else:
            b_wins += 1

    if m_wins > b_wins:
        return "Maria"
    elif b_wins > m_wins:
        return "Ben"
    else:
        return None
