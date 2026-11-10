# 55. Jump Game

**Difficulty:** Medium | **Topics:** Array, Dynamic Programming, Greedy

**Link:** https://leetcode.com/problems/jump-game/

---

## Problem Description

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element represents your **maximum jump length** at that position.

Return `true` if you can reach the last index, or `false` otherwise.

**Example 1**
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2**
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index.
```

**Constraints**
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

---

## Intuition and Key Insight

Work **backwards**. The last index is the goal. An index `i` can reach the goal if `i + nums[i] >= goal`. If it can, then `i` itself becomes the new goal, because reaching `i` is now good enough. Repeat for every index moving left. At the end, if the goal has moved all the way to index 0, the start can reach the end.

The forward view is equivalent: track the **farthest index reachable** so far, and fail if you ever stand at an index beyond it.

**Pattern to recognize:** "can I reach the end / is a path possible" with flexible step sizes → greedy, tracking a single frontier (farthest reach or earliest good position) instead of exploring all paths.

---

## Approaches

### 1. Brute Force: Recursion (Try Every Jump)

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(i: int) -> bool:
            if i >= n - 1:
                return True
            for step in range(1, nums[i] + 1):
                if dfs(i + step):
                    return True
            return False

        return dfs(0)
```

- **Time:** O(2^n) in the worst case, since there are exponentially many jump sequences
- **Space:** O(n) for the recursion stack
- **Verdict:** Correct but far too slow. Mention it to show the search space, then add memoization.

### 2. Top-Down DP (Memoization)

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}                                   # index -> can reach end from here

        def dfs(i: int) -> bool:
            if i >= n - 1:
                return True
            if i in memo:
                return memo[i]
            for step in range(1, nums[i] + 1):
                if dfs(i + step):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)
```

- **Time:** O(n²), since each index is solved once and tries up to n jumps
- **Space:** O(n) for the memo and recursion stack
- **Verdict:** Fixes the exponential blowup and shows the DP structure. Recursion depth can reach 10^4, so it risks hitting Python's recursion limit.

### 3. Bottom-Up DP

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        good = [False] * n
        good[n - 1] = True                          # last index trivially reaches itself

        for i in range(n - 2, -1, -1):
            furthest = min(i + nums[i], n - 1)
            for j in range(i + 1, furthest + 1):
                if good[j]:
                    good[i] = True
                    break
        return good[0]
```

- **Time:** O(n²)
- **Space:** O(n)
- **Verdict:** Same idea as memoization without recursion. It is the stepping stone to the greedy insight that you only need to remember the **leftmost good index**.

### 4. Greedy, Move the Goal Backwards (Your Solution, Optimal)

```python
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1                        # index we must reach

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:                 # i can reach the current goal
                goal = i                            # so i is the new goal

        return True if goal == 0 else False
```

- **Time:** O(n), one pass
- **Space:** O(1)
- **Verdict:** Optimal. The final line can be shortened to `return goal == 0`.

### 5. Greedy, Track Farthest Reach (Forward)

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:                        # stranded: cannot even reach index i
                return False
            farthest = max(farthest, i + jump)
            if farthest >= len(nums) - 1:           # early exit
                return True
        return True
