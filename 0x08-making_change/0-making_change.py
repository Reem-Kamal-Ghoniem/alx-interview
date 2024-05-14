#!/usr/bin/python3

""" here in this fileyou can find makeChange function"""


def makeChange(coins, total):
    """
    Returns: least number of coins to meet the total value
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
