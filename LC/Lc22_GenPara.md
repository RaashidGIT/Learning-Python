# 22. Generate Parentheses

**Difficulty:** Medium | **Topics:** String, Dynamic Programming, Backtracking

**Link:** https://leetcode.com/problems/generate-parentheses/

---

## Problem Description

Given `n` pairs of parentheses, write a function to **generate all combinations of well-formed parentheses**.

**Example 1**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2**
```
Input: n = 1
Output: ["()"]
```

**Constraints**
- `1 <= n <= 8`

---

## Intuition and Key Insight

Build the string one character at a time, but only take choices that can still lead to a valid result. Two rules are enough to guarantee validity:

1. Add an **open** parenthesis only if `open < n` (you still have some left to place).
2. Add a **close** parenthesis only if `closed < open` (there is an unmatched open one to close).

A string is complete and valid exactly when `open == closed == n`. Because invalid prefixes are never created, there is no need to generate everything and filter afterward. This is **backtracking with pruning**, and the number of results is the n-th **Catalan number**, which is about 4^n / (n^1.5 x sqrt(pi)).

Your solution encodes exactly these rules in its comments, which is the right way to explain it in an interview.

**Pattern to recognize:** "generate all valid sequences under constraints" → backtracking where the constraints prune choices before they are made.

---

## Approaches

### 1. Brute Force: Generate All 2^(2n) Strings, Then Filter

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def is_valid(s: str) -> bool:
            balance = 0
            for c in s:
                balance += 1 if c == "(" else -1
                if balance < 0:
                    return False
            return balance == 0

        def gen(cur: list):
            if len(cur) == 2 * n:
                s = "".join(cur)
                if is_valid(s):
                    res.append(s)
                return
            for c in "()":
                cur.append(c)
                gen(cur)
                cur.pop()

        gen([])
        return res
```

- **Time:** O(2^(2n) x n), since there are 4^n strings and each costs O(n) to validate
- **Space:** O(n) recursion depth, plus the output
- **Verdict:** Correct but wasteful, because it builds many strings that were invalid from an early prefix. Mention it as the baseline, then add pruning.

### 2. Backtracking with Pruning (Your Solution, Optimal)

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []                                  # the string being built
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:               # used all pairs, and balanced
                res.append("".join(stack))
                return

            if openN < n:                           # still have an open to place
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()                         # undo

            if closedN < openN:                     # an unmatched open exists
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()                         # undo

        backtrack(0, 0)
        return res
```

- **Time:** O(4^n / sqrt(n)), proportional to the Catalan number times the string length (each result costs O(n) to join)
- **Space:** O(n) for the recursion depth and the working stack (output excluded)
- **Verdict:** Optimal and the expected interview answer. Every branch it explores leads to at least one valid string, so no work is wasted.

### 3. Backtracking with a String Parameter (No Undo Needed)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur: str, openN: int, closedN: int):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if openN < n:
                backtrack(cur + "(", openN + 1, closedN)
            if closedN < openN:
                backtrack(cur + ")", openN, closedN + 1)

        backtrack("", 0, 0)
        return res
```

- **Time:** O(4^n / sqrt(n)) times string-building cost, so O(n x Catalan(n)) overall
- **Space:** O(n) per frame for the new strings, so O(n²) across the recursion path
- **Verdict:** Shorter, since strings are immutable and each call passes a fresh one, so no `pop` is required. It is slightly less efficient because of the string copies, which doesn't matter at n up to 8.

### 4. Dynamic Programming (Closure Number)

Every valid string of length 2n can be written uniquely as `"(" + A + ")" + B`, where `A` is a valid string with `i` pairs and `B` is a valid string with `n - 1 - i` pairs.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        for k in range(1, n + 1):
            for i in range(k):
                for left in dp[i]:
                    for right in dp[k - 1 - i]:
                        dp[k].append("(" + left + ")" + right)
        return dp[n]
```

- **Time:** O(n x Catalan(n)) (the sum of the products of the Catalan numbers, with string building)
- **Space:** O(n x Catalan(n)) to store all the lists
- **Verdict:** An elegant decomposition that mirrors the Catalan recurrence. It uses more memory than backtracking, so it is a good "show you know another way" answer.

---

## Complexity Summary

| Approach | Time | Space (extra) | Notes |
|---|---|---|---|
| Generate all, then filter | O(4^n x n) | O(n) | Wasteful baseline |
| **Backtracking with pruning (yours)** | **O(4^n / sqrt(n))** | **O(n)** | **Optimal, standard answer** |
| Backtracking, string parameter | same order | O(n²) | Shorter, no undo |
| DP (closure number) | same order | O(n x Catalan(n)) | Mirrors the Catalan recurrence |