```

- **Time:** O(n)
- **Space:** O(1)
- **Verdict:** Equally optimal, and many people find it the more intuitive framing. It can exit early, unlike the backward version.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Recursion | O(2^n) | O(n) | TLE |
| Top-down DP | O(n²) | O(n) | Recursion depth risk |
| Bottom-up DP | O(n²) | O(n) | Stepping stone to greedy |
| **Greedy, goal moves back (yours)** | **O(n)** | **O(1)** | **Optimal** |
| **Greedy, farthest reach** | **O(n)** | **O(1)** | **Optimal, early exit** |

---

## Walkthrough (Your Solution)

`nums = [2, 3, 1, 1, 4]`, starting with `goal = 4`

| i | nums[i] | i + nums[i] | >= goal? | goal after |
|---|---|---|---|---|
| 4 | 4 | 8 | Yes | 4 |
| 3 | 1 | 4 | Yes | 3 |
| 2 | 1 | 3 | Yes | 2 |
| 1 | 3 | 4 | Yes (4 >= 2) | 1 |
| 0 | 2 | 2 | Yes (2 >= 1) | **0** |

`goal == 0`, so the answer is `True`.

Failing case, `nums = [3, 2, 1, 0, 4]`, starting with `goal = 4`

| i | nums[i] | i + nums[i] | >= goal? | goal after |
|---|---|---|---|---|
| 4 | 4 | 8 | Yes | 4 |
| 3 | 0 | 3 | No | 4 |
| 2 | 1 | 3 | No | 4 |
| 1 | 2 | 3 | No | 4 |
| 0 | 3 | 3 | No | 4 |

`goal == 4`, not 0, so the answer is `False`.

---

## Why It Works

At each step, `goal` is the **leftmost index known to reach the end**. For an index `i` to be good, it only needs to reach *some* good index, and the leftmost good index is the easiest target, since any jump that lands at or beyond it passes through the good region. Because a jump of length `nums[i]` can land on **any** index from `i + 1` to `i + nums[i]`, reaching at least `goal` means you can land exactly on `goal`.

So checking `i + nums[i] >= goal` is both necessary and sufficient, and moving `goal` left as soon as it succeeds never loses information.

---

## Edge Cases and Pitfalls

- **Single element** (`[0]`): you are already at the last index, so the answer is `True`. Here `goal = 0` from the start, and the loop leaves it at 0.
- **Zero at the start with length > 1** (`[0, 1]`): `False`, because you can't move.
- **A zero in the middle isn't always fatal** (`[2, 0, 0]`): you can jump over it, so the answer is `True`.
- **A zero that you can't jump over** (`[3, 2, 1, 0, 4]`): `False`. The sum of the reachable positions stalls at index 3.
- **Large jumps:** `i + nums[i]` can exceed the array length, and the `>=` comparison handles it. No clamping is needed.
- **`>=` not `==`:** you do not need to land exactly on the goal, because you can always choose a shorter jump.
- **Looping direction in the backward version:** it must go right to left, since each decision depends on the goal found to its right.
- **Style note:** `return True if goal == 0 else False` works, but `return goal == 0` is the idiomatic form. `list[int]` needs Python 3.9+ (LeetCode's template uses `List[int]`).

---

## Interview Follow-Ups

- **"What's the minimum number of jumps?"** That is LC 45 (Jump Game II), solved with a greedy BFS over reachable ranges in O(n).
- **"Return the path, not just true or false."** Use the forward version and store, for each index, the index that first reached it, or do DP with parent pointers.
- **"What if you can also jump backwards?"** The problem becomes graph reachability, so use BFS or DFS (LC 1306, LC 1345).
- **"What if each jump must be exactly nums[i]?"** Then it is a graph traversal from index 0, with visited tracking (LC 1306 style).
- **"Why is greedy correct here but not for other path problems?"** Because reachability is monotone: if you can reach index `x`, you can reach every index before `x` that is also within range, so only the frontier matters.
- **"Can you do better than O(n)?"** No, since every element can affect the answer.

---

## Related Problems

- **45. Jump Game II:** minimum number of jumps, greedy
- **1306. Jump Game III:** reachability with jumps in both directions (BFS/DFS)
- **1345. Jump Game IV:** BFS over a graph with value-based edges
- **1340. Jump Game V:** DP with bounded jumps
- **1696. Jump Game VI:** DP with a sliding window maximum
- **134. Gas Station:** another greedy on a circular reachability idea
- **763. Partition Labels:** greedy with a running frontier
- **55 vs 53:** both are single-pass greedy running-value problems, like 53. Maximum Subarray

---
