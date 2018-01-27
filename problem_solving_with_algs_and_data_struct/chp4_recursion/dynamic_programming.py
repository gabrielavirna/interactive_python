"""
Dynamic programming is one strategy for optimization problems, e.g. find the shortest path between two
points, find the line that best fits a set of points, or find the smallest set of objects that satisfies some criteria.


A classic example of an optimization problem: making change using the fewest coins.

-> Greedy method: (try to solve as big a piece of the problem as possible right away).
Suppose you are a programmer for a vending machine manufacturer. Your company wants to streamline effort by giving out
the fewest possible coins in change for each transaction. Suppose a customer puts in a dollar bill and purchases an item
for 37 cents. What is the smallest number of coins you can use to make change?
The answer is six coins: two quarters, one dime, and three pennies.
Strategy to answer: We start with the largest coin in our arsenal (a quarter) and use as many of those as possible, then
we go to the next lowest coin value and use as many of those as possible.

-> Recursive solution: (start with identifying the base case).
If we are trying to make change for the same amount as the value of one of our coins, the base case is easy, one coin.
If the amount does not match we have several options.

num_coins = min {1 + num_coins(original_amount - 1), 1 + num_coins(original_amount - 5),
                 1 + num_coins(original_amount - 10, 1 + num_coins(original_amount - 25)}

"""


# I. Recursive solution: extremely inefficient => takes 67,716,925 recursive calls to find the optimal solution
# Problem: wasting a lot of time and effort recalculating old results.
def recursive_money_change(coin_value_list, change):
    min_coins = change
    # check for the base case: make change in the exact amount of one of our coins.
    if change in coin_value_list:
        return 1
    # if no coin = the amount of change, make recursive calls for each different coin value < the amount of change.
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + recursive_money_change(coin_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


# II.  Improved the performance of the program by using the technique: “memoization” /“caching.
# Improved recursive solution: Remembering some of the past results to avoid recomputing results we already know
# Store the results for the minimum number of coins in a table when we find them. Then before we compute a new minimum,
# first check the table to see if a result is already known. If there's a result in the table, use it.
def improved_money_change(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + improved_money_change(coin_value_list, change - i, known_results)

        if num_coins < min_coins:
            min_coins = num_coins
            known_results[change] = min_coins

    return min_coins


# The dynamic programming solution. Solution is going to start with making change for one cent and systematically work
# its way up to the amount of change we require => at each step of the algorithm we already know the minimum number of
# coins needed to make change for any smaller amount.
def dynamic_money_change(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        # coinCount: the min. no. coins used to make change for the amount corresponding to the pos. in coins_used list.
        coin_count = cents
        new_coin = 1
        # In this loop we consider using all possible coins to make change for the amount specified by cents.
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        # remember the minimum value and store it in minCoins list.
        min_coins[cents] = coin_count
        # keep track of the coins used by remembering the last coin we add for each entry in the minCoins table
        coins_used[cents] = new_coin
    return min_coins[cents]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin -= this_coin


def main():
    amount = 63
    coins = [1, 5, 10, 21, 25]
    # print(recursive_money_change(coins, amount))
    # print(improved_money_change(coins, amount, [0]*64))
    coins_used = [0]*(amount + 1)
    coin_count = [0]*(amount + 1)
    print("Making change for the {} requires: {} coins".format(amount,
          dynamic_money_change(coins, amount,coin_count, coins_used)))
    print_coins(coins_used, amount)
    print("and the list used is: {}".format(coins_used))

if __name__ == "__main__":
    main()

