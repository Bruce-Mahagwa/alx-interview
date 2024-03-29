#!/usr/bin/python3

""" Functions that determine the outcome of a game 
    The game is a prime game and it returns the winner of the game
"""


""" Checks if a number is even or odd """


def isEven(n):
    """ checks if a number is even"""
    if n % 2 == 0:
        return True
    return False


"""Checks if a number is prime or not """


def isPrime(n):
    """ returns true if a number is prime"""
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    prime = True
    for i in range(2, round(n ** 0.5 + 1)):
        if n % i == 0:
            prime = False
            break
    return prime


"""Checks for the winner in the prime game """


def isWinner(x, nums):
    """Finds the winner of a game based on repetition
        returns winner's name
    """
    if (len(nums) == 0:
        return None
    ben = 0
    maria = 0
    i = 0
    while i < len(nums):
        options = []
        ele = nums[i]
        for j in range(1, ele + 1):
            if (isPrime(j) == True):
                options.append(j)
        if len(options) == 0:
            ben += 1
        elif isEven(len(options)):
            ben += 1
        else: 
            maria += 1
        i+=1;
    if ben > maria:
        return "Ben"
    return "Maria"
