# 435. Non-overlapping Intervals

**Difficulty:** Medium | **Topics:** Array, Dynamic Programming, Greedy, Sorting

**Link:** https://leetcode.com/problems/non-overlapping-intervals/

---

## Problem Description

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the **minimum number of intervals you need to remove** so that the rest of the intervals are non-overlapping.

Intervals that only touch at an endpoint, like `[1,2]` and `[2,3]`, are **not** overlapping.

**Example 1**
```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: Remove [1,3] and the rest are non-overlapping.
```

**Example 2**
```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest non-overlapping.
```

**Example 3**
```
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: Already non-overlapping.
```

**Constraints**
- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

---

## Intuition and Key Insight

Removing the minimum number of intervals is the same as **keeping the maximum number of non-overlapping intervals**:

```
answer = n - (max number of intervals you can keep)
```

This is the classic **activity selection** problem. Whenever two intervals overlap, one of them must go. The right one to drop is the one that **ends later**, because an interval that stretches further right blocks more of the future and can never help more than the one that ends sooner.

Your solution sorts by start. When it sees an overlap, it removes the interval with the larger end by keeping `min(end, prevEnd)` as the running end. Sorting by end is an alternative that makes the greedy choice even simpler (approach 4).

**Pattern to recognize:** "minimum removals to avoid conflicts" or "maximum number of non-conflicting intervals" → sort, then greedily keep the interval that ends earliest.

---

## Approaches

### 1. Brute Force: Recursion (Include or Exclude)

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)

        def dfs(i: int, prev_end: int) -> int:
            # returns the max number of intervals we can keep from index i onward
            if i == n:
                return 0
            skip = dfs(i + 1, prev_end)
            take = 0
            if intervals[i][0] >= prev_end:
                take = 1 + dfs(i + 1, intervals[i][1])
            return max(skip, take)

        return n - dfs(0, float('-inf'))
```

- **Time:** O(2^n)
- **Space:** O(n) for the recursion stack
- **Verdict:** Shows the include/exclude structure but is far too slow for n up to 10^5. Mention it as the baseline.

### 2. DP (Longest Chain Ending at Each Interval)

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        dp = [1] * n                                # dp[i] = max kept, with interval i as the last one
        for i in range(n):
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)
```

- **Time:** O(n²)
- **Space:** O(n)
- **Verdict:** This is the Longest Increasing Subsequence pattern, with "does not overlap" as the compatibility test. It times out at n = 10^5, but it is a good stepping stone and the base for the weighted version (LC 1235).

### 3. Greedy, Sort by Start (Your Solution, Optimal)

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()                            # sort by start (ties by end)

        res = 0                                     # intervals removed
        prevEnd = intervals[0][1]                   # end of the last interval we kept
        for start, end in intervals[1:]:
            if start >= prevEnd:                    # no overlap (touching is fine)
                prevEnd = end
            else:                                   # overlap: remove one interval
                res += 1
                prevEnd = min(end, prevEnd)         # keep the one that ends sooner
        return res
```

- **Time:** O(n log n), dominated by the sort, with a single O(n) pass after it
- **Space:** O(n) in practice, because `intervals[1:]` makes a copy and Timsort needs auxiliary space. Iterating by index would avoid the slice copy.
- **Verdict:** Optimal and correct. The key line is `prevEnd = min(end, prevEnd)`, which is where the removal decision is made.

### 4. Greedy, Sort by End (Classic Activity Selection)

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])          # sort by end
        res = 0
        prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end:                   # compatible: keep it
                prev_end = end
            else:                                   # overlaps the kept one: remove this one
                res += 1
        return res
```

- **Time:** O(n log n)
- **Space:** O(n) for the sort
- **Verdict:** Equally optimal, and the easiest to prove. Because intervals are processed in order of end time, the interval we already kept always ends no later than the current one, so on a conflict you can always just drop the current one, with no `min` needed. This is the form most editorials use.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Recursion | O(2^n) | O(n) | TLE |
| DP (LIS style) | O(n²) | O(n) | TLE, base for weighted version |
| **Greedy, sort by start (yours)** | **O(n log n)** | **O(n)** | **Optimal, remove the later-ending one** |
| **Greedy, sort by end** | **O(n log n)** | **O(n)** | **Optimal, simplest to prove** |

---

## Walkthrough (Your Solution)

`intervals = [[1,2],[2,3],[3,4],[1,3]]` → sorted: `[[1,2],[1,3],[2,3],[3,4]]`