*The output size is Catalan(n), about 4^n / (n^1.5 x sqrt(pi)). Every approach has to produce all of it.*

---

## Walkthrough (Your Solution)

`n = 2`. The decision tree, where `(o, c)` is the count of open and closed parentheses so far:

```
                           "" (0,0)
                              |  only "(" allowed
                          "(" (1,0)
                 "(" ok /           \ ")" ok (c < o)
              "((" (2,0)              "()" (1,1)
                  |  only ")"            |  only "(" (c == o blocks ")")
             "(()" (2,1)              "()(" (2,1)
                  |                      |
            "(())" (2,2) ✓          "()()" (2,2) ✓
```

Result: `["(())", "()()"]`.

Trace of the first branch:

| Call | stack | openN | closedN | Action |
|---|---|---|---|---|
| backtrack(0,0) | `` | 0 | 0 | open < 2, push `(` |
| backtrack(1,0) | `(` | 1 | 0 | open < 2, push `(` |
| backtrack(2,0) | `((` | 2 | 0 | open == n, skip open. closed < open, push `)` |
| backtrack(2,1) | `(()` | 2 | 1 | push `)` |
| backtrack(2,2) | `(())` | 2 | 2 | **record** `(())` |

---

## Why It Works

**Validity:** a string of parentheses is balanced exactly when every prefix has at least as many `(` as `)` and the totals are equal. Rule 2 (`closed < open`) ensures every prefix satisfies the first condition. Rule 1 (`open < n`) and the final check `open == closed == n` ensure the totals are right.

**Completeness:** every valid string is reachable, because at each position the next character it needs is one of the allowed choices (a valid string never needs a disallowed character). So every valid string is a root-to-leaf path in the pruned tree.

**No duplicates:** each path is a distinct sequence of characters, so each leaf is a distinct string.

**Why `closedN < openN` is enough:** you never need an explicit check that `closedN < n`, because `closedN < openN <= n` already implies it.

---

## Edge Cases and Pitfalls

- **`n = 1`:** returns `["()"]`.
- **Forgetting `pop()`:** the choice leaks into the next branch and the strings come out wrong or too long.
- **Using `closedN <= openN`:** this allows `)` when there is nothing to close, producing invalid strings like `")("`.
- **Using `closedN < n` instead of `closedN < openN`:** also allows invalid prefixes such as `")"`.
- **Appending `stack` instead of `"".join(stack)`:** the result would store references to a list that keeps changing.
- **Base-case condition:** `openN == closedN == n` is a Python chained comparison and is correct. In other languages, write `openN == n && closedN == n`.
- **Order of output:** any order is accepted. This solution returns them in lexicographic order, with `(` before `)`.
- **Style note:** your code is correct and the comments are excellent (the three rules at the top are exactly what to say out loud in an interview). `paranthesis` should be `parenthesis`, `stack` is really a character buffer so `path` is a common name, and `list[str]` needs Python 3.9+ (LeetCode's template uses `List[str]`).

---

## Interview Follow-Ups

- **"How many results are there?"** The n-th Catalan number: 1, 2, 5, 14, 42, 132, 429, 1430 for n = 1 to 8.
- **"Why is the time complexity not simply O(2^(2n))?"** Pruning removes every invalid prefix, so the work is proportional to the number of valid strings (Catalan), which is about 4^n / n^1.5.
- **"Can you do it iteratively?"** Yes, use an explicit stack or queue of `(string, open, closed)` states (BFS or DFS).
- **"What if there are several bracket types, such as (), [] and {}?"** Track the last unmatched opener with a stack and allow only the matching closer (a generalization of LC 20).
- **"Count the valid strings without generating them?"** Use the Catalan formula `C(2n, n) / (n + 1)` or the DP recurrence, in O(n) or O(n²).
- **"Check whether a given string is valid?"** Valid Parentheses, LC 20, using a counter or stack.
- **"What if n is large?"** The output is exponential, so generate lazily with a generator.

---

## Related Problems

- **20. Valid Parentheses:** validate a given string with a stack
- **32. Longest Valid Parentheses:** DP or stack
- **301. Remove Invalid Parentheses:** BFS or backtracking to fix a string
- **241. Different Ways to Add Parentheses:** divide and conquer over split points
- **96. Unique Binary Search Trees:** the same Catalan recurrence
- **17. Letter Combinations of a Phone Number:** decision tree over digits
- **78. Subsets:** include/exclude backtracking
- **46. Permutations:** backtracking over orderings
- **39. Combination Sum:** backtracking with a pruning condition

---
