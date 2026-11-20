# 46. Permutations

**Difficulty:** Medium | **Topics:** Array, Backtracking

**Link:** https://leetcode.com/problems/permutations/

---

## Problem Description

Given an array `nums` of **distinct** integers, return all the possible permutations. You can return the answer in **any order**.

**Example 1**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2**
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3**
```
Input: nums = [1]
Output: [[1]]
```

**Constraints**
- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

---

## Intuition and Key Insight

A permutation is an ordering, so at each position you choose **one of the elements not yet used**. That gives n choices for the first slot, n - 1 for the second, and so on, for n! permutations in total.

Your solution uses a **recursive build-up** idea: pick one element `n` out of the array, get all permutations of the remaining elements, then attach `n` to each of them. Doing this for every choice of `n` covers every permutation exactly once.

The standard backtracking alternative keeps a shared path and a "used" marker, and is the template reused in most backtracking problems.

**Pattern to recognize:** "generate all orderings / arrangements" → backtracking where each level picks one unused element.

---

## Approaches

### 1. Recursive Build-Up: Pop, Recurse, Append (Your Solution)

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        # base case
        if len(nums) == 1:
            return [nums.copy()]                # one element: one permutation

        for i in range(len(nums)):
            n = nums.pop(0)                     # take the front element out
            perms = self.permute(nums)          # all permutations of the rest

            for perm in perms:
                perm.append(n)                  # attach the removed element
            result.extend(perms)
            nums.append(n)                      # put it at the back, rotating the list

        return result
```

- **Time:** O(n x n!), since there are n! permutations, each built with O(n) work (and `pop(0)` costs O(n) per call as well)
- **Space:** O(n) recursion depth, plus the intermediate lists, with the output itself O(n x n!)
- **Verdict:** Correct, and the rotation trick is clever. Each iteration removes the front element and appends it to the back afterwards, so across the loop every element takes a turn being the one removed. It is less common than the standard template, so be ready to explain it.

**Your two submissions are equivalent.** `nums.copy()` and `nums[:]` both make a shallow copy of the list, so the second block is the same algorithm with a different spelling. Only one is needed.

### 2. Backtracking with a Used Array (Standard Template)

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())         # copy, because path keeps changing
                return
            for i in range(len(nums)):
                if used[i]:
                    continue                    # already placed in this permutation
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()                      # undo
                used[i] = False

        dfs()
        return res
```

- **Time:** O(n x n!)
- **Space:** O(n) for `path`, `used` and the recursion
- **Verdict:** The expected interview answer. It is the same decision tree as Subsets, except that each level chooses among unused elements instead of include/exclude.

### 3. Backtracking with Swapping (In-Place)

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start):
            if start == len(nums):
                res.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]     # choose nums[i] for position start
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]     # undo the swap

        dfs(0)
        return res
