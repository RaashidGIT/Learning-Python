# 78. Subsets

**Difficulty:** Medium | **Topics:** Array, Backtracking, Bit Manipulation

**Link:** https://leetcode.com/problems/subsets/

---

## Problem Description

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set must **not contain duplicate subsets**. You can return the solution in **any order**.

**Example 1**
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2**
```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints**
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

---

## Intuition and Key Insight

Every element has exactly two choices: it is **in** the subset or it is **out**. With n elements that gives 2^n subsets, and the problem is just enumerating every combination of those choices.

This maps directly to a **decision tree**. At depth `i` you decide about `nums[i]`, branching into "include" and "exclude". Each leaf (depth n) is one complete subset. Your solution does this with backtracking: add the element, recurse, then undo the add (`pop`) and recurse on the other branch.

**Pattern to recognize:** "generate all combinations / subsets / permutations" → backtracking over a decision tree, with a shared path that you extend and then undo.

---

## Approaches

### 1. Backtracking, Include/Exclude Decision Tree (Your Solution)

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())       # copy, because subset keeps changing
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()                        # undo the choice (backtrack)
            dfs(i + 1)

        dfs(0)
        return res
```

- **Time:** O(n x 2^n), since there are 2^n leaves and each copies a subset of up to n elements
- **Space:** O(n) for the recursion depth and the working subset (the output, which is O(n x 2^n), is excluded)
- **Verdict:** Optimal in the sense that the output size itself is O(n x 2^n), so no algorithm can beat this. It is the cleanest version to explain in an interview.

### 2. Backtracking, For-Loop Version (Choose the Next Element)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(start):
            res.append(subset.copy())           # every node of the tree is a valid subset
            for j in range(start, len(nums)):
                subset.append(nums[j])
                dfs(j + 1)                      # only look at later elements, so no repeats
                subset.pop()

        dfs(0)
        return res
```

- **Time:** O(n x 2^n)
- **Space:** O(n) recursion depth
- **Verdict:** Same complexity. Every node of the recursion is recorded as an answer, not just the leaves, so the tree is smaller. This is the template reused in Combinations, Combination Sum and Subsets II.

### 3. Iterative (Build Up by Doubling)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]   # each existing subset, with and without num
        return res
```

- **Time:** O(n x 2^n)
- **Space:** O(n x 2^n) for the output, with no recursion stack
- **Verdict:** The shortest version. For each new element, the existing subsets are doubled by adding a copy that includes it. Good when you want to avoid recursion.

### 4. Bitmask

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for mask in range(1 << n):                      # 0 .. 2^n - 1
            subset = []
            for j in range(n):
                if mask & (1 << j):                     # bit j set means nums[j] is included
                    subset.append(nums[j])
            res.append(subset)
        return res
```

- **Time:** O(n x 2^n)
- **Space:** O(1) extra (output excluded)
- **Verdict:** Each integer from 0 to 2^n - 1 is a binary string choosing which elements to include. Neat and iterative, and it works because n is at most 10 (n must fit in the integer width, at most about 30 to 60 bits in practice).

---

## Complexity Summary

| Approach | Time | Space (extra) | Notes |
|---|---|---|---|
| **Backtracking, include/exclude (yours)** | **O(n x 2^n)** | **O(n)** | **Clearest decision tree** |
| Backtracking, for-loop | O(n x 2^n) | O(n) | Reusable template |
| Iterative doubling | O(n x 2^n) | O(1) | Shortest code |
| Bitmask | O(n x 2^n) | O(1) | Iterative, needs small n |

*All are optimal, because the output itself has size Θ(n x 2^n).*

---

## Walkthrough (Your Solution)

`nums = [1, 2, 3]`

The decision tree, where each level decides about one element (include on the left, exclude on the right):

```
                          []
               include 1 /    \ exclude 1
                    [1]          []
              inc 2 /  \ exc 2   inc 2 /  \ exc 2
               [1,2]    [1]    [2]       []
              /   \    /   \   /   \    /   \
         [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3]  []
