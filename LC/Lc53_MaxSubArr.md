# 53. Maximum Subarray

**Difficulty:** Medium | **Topics:** Array, Divide and Conquer, Dynamic Programming

**Link:** https://leetcode.com/problems/maximum-subarray/

---

## Problem Description

Given an integer array `nums`, find the **subarray** (a contiguous, non-empty part of the array) with the largest sum, and return its sum.

**Example 1**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

**Example 2**
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

**Example 3**
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

**Constraints**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

**Follow-up:** If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

---

## Intuition and Key Insight

At each position, you decide: **extend the current subarray, or start fresh here?**

If the running sum before the current element is negative, it can only drag the new sum down, so you are better off discarding it and starting a new subarray at the current element. If it is non-negative, keeping it never hurts.

Your solution expresses this directly: reset `curSum` to 0 whenever it goes negative, then add the current number. This is **Kadane's algorithm**.

**Pattern to recognize:** "best contiguous segment" → a running value that either extends or restarts, with a separate variable tracking the best seen so far.

---

## Approaches

### 1. Brute Force: Every Subarray

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        best = float('-inf')
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]            # running sum of nums[i..j]
                best = max(best, total)
        return best
```

- **Time:** O(n²), since the inner loop reuses the running sum instead of recomputing it (the naive version that re-sums each subarray is O(n³))
- **Space:** O(1)
- **Verdict:** With n up to 10^5 that is about 5 x 10^9 steps, so it will time out. Mention it as the baseline.

### 2. Kadane's Algorithm, Reset Style (Your Solution, Optimal)

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]                  # best answer so far (non-empty, so seed with nums[0])
        curSum = 0                        # sum of the current subarray

        for n in nums:
            if curSum < 0:                # a negative prefix only hurts
                curSum = 0                # drop it and start fresh
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub
```

- **Time:** O(n), one pass
- **Space:** O(1)
- **Verdict:** Optimal and correct. Seeding `maxSub` with `nums[0]` rather than `0` is important, and it is what makes the all-negative case work.

### 3. Kadane's Algorithm, DP Style

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = best = nums[0]
        for n in nums[1:]:
            cur = max(n, cur + n)         # extend, or restart at n
            best = max(best, cur)
        return best
```

- **Time:** O(n)
- **Space:** O(1) (note that `nums[1:]` makes an O(n) copy. Use `for i in range(1, len(nums))` to keep it strictly O(1))
- **Verdict:** Same algorithm, framed as the recurrence `dp[i] = max(nums[i], dp[i-1] + nums[i])`, where `dp[i]` is the best sum of a subarray **ending at** `i`. This framing is easier to explain in an interview.

### 4. Divide and Conquer (the Follow-Up)

Split the array at the middle. The best subarray is one of three things: entirely in the left half, entirely in the right half, or **crossing the middle**.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(l: int, r: int) -> int:
            if l == r:
                return nums[l]
            mid = (l + r) // 2

            # best sum of a subarray that crosses the midpoint
            left_best, total = float('-inf'), 0
            for i in range(mid, l - 1, -1):         # extend leftward from mid
                total += nums[i]
                left_best = max(left_best, total)

            right_best, total = float('-inf'), 0
            for i in range(mid + 1, r + 1):         # extend rightward from mid + 1
                total += nums[i]
                right_best = max(right_best, total)

            cross = left_best + right_best
            return max(solve(l, mid), solve(mid + 1, r), cross)

        return solve(0, len(nums) - 1)
```

- **Time:** O(n log n), from T(n) = 2T(n/2) + O(n)
- **Space:** O(log n) for the recursion stack
- **Verdict:** Slower than Kadane's, but it is what the follow-up asks for. The version that returns (total, prefix, suffix, best) from each call gets this down to O(n), which is how segment trees answer range max-subarray queries.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n²) | O(1) | TLE on large inputs |
| **Kadane (reset style, yours)** | **O(n)** | **O(1)** | **Optimal** |
| Kadane (DP style) | **O(n)** | **O(1)** | **Optimal, easiest to explain** |
| Divide and conquer | O(n log n) | O(log n) | The follow-up |

---

## Walkthrough (Your Solution)

`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| n | curSum before | Reset? | curSum after | maxSub |
|---|---|---|---|---|
| -2 | 0 | No | -2 | -2 |
| 1 | -2 | **Yes** → 0 | 1 | 1 |
| -3 | 1 | No | -2 | 1 |
| 4 | -2 | **Yes** → 0 | 4 | 4 |
| -1 | 4 | No | 3 | 4 |
| 2 | 3 | No | 5 | 5 |
| 1 | 5 | No | 6 | **6** |
| -5 | 6 | No | 1 | 6 |
| 4 | 1 | No | 5 | 6 |

Result: `6`, from the subarray `[4, -1, 2, 1]`.

---

## Why the Reset Is Safe

If `curSum < 0`, any subarray that continues through the current position is strictly better off without that negative prefix, because dropping it raises its sum. So no optimal subarray needs to include it, and restarting never skips a better answer.

Note that the check is `< 0`, not `<= 0`. Resetting on exactly 0 would also be correct (a tie either way), but `< 0` is the standard form.

---

## Edge Cases and Pitfalls

- **All negative** (`[-3, -1, -2]`): the answer is `-1`, the largest single element, since the subarray must be non-empty. This is why `maxSub` starts at `nums[0]` and not `0`. Initializing to `0` would wrongly return `0`.
- **Single element** (`[1]` or `[-5]`): returns that element.
- **All positive:** the whole array is the answer, and `curSum` is never reset.
- **Mixed with zeros** (`[0, -1, 0]`): returns `0`.
- **Returning the subarray itself:** track a `start` index. Set `start = i` when you reset, and record `(start, i)` whenever `maxSub` improves.
- **Style note on your code:** `list[int]` needs Python 3.9+ (LeetCode's template uses `List[int]`), and the variable `n` shadows the usual meaning of "length" in interviews, so `num` is a clearer name. Neither affects correctness.

---

## Interview Follow-Ups

- **"Return the subarray, not just the sum."** Track the start index on resets, as above.
- **"What if the array is circular?"** Answer is `max(kadane_max, total - kadane_min)`, with a special case when all elements are negative (LC 918).
- **"What about maximum product instead of sum?"** Track both the running max and min, since a negative can flip them (LC 152).
- **"What if the subarray must have length at least k?"** Combine prefix sums with a running minimum prefix.
- **"Can you do it with divide and conquer?"** Yes, see approach 4. Mention that it is O(n log n), or O(n) with the combine-node trick.
- **"What about a 2D version?"** Fix a pair of rows, collapse to 1D, and run Kadane's, giving O(rows² x cols).

---

## Related Problems

- **121. Best Time to Buy and Sell Stock:** the same problem over the differences array
- **152. Maximum Product Subarray:** track max and min
- **918. Maximum Sum Circular Subarray:** Kadane's plus the total-minus-min trick
- **1749. Maximum Absolute Sum of Any Subarray:** run Kadane's for both max and min
- **325. Maximum Size Subarray Sum Equals k:** prefix sums with a hash map
- **560. Subarray Sum Equals K:** prefix sums with a hash map
- **238. Product of Array Except Self:** a related prefix/suffix pattern

---