Start with `prevEnd = 2` (from `[1,2]`), `res = 0`.

| interval | start >= prevEnd? | Action | prevEnd | res |
|---|---|---|---|---|
| [1,3] | 1 >= 2? **No** | overlap, `res += 1`, `prevEnd = min(3, 2)` | 2 | 1 |
| [2,3] | 2 >= 2? Yes | keep, `prevEnd = 3` | 3 | 1 |
| [3,4] | 3 >= 3? Yes | keep, `prevEnd = 4` | 4 | 1 |

Result: `1`.

Duplicate case, `[[1,2],[1,2],[1,2]]`: the first is kept, and each of the other two overlaps it (1 < 2), so `res = 2`.

---

## Why It Works

When two intervals overlap, at least one has to be removed, and it is always safe to remove the one with the **larger end**. Any set of future intervals that is compatible with the larger-end interval is also compatible with the smaller-end one, because the smaller-end one frees up the timeline sooner. So keeping the smaller end never excludes a better solution (an exchange argument).

In your code, `prevEnd = min(end, prevEnd)` does exactly this. It does not track which interval was removed, only the end of the interval that survives.

Why sorting by start is enough: with intervals sorted by start, the current interval's start is at least every earlier start. If it overlaps the last kept interval, it overlaps because `start < prevEnd`, and the only decision left is which of the two ends to keep.

---

## Edge Cases and Pitfalls

- **Touching intervals** (`[1,2]`, `[2,3]`): not overlapping, so the check must be `start >= prevEnd`. Using `>` would wrongly count them as overlaps.
- **Identical intervals** (`[[1,2],[1,2]]`): the second overlaps the first, so one is removed.
- **One interval:** the answer is `0`. Your code handles it because the loop over `intervals[1:]` is empty.
- **Empty input:** the constraints guarantee at least one interval, so `intervals[0]` is safe. Without that guarantee, add `if not intervals: return 0`.
- **One interval nested inside another** (`[[1,10],[2,3],[4,5]]`): the greedy removes `[1,10]` by keeping the min end, giving `1`. Keeping `[1,10]` would force removing two.
- **Not updating `prevEnd` on overlap:** if you forget `min`, a long interval stays as the barrier and you remove too many (`[[1,10],[2,3],[4,5]]` would return 2).
- **Sorting by end vs by start:** both work, but with sort-by-end you must **not** use `min` logic, and with sort-by-start you must. Mixing the two causes wrong answers.
- **Counting what is kept instead of removed:** `answer = n - kept`. Be careful with off-by-one on the first interval.
- **Input is mutated** by `sort()`. Copy first if you need the original order.
- **Style note:** `list[list[int]]` needs Python 3.9+ (LeetCode's template uses `List[List[int]]`). The empty code cell above your solution can be deleted.

---

## Interview Follow-Ups

- **"Why is it safe to remove the interval that ends later?"** Give the exchange argument above.
- **"Return the intervals that were removed, not just the count."** Track the interval objects instead of only `prevEnd`, and append the one with the larger end on each overlap.
- **"What if intervals have weights and you want maximum total weight kept?"** Greedy fails, so use DP sorted by end with binary search to find the last compatible interval, O(n log n) (LC 1235).
- **"What if touching intervals count as overlapping?"** Change `>=` to `>`.
- **"What's the minimum number of meeting rooms needed?"** A different question, solved with a min-heap or a sweep line (LC 253).
- **"Minimum arrows to burst balloons?"** It is the same greedy, sorting by end and counting groups (LC 452).
- **"Can you do better than O(n log n)?"** Not in general, since sorting is required. If coordinates are bounded (here within 10^5 range), a counting-based approach can reach O(n + range).

---

## Related Problems

- **452. Minimum Number of Arrows to Burst Balloons:** the same greedy, sort by end
- **646. Maximum Length of Pair Chain:** the same activity selection
- **56. Merge Intervals:** sort by start and merge
- **57. Insert Interval:** interval insertion and merging
- **252. Meeting Rooms:** detect any overlap
- **253. Meeting Rooms II:** minimum rooms, heap or sweep line
- **1235. Maximum Profit in Job Scheduling:** the weighted version (DP + binary search)
- **1353. Maximum Number of Events That Can Be Attended:** greedy with a heap
- **300. Longest Increasing Subsequence:** the DP pattern behind approach 2

---
