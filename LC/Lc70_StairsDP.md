# 70. Climbing Stairs

**Difficulty:** Easy | **Topics:** Math, Dynamic Programming, Memoization

**Link:** https://leetcode.com/problems/climbing-stairs/

---

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can climb **1 or 2 steps**. In how many **distinct ways** can you climb to the top?

**Example 1**
```
Input: n = 2
Output: 2
Explanation: 1 + 1, or 2.
```

**Example 2**
```
Input: n = 3
Output: 3
Explanation: 1 + 1 + 1, 1 + 2, or 2 + 1.
```

**Constraints**
- `1 <= n <= 45`

---

## Intuition and Key Insight

To stand on step `i`, your last move was either a 1-step from `i - 1` or a 2-step from `i - 2`. So:

```
ways(i) = ways(i - 1) + ways(i - 2)
```

with `ways(0) = 1` (one way to stay at the bottom) and `ways(1) = 1`. This is the **Fibonacci sequence**. Each value depends only on the previous two, so you never need to store the whole table.

Your solution keeps just those two values, `one` and `two`, and rolls them forward.

**Pattern to recognize:** "count the ways to reach a state where the last move came from a small fixed set of earlier states" → DP with a recurrence, then compress the space to the last few values.

---

## Approaches

### 1. Brute Force: Plain Recursion

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```

- **Time:** O(2^n), since each call branches into two and the same subproblems are recomputed
- **Space:** O(n) for the recursion stack
- **Verdict:** Correct but exponential. For n = 45 it makes billions of calls and times out. Mention it, then add memoization.

### 2. Top-Down DP (Memoization)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def dp(i: int) -> int:
            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)
```

- **Time:** O(n), since each subproblem is solved once
- **Space:** O(n) for the memo and recursion stack
- **Verdict:** Removes the repeated work and shows the DP structure. `functools.cache` does the same in one decorator.

### 3. Bottom-Up DP (Table)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

- **Time:** O(n)
- **Space:** O(n)
- **Verdict:** No recursion, and the table makes the recurrence obvious. It is the stepping stone to the constant-space version.

### 4. Two Variables (Your Solution, Optimal)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1                 # ways(i - 1) and ways(i - 2)

        for i in range(n - 1):          # n - 1 steps of rolling forward
            temp = one
            one = one + two             # ways(i) = ways(i - 1) + ways(i - 2)
            two = temp                  # old one becomes the new "two back"

        return one
```

- **Time:** O(n)
- **Space:** O(1)
- **Verdict:** Optimal for this problem and the expected final answer. It can be written more compactly as `one, two = one + two, one`.

### 5. Matrix Exponentiation / Closed Form

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def mul(A, B):
            return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                    [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

        result = [[1, 0], [0, 1]]
        base = [[1, 1], [1, 0]]
        p = n
        while p:
            if p & 1:
                result = mul(result, base)
            base = mul(base, base)
            p >>= 1
        return result[0][0]
```

- **Time:** O(log n)
- **Space:** O(1)
- **Verdict:** Faster in theory, and worth mentioning when an interviewer asks "can you beat O(n)?". For n at most 45, the linear loop is simpler and just as fast. The closed form with the golden ratio also exists, but floating-point error makes it risky for large n.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Plain recursion | O(2^n) | O(n) | TLE |
| Memoization | O(n) | O(n) | Shows the DP structure |
| Bottom-up table | O(n) | O(n) | Clear recurrence |
| **Two variables (yours)** | **O(n)** | **O(1)** | **Optimal, standard** |
| Matrix exponentiation | O(log n) | O(1) | Beats linear, rarely needed |

---

## Walkthrough (Your Solution)

`n = 5`, start with `one = 1`, `two = 1`, and the loop runs `n - 1 = 4` times.

| Iteration | temp | one (new) | two (new) | Meaning |
|---|---|---|---|---|
| start | | 1 | 1 | ways(1), ways(0) |
| 1 | 1 | 2 | 1 | ways(2), ways(1) |
| 2 | 2 | 3 | 2 | ways(3), ways(2) |
| 3 | 3 | 5 | 3 | ways(4), ways(3) |
| 4 | 5 | 8 | 5 | ways(5), ways(4) |

Return `one = 8`, so there are 8 ways to climb 5 stairs.

---

## Why It Works

At every point `one` holds `ways(i)` and `two` holds `ways(i - 1)`. The update `one = one + two` applies the recurrence, and `two = temp` shifts the old `one` into the "previous" slot. After `n - 1` updates starting from `ways(1)`, `one` is `ways(n)`.

**Why the loop runs `n - 1` times:** you start already at `ways(1)`, so reaching `ways(n)` takes `n - 1` steps.

**Why both start at 1:** `ways(0) = 1` (the empty climb) and `ways(1) = 1` (a single step).

---

## Edge Cases and Pitfalls

- **`n = 1`:** the loop runs `0` times and returns `1`. Correct.
- **`n = 2`:** the loop runs once, giving `one = 2`.
- **Off-by-one in the loop count:** `range(n)` would return `ways(n + 1)`. Check against `n = 2` (answer 2) to verify.
- **Mixing up the update order:** doing `one = one + two` then `two = one` loses the old `one`, which is why the temp variable (or tuple assignment) is needed.
- **Overflow:** none in Python. The maximum answer for `n = 45` is 1,836,311,903, which fits in a signed 32-bit int, so C++ `int` is safe here.
- **Unused loop variable:** `i` is never used, so `for _ in range(n - 1)` is the conventional form.
- **Style note:** your code is correct and clean. The tuple form `one, two = one + two, one` removes the temp variable.

---

## Interview Follow-Ups

- **"What if you can take 1, 2 or 3 steps?"** Tribonacci recurrence, `ways(i) = ways(i-1) + ways(i-2) + ways(i-3)`, keeping three values.
- **"What if you can take any step size from a set `S`?"** General DP, `dp[i] = sum(dp[i - s] for s in S if i >= s)`, which is Coin Change style counting (LC 377).
- **"What if some steps are broken?"** Set `dp[i] = 0` for broken steps (LC 1137-style variations).
- **"What if each step has a cost?"** Min Cost Climbing Stairs (LC 746), with `min` instead of `+`.
- **"Can you do better than O(n)?"** Yes, matrix exponentiation or fast doubling gives O(log n).
- **"What if n is huge and the answer is needed modulo a prime?"** Apply `% MOD` at every addition, using fast doubling.
- **"How is this related to Fibonacci?"** `ways(n) = Fib(n + 1)` with `Fib(1) = Fib(2) = 1`.

---

## Related Problems

- **746. Min Cost Climbing Stairs:** the same recurrence with costs
- **509. Fibonacci Number:** the same sequence
- **1137. N-th Tribonacci Number:** three-term recurrence
- **198. House Robber:** a two-state rolling DP
- **213. House Robber II:** circular variant
- **377. Combination Sum IV:** counting ordered ways with a set of steps
- **322. Coin Change:** minimum coins, a similar DP shape
- **62. Unique Paths:** 2D grid path counting
- **91. Decode Ways:** counting ways with a 1-or-2 character choice

---