```

The leaves, read left to right, are the recorded subsets:

`[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []`

That is 8 subsets, which equals 2^3.

Trace of the first few calls:

| Call | subset before | Action | subset after |
|---|---|---|---|
| dfs(0) | [] | include 1 | [1] |
| dfs(1) | [1] | include 2 | [1,2] |
| dfs(2) | [1,2] | include 3 | [1,2,3] |
| dfs(3) | [1,2,3] | `i >= len`, **record** `[1,2,3]` | |
| back in dfs(2) | [1,2,3] | `pop`, subset = [1,2] | [1,2] |
| dfs(3) | [1,2] | **record** `[1,2]` | |

---

## Why It Works

Each root-to-leaf path in the tree is a unique sequence of include/exclude decisions, so each of the 2^n leaves is a distinct subset, and no subset is missed. There are no duplicates because the elements are unique and every decision is made exactly once in a fixed order.

**Backtracking** is what lets one shared list represent every path. After exploring the "include" branch, `pop()` restores `subset` to its state before that choice, so the "exclude" branch starts from the correct path.

**Why `.copy()`:** `subset` is a single list reused for every path. Appending `subset` itself would store a reference, and by the end every entry in `res` would point to the same (empty) list.

---

## Edge Cases and Pitfalls

- **Forgetting the copy:** `res.append(subset)` instead of `res.append(subset.copy())` (or `subset[:]`, `list(subset)`) gives a result full of empty lists. This is the most common backtracking bug.
- **Forgetting to `pop`:** the include choice leaks into the exclude branch, and every subset after the first is wrong.
- **Empty subset:** it must be in the answer. The include/exclude version produces it as the all-exclude leaf, and the other versions add it explicitly.
- **Single element** (`[0]`): returns `[[], [0]]`.
- **Order of output:** any order is accepted, and different approaches produce different orders.
- **Unique elements only:** this problem guarantees it. With duplicates you need LC 90 and a sorted array with a skip rule.
- **Base case condition:** `i >= len(nums)` works, and `i == len(nums)` is equivalent here because `i` only increases by 1.
- **Time claim:** the O(n x 2^n) in your comment is correct. It is 2^n subsets, each costing up to O(n) to copy.
- **Style note:** your solution is correct and clean. `subset` and `res` are clear names, and `list[int]` needs Python 3.9+ (LeetCode's template uses `List[int]`). The `dfs` helper has no type hint, which is fine, though `dfs(i: int) -> None` is more explicit in an interview.

---

## Interview Follow-Ups

- **"What if the array has duplicates?"** Sort it, and in the for-loop version skip `nums[j]` when `j > start and nums[j] == nums[j - 1]` (LC 90).
- **"Can you do it without recursion?"** Yes, use the iterative doubling or bitmask versions.
- **"Only subsets of size k?"** That is Combinations (LC 77). Stop recording unless `len(subset) == k`, and prune when there are not enough elements left.
- **"Subsets that sum to a target?"** Combination Sum style (LC 39, 40, 216), with pruning when the sum exceeds the target.
- **"What's the space complexity?"** O(n) extra for recursion, and O(n x 2^n) including the output. State both.
- **"Can you do better than O(n x 2^n)?"** No, because the output itself contains n x 2^(n-1) elements in total.
- **"What if n is large?"** The answer is exponential, so you would generate subsets lazily with a generator instead of returning them all.

---

## Related Problems

- **90. Subsets II:** the same problem with duplicates
- **77. Combinations:** subsets of fixed size k
- **46. Permutations:** backtracking over orderings
- **47. Permutations II:** permutations with duplicates
- **39. Combination Sum:** backtracking with a target
- **40. Combination Sum II:** with duplicates and single use
- **17. Letter Combinations of a Phone Number:** decision tree over digits
- **131. Palindrome Partitioning:** backtracking over cut positions
- **79. Word Search:** backtracking on a grid

---
