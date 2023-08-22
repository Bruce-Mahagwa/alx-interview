#!/usr/bin/python3
"""
Find least number of coins to make change with
"""


def makeChange(coins, total):
    """
    When given acertain number of coins, determine the least amount of coins neeed to make change

    Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1

        - Coins is a list of the values of the coins in your possession
        - The value of a coin will always be an integer greater than 0
        - You can assume you have an infinite number of each denomination of
        coin in the list
    """
    if total <= 0:
        return 0

    temp = total + 1

    obj = {0: 0}

    for i in range(1, total + 1):
        obj[i] = temp

        for coin in coins:
            count = i - coin
            if count < 0:
                continue

            obj[i] = min(obj[count] + 1, obj[i])

    if obj[total] == total + 1:
        return -1

    return obj[total]
