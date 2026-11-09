# 560. Subarray Sum Equals K

**Difficulty:** Medium | **Topics:** Array, Hash Table, Prefix Sum

**Link:** https://leetcode.com/problems/subarray-sum-equals-k/

---

## Problem Description

Given an array of integers `nums` and an integer `k`, return the **total number of subarrays** whose sum equals `k`.

A subarray is a contiguous, **non-empty** sequence of elements within the array.

**Example 1**
```
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: The subarrays [1,1] at indices 0..1 and 1..2 both sum to 2.
```

**Example 2**
```
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [3] both sum to 3.
```

**Constraints**
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

---

## Intuition and Key Insight

Let `prefix[i]` be the sum of the first `i` elements. The sum of the subarray `nums[j..i-1]` is `prefix[i] - prefix[j]`. We want that to equal `k`, which means:

```
prefix[j] = prefix[i] - k
```

So as you scan, for the current running sum `curSum`, you ask: **how many earlier prefix sums equal `curSum - k`?** Each one marks the start of a subarray ending here with sum `k`. A hash map of `prefix sum -> count of times seen` answers that in O(1).

This is the Two Sum idea applied to prefix sums, and it is why the approach works with **negative numbers**, where a sliding window fails (the window can't decide when to shrink).

**Pattern to recognize:** "count or find subarrays with a given sum" → prefix sums plus a hash map of counts.

---

## Approaches

### 1. Brute Force: Every Subarray

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]            # running sum of nums[i..j]
                if total == k:
                    res += 1
        return res
```

- **Time:** O(n²) (the naive version that re-sums each subarray is O(n³))
- **Space:** O(1)
- **Verdict:** With n up to 2 x 10^4 that is about 2 x 10^8 steps, which often passes but is the baseline to beat.

### 2. Prefix Sum Array + Pair Check

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if prefix[j] - prefix[i] == k:
                    res += 1
        return res
```

- **Time:** O(n²)
- **Space:** O(n)
- **Verdict:** Not an improvement over brute force, but it is the stepping stone to the hash map version. It makes the `prefix[j] - prefix[i] = k` relation explicit.

### 3. Prefix Sum + Hash Map, One Pass (Your Solution, Optimal)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0: 1}                         # empty prefix: sum 0 seen once

        for n in nums:
            curSum += n
            diff = curSum - k                       # needed earlier prefix sum

            res += prefixSums.get(diff, 0)          # subarrays ending here that sum to k
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)   # record AFTER querying

        return res
```

- **Time:** O(n), one pass with O(1) average lookups
- **Space:** O(n), since the map holds up to n + 1 distinct prefix sums
- **Verdict:** Optimal and the expected interview answer.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n²) | O(1) | Baseline |
| Prefix array + pairs | O(n²) | O(n) | Stepping stone |
| **Prefix sum + hash map (yours)** | **O(n)** | **O(n)** | **Optimal, handles negatives** |

---

## Walkthrough (Your Solution)

`nums = [1, 2, 3]`, `k = 3`

| n | curSum | diff = curSum - k | `prefixSums` lookup | res | `prefixSums` after |
|---|---|---|---|---|---|
| (start) | 0 | | | 0 | {0: 1} |
| 1 | 1 | -2 | 0 | 0 | {0: 1, 1: 1} |
| 2 | 3 | 0 | 1 (the empty prefix) | 1 | {0: 1, 1: 1, 3: 1} |
| 3 | 6 | 3 | 1 | 2 | {0: 1, 1: 1, 3: 1, 6: 1} |

Result: `2`, for the subarrays `[1,2]` and `[3]`.

---

## Why It Works

Every subarray ending at the current index corresponds to exactly one earlier prefix (including the empty prefix). It sums to `k` precisely when that earlier prefix equals `curSum - k`. Counting how many earlier prefixes have that value counts every valid subarray ending here, and summing over all end positions counts each subarray exactly once.

**Why `{0: 1}` at the start:** it represents the empty prefix. Without it, subarrays that start at index 0 (like `[1,2]` above, where `curSum == k`) would be missed.

**Why record after querying:** the current prefix must not match itself. If `k = 0`, recording first would count an empty subarray at every position.

---

## Edge Cases and Pitfalls

- **Negative numbers:** the main reason a sliding window fails here. A window can't know whether extending or shrinking will help, but prefix sums handle it naturally.
- **Zeros and `k = 0`** (`[0,0,0]`, `k = 0`): the answer is 6, since every non-empty subarray sums to 0. The map counts (not just presence) are what make this work.
- **Forgetting `{0: 1}`:** misses every subarray that starts at index 0.
- **Using a set instead of counts:** undercounts when the same prefix sum occurs multiple times, as it does with zeros or cancelling values.
- **Updating the map before the lookup:** counts empty subarrays when `k = 0`.
- **Single element** (`[1]`, `k = 1`): answer is 1. `[1]`, `k = 2`: answer is 0.
- **Answer is a count, not the subarrays themselves.** Returning them would need the map to store index lists.
- **Style note:** your code is correct and clean. The loop variable `n` suggests "length" to most readers, so `num` is a clearer name. Also, `List[int]` needs `from typing import List` outside LeetCode.

---

## Interview Follow-Ups

- **"Why doesn't a sliding window work?"** Negative numbers break its monotonicity. Sliding window only works when all elements are non-negative (compare LC 209).
- **"What if all numbers are positive?"** A sliding window gives O(n) time and O(1) space.
- **"Return the longest subarray with sum k."** Store the **first index** of each prefix sum instead of a count (LC 325).
- **"Return the subarrays themselves."** Store a list of indices per prefix sum, though the output itself can be O(n²).
- **"What about subarray sum divisible by k?"** Track prefix sums modulo k, handling negative remainders (LC 974).
- **"Binary arrays, equal 0s and 1s?"** Map 0 to -1 and look for sum 0 (LC 525).
- **"What if the data is a stream?"** The one-pass version works unchanged, using O(distinct prefix sums) memory.

---

## Related Problems

- **1. Two Sum:** the same "look up the complement" idea
- **325. Maximum Size Subarray Sum Equals k:** hash map of first indices
- **523. Continuous Subarray Sum:** prefix sums modulo k
- **525. Contiguous Array:** prefix sums with a 0/1 to -1/+1 mapping
- **974. Subarray Sums Divisible by K:** prefix remainders with counts
- **209. Minimum Size Subarray Sum:** sliding window, positives only
- **53. Maximum Subarray:** Kadane's, a different running-value pattern
- **930. Binary Subarrays With Sum:** prefix sums or sliding window
- **437. Path Sum III:** the same technique on a tree path

---
