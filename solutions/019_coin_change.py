# https://leetcode.com/problems/coin-change/description/

# Table is 1 by n, where n is amount
# Step length is just coins[i]
# Init coin counter
# Set range
# for x in coins if step relates to denomination by SOMETHING
# min check between current holder and new value
# Edge cases of 0 and unable to reach intermediate step
# return min for final step if no edge cases
# continue case is if no coin combinations give specific curr_amount

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Table length = 1 * (n + 1) so index into n is end of table
        MAX = 10 ** 4 + 1

        coin_counter = [0] + [MAX] * amount
        coin_counter[0] = 0
        for coin in coins:
            if coin <= amount:
                coin_counter[coin] = 1

        for curr_amount in range(1, amount + 1):
            if coin_counter[curr_amount] == MAX:
                continue
            for coin in coins:
                if curr_amount + coin <= amount:
                    coin_counter[curr_amount + coin] = min(
                        coin_counter[curr_amount] + 1,
                        coin_counter[curr_amount + coin]
                    )

        return coin_counter[-1] if coin_counter[-1] != MAX else -1

        # coin_counter = {}

        # def recursive_fn(amount):
        #     if amount in coin_counter:
        #         return coin_counter[amount]

        #     if amount == 0:
        #         return 0

        #     tally = []
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             tally.append(recursive_fn(amount - coin))
        #         else:
        #             tally.append(float('inf'))

        #     min_coins = min(tally) + 1
        #     coin_counter[amount] = min_coins
        #     return min_coins

        # res = recursive_fn(amount)
        # return res if res != float('inf') else -1
