# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy | **Topics:** Array, Dynamic Programming, Sliding Window

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

---

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on day `i`.

You want to maximize your profit by choosing a **single day to buy** one stock and choosing a **different day in the future to sell** it. Return the maximum profit you can achieve. If you cannot achieve any profit, return `0`.

**Example 1**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed, because you must buy before you sell.
```

**Example 2**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: Prices only fall, so no transaction is done and the max profit is 0.
```

**Constraints**
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Intuition and Key Insight

For each potential sell day, the best buy day is the **cheapest price seen before it**. So you don't need to try every pair. You only need to remember the lowest price so far and compare against it as you scan.

Your two-pointer version expresses this directly: `l` is the buy day, `r` is the sell day.
- If `prices[r] > prices[l]`, the trade is profitable, so record it.
- Otherwise `prices[r]` is a new cheapest price (or tied), and any future sell is at least as good when bought at `r` instead of `l`, so move `l` to `r`.

**Pattern to recognize:** "best pair (i < j) maximizing `a[j] - a[i]`" → track the running minimum (or a sliding window) in one pass.

---

## Approaches

### 1. Brute Force: Try Every Buy/Sell Pair

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n):
            for j in range(i + 1, n):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit
```

- **Time:** O(n²)
- **Space:** O(1)
- **Verdict:** With n up to 10^5 that's about 5 x 10^9 pair checks, so it will time out. Mention it as the baseline, then optimize.

### 2. One Pass, Track Minimum Price

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)               # cheapest buy so far
            max_profit = max(max_profit, price - min_price) # best sell today
        return max_profit
```

- **Time:** O(n)
- **Space:** O(1)
- **Verdict:** The most common textbook answer. It is logically the same as your two-pointer solution, since `prices[l]` is always the running minimum.

### 3. Two Pointers / Sliding Window (Optimal)

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1                       # l = buy day, r = sell day
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:     # profitable trade
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r                     # found a new lowest price, buy here instead
            r += 1                        # always advance the sell day

        return maxP
```

- **Time:** O(n), since `r` visits each index once and `l` only jumps forward
- **Space:** O(1)
- **Verdict:** Optimal. It is correct as written. This framing is useful because the same left/right pointer idea shows up in many sliding window problems.

### 4. Kadane's View (Dynamic Programming)

Let `diff[i] = prices[i] - prices[i-1]`. The profit of buying on day `i` and selling on day `j` equals the sum of daily differences from `i+1` to `j`, so the problem becomes **maximum subarray sum** (LC 53) over the differences.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur = 0                                   # best profit ending today
        for i in range(1, len(prices)):
            cur = max(0, cur + prices[i] - prices[i - 1])
            max_profit = max(max_profit, cur)
        return max_profit
```

- **Time:** O(n)
- **Space:** O(1)
- **Verdict:** Not needed for this problem, but it shows the link to Kadane's algorithm, which helps with the harder stock variants.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n²) | O(1) | TLE on large inputs |
| Track min price | **O(n)** | **O(1)** | **Optimal, simplest** |
| **Two pointers (yours)** | **O(n)** | **O(1)** | **Optimal, sliding window framing** |
| Kadane on differences | O(n) | O(1) | Connects to max subarray |

---

## Walkthrough (Two Pointers)

`prices = [7, 1, 5, 3, 6, 4]`

| l | r | prices[l] | prices[r] | Action | maxP |
|---|---|---|---|---|---|
| 0 | 1 | 7 | 1 | 7 < 1? No, so `l = 1` | 0 |
| 1 | 2 | 1 | 5 | profit 4 | 4 |
| 1 | 3 | 1 | 3 | profit 2 | 4 |
| 1 | 4 | 1 | 6 | profit 5 | **5** |
| 1 | 5 | 1 | 4 | profit 3 | 5 |

Result: `5`.

Decreasing case, `prices = [7, 6, 4, 3, 1]`: every step hits the `else` branch and `l` follows `r`, so `maxP` stays `0`.

---

## Why Moving `l = r` Is Safe

When `prices[r] <= prices[l]`, buying at `r` is at least as cheap as buying at `l`. Every future sell day after `r` gives an equal or better profit with the buy at `r`, so `l` can never be the better buy again. No candidate is skipped, which is why a single pass is enough.

---

## Edge Cases and Pitfalls

- **Single day** (`[5]`): `r = 1` is never `< len(prices)`, so the loop doesn't run and it returns `0`. Correct.
- **Strictly decreasing prices:** return `0`, not a negative number. Initializing `maxP = 0` handles this.
- **Equal prices** (`[3,3,3]`): `prices[l] < prices[r]` is false, so `l` moves forward, which is harmless since the profit would be 0 anyway.
- **Selling before buying:** the answer is not `max(prices) - min(prices)`. For `[7,1,5,3,6,4]` that happens to work, but for `[5,1,0,...]`-style cases where the max comes before the min (`[2,4,1]`), it gives 3 instead of the correct 2. Order matters.
- **Initializing `min_price` to `0`:** this is a bug in the min-tracking version. Use `float('inf')` or `prices[0]`.
- **Style note on your code:** `while(r < len(prices))` doesn't need parentheses in Python, and `list[int]` as a type hint requires Python 3.9+ (LeetCode's template uses `List[int]`). Neither affects correctness.

---

## Interview Follow-Ups

- **"What if you can do as many transactions as you like?"** Add every positive day-to-day difference (LC 122, greedy).
- **"What if you're limited to at most 2 or k transactions?"** Use DP with states for each transaction count (LC 123, LC 188).
- **"What if there's a cooldown or a transaction fee?"** Use a state machine DP (LC 309, LC 714).
- **"Can you also return the buy and sell days?"** Track the index of `l` when you update `maxP`.
- **"What if prices arrive as a stream?"** The min-tracking version works unchanged, since it only needs the running minimum and the best profit so far.

---

## Related Problems

- **122. Best Time to Buy and Sell Stock II:** unlimited transactions (greedy)
- **123. Best Time to Buy and Sell Stock III:** at most 2 transactions (DP)
- **188. Best Time to Buy and Sell Stock IV:** at most k transactions (DP)
- **309. Best Time to Buy and Sell Stock with Cooldown:** state machine DP
- **714. Best Time to Buy and Sell Stock with Transaction Fee:** state machine DP
- **53. Maximum Subarray:** Kadane's algorithm, the same idea as approach 4
- **3. Longest Substring Without Repeating Characters:** same two-pointer window style

---

Your solution is correct and optimal. Send the next problem, or ask for the C++ version of 121. When you have a few done, I can combine everything into one study document.