```

- **Time:** O(n x n!)
- **Space:** O(n) recursion only, with no `used` array
- **Verdict:** The most space-efficient version. The prefix `nums[:start]` is the fixed part of the permutation, and the suffix holds the remaining candidates. It mutates `nums` temporarily but restores it.

### 4. Library: `itertools.permutations`

```python
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in permutations(nums)]
```

- **Time:** O(n x n!)
- **Space:** O(n x n!) for the output
- **Verdict:** One line, and fine in practice. Interviewers usually want the manual version, so mention it as a shortcut only.

---

## Complexity Summary

| Approach | Time | Space (extra) | Notes |
|---|---|---|---|
| Pop / recurse / append (yours) | O(n x n!) | O(n) | Elegant, uses list rotation |
| **Backtracking with `used`** | **O(n x n!)** | **O(n)** | **Standard template** |
| Backtracking with swaps | O(n x n!) | O(n) | No `used` array |
| `itertools.permutations` | O(n x n!) | O(1) | Library shortcut |

*All are optimal, because the output has n! permutations of length n.*

---

## Walkthrough (Your Solution)

`nums = [1, 2, 3]`

Top-level loop, with `nums` rotating each time:

| i | nums before | pop(0) gives n | nums passed down | perms of rest | After appending n | nums after append |
|---|---|---|---|---|---|---|
| 0 | [1,2,3] | 1 | [2,3] | [[2,3],[3,2]] | [[2,3,1],[3,2,1]] | [2,3,1] |
| 1 | [2,3,1] | 2 | [3,1] | [[3,1],[1,3]] | [[3,1,2],[1,3,2]] | [3,1,2] |
| 2 | [3,1,2] | 3 | [1,2] | [[1,2],[2,1]] | [[1,2,3],[2,1,3]] | [1,2,3] |

Result: `[[2,3,1],[3,2,1],[3,1,2],[1,3,2],[1,2,3],[2,1,3]]`, which is all 6 permutations.

The inner call `permute([2,3])` works the same way: pop 2, base case on `[3]` gives `[[3]]`, append 2 to get `[[3,2]]`, rotate to `[3,2]`, pop 3, base case on `[2]` gives `[[2]]`, append 3 to get `[[2,3]]`, and the list returns to its original order after the loop.

---

## Why It Works

**The rotation:** after n iterations, each of which moves the front element to the back, the list is rotated n times and returns to its original order. That is why `nums` is unchanged when the function returns, which the caller relies on.

**Coverage:** in iteration `i`, the element removed is the one originally at index `i` (since the previous `i` elements have rotated behind it). So every element gets a turn as the "last" element of its permutations, and the recursion covers all orderings of the rest.

**Why `copy()` in the base case:** the recursion returns lists that the caller then **mutates** with `perm.append(n)`. Returning `[nums]` itself would hand back a reference to the caller's own list, so the append would corrupt it. The copy (`nums.copy()` or `nums[:]`) prevents that aliasing.

**Why it builds permutations backwards:** each level appends `n` at the end, so the permutation is assembled from the last position to the first. The order of results differs from the standard template, which is fine since any order is accepted.

---

## Edge Cases and Pitfalls

- **Single element** (`[1]`): returns `[[1]]`, handled by the base case.
- **Two elements** (`[0,1]`): returns both orderings.
- **Returning `[nums]` in the base case:** aliasing bug, because the caller's `perm.append(n)` would modify the live `nums`.
- **Forgetting `nums.append(n)` after recursing:** the list shrinks permanently and the rotation breaks, so later iterations see the wrong elements.
- **Mutating the input temporarily:** your solution modifies `nums` during the run, but it ends up restored. In an interview, mention that the input is mutated mid-execution (not safe for concurrent use).
- **`pop(0)` is O(n)** on a Python list. `collections.deque` with `popleft()` is O(1), though for n at most 6 it makes no difference.
- **Empty input:** the constraints guarantee at least one element. For an empty list your code would recurse on an empty array and hit `pop(0)` only inside the loop, which doesn't run, so it returns `[]` (while the mathematically correct answer is `[[]]`).
- **Duplicates:** this problem guarantees distinct elements. With duplicates you need LC 47, with sorting and a skip rule.
- **Style note:** `if (len(nums) == 1):` doesn't need parentheses in Python. `self.permute(nums)` works, though a nested helper is more common. `list[int]` needs Python 3.9+ (LeetCode's template uses `List[int]`). Your two code blocks are duplicates, and the `//` separator would need removing before submitting.

---

## Interview Follow-Ups

- **"What if the array has duplicates?"** Sort it, and skip an element if it equals the previous one and the previous one is unused (LC 47).
- **"Can you do it in place without a `used` array?"** Yes, the swap-based version.
- **"Return the next permutation only?"** Find the rightmost ascent, swap with the next larger element to its right, and reverse the suffix, in O(n) (LC 31).
- **"Return the k-th permutation?"** Use the factorial number system to pick each digit directly, in O(n²) (LC 60).
- **"Why is the complexity O(n x n!)?"** There are n! leaves, and each permutation costs O(n) to copy into the result.
- **"What if n is large?"** The output is factorial, so generate permutations lazily with a generator or use Heap's algorithm.
- **"Permutations of a subset of size k?"** Stop at depth k instead of n (partial permutations, n!/(n-k)!).

---

## Related Problems

- **47. Permutations II:** permutations with duplicates
- **31. Next Permutation:** the next one in lexicographic order
- **60. Permutation Sequence:** the k-th permutation
- **78. Subsets:** the include/exclude backtracking template
- **77. Combinations:** subsets of fixed size k
- **39. Combination Sum:** backtracking with a target
- **17. Letter Combinations of a Phone Number:** decision tree over digits
- **784. Letter Case Permutation:** binary choice per character
- **996. Number of Squareful Arrays:** permutations with pruning

---
