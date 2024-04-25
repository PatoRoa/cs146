# You are given an integer array coins representing coins of different denominations and an integer amount representing
# a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
# any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    # Sets up the list with the amount of combinations for each value of the array's index
    combo = [0] * (amount + 1)

    # Only one way to make up 0 xd
    combo[0] = 1

    # Tabulation x-axis
    for i in range(len(coins)):
        # Tabulation y-axis
        for j in range(len(combo)):
            # If the value of the coin is less than or equal to than the amount given by the index of the array
            if coins[i] <= j:
                # Operation that mathematically creates the possible amount of coin combinations for each value
                combo[j] += combo[j - coins[i]]

    return combo[amount]


coins = [1, 2, 5]
amount = 11

print(coinChange(coins, amount))
