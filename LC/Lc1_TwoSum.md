# 1. Two Sum

**Difficulty:** Easy | **Topics:** Array, Hash Table

---

## Problem Description

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

**Example 1**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9
```

**Example 2**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

**Follow-up:** Can you come up with an algorithm that is less than O(n²) time complexity?

---

## Intuition and Key Insight

For each number `x`, you need to know whether `target - x` (its **complement**) exists elsewhere in the array. Searching the array for every element is the O(n²) brute force. A hash map turns "does the complement exist, and where?" into an O(1) lookup.

The key trick is to **build the map as you go**. When you reach index `i`, any valid partner at an earlier index is already in the map. Every pair is therefore found when its second element is processed, with no second pass.

**Pattern to recognize:** "find a pair/element satisfying a relation with the current element" → store what you've seen in a hash map (value → index) and look up the complement.

---

## Approaches

### 1. Brute Force: Check Every Pair

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

- **Time:** O(n²)
- **Space:** O(1)
- **Verdict:** With n up to 10^4 this is about 5 x 10^7 comparisons, which passes on LeetCode but is the answer the follow-up is asking you to beat. Mention it as the baseline, then optimize.

### 2. Sorting + Two Pointers

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep original indices, since sorting would otherwise lose them
        indexed = sorted(enumerate(nums), key=lambda p: p[1])
        l, r = 0, len(indexed) - 1
        while l < r:
            s = indexed[l][1] + indexed[r][1]
            if s == target:
                return [indexed[l][0], indexed[r][0]]
            if s < target:
                l += 1            # need a bigger sum
            else:
                r -= 1            # need a smaller sum
        return []
```

- **Time:** O(n log n), dominated by the sort
- **Space:** O(n) for the (index, value) pairs
- **Verdict:** Slower than the hash map, and the index bookkeeping costs O(n) space anyway. It is still worth knowing because this is exactly the technique used when the input is already sorted (LC 167), where it needs only O(1) space.

### 3. Hash Map, Two Passes

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of = {}
        for i, num in enumerate(nums):      # pass 1: build value -> index
            index_of[num] = i
        for i, num in enumerate(nums):      # pass 2: look up complements
            j = index_of.get(target - num)
            if j is not None and j != i:    # must not reuse the same element
                return [i, j]
        return []
```

- **Time:** O(n)
- **Space:** O(n)
- **Verdict:** Correct and linear, but it needs the `j != i` guard and makes two passes. The `[3,3]` case works because the dict keeps the **last** index for duplicate values (index 1), so the lookup from `i = 0` finds `j = 1`.

### 4. Hash Map, One Pass (Optimal)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                            # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:           # O(1) average lookup
                return [seen[complement], i]
            seen[num] = i                    # insert AFTER checking
        return []                            # unreachable: a solution is guaranteed
```

- **Time:** O(n), one pass with O(1) average lookups and inserts
- **Space:** O(n), since the map holds up to n - 1 entries before the answer is found
- **Verdict:** This is the expected interview answer. Checking before inserting means an element can never match itself, so no `j != i` guard is needed, and it can exit early.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n²) | O(1) | Passes here, but the follow-up wants better |
| Sort + two pointers | O(n log n) | O(n) | Must track original indices |
| Hash map (two pass) | O(n) | O(n) | Needs the `j != i` guard |
| **Hash map (one pass)** | **O(n)** | **O(n)** | **Optimal, early exit, simplest logic** |

---

## Walkthrough (One-Pass Hash Map)

`nums = [2, 7, 11, 15]`, `target = 9`

| i | num | complement | In `seen`? | Action | `seen` |
|---|---|---|---|---|---|
| 0 | 2 | 7 | No | store `2 -> 0` | {2: 0} |
| 1 | 7 | 2 | **Yes** (index 0) | return `[0, 1]` | |

Duplicate case, `nums = [3, 3]`, `target = 6`:

| i | num | complement | In `seen`? | Action | `seen` |
|---|---|---|---|---|---|
| 0 | 3 | 3 | No (map is empty) | store `3 -> 0` | {3: 0} |
| 1 | 3 | 3 | **Yes** (index 0) | return `[0, 1]` | |

---

## Edge Cases and Pitfalls

- **Same element twice** (`nums = [3,2,4]`, `target = 6`): `3 + 3 = 6`, but there is only one 3, so the answer is `[1,2]` (2 + 4), not `[0,0]`. Checking before inserting prevents this.
- **Duplicate values** (`[3,3]`, target 6): valid, because they are two different indices. The one-pass version handles this naturally.
- **Return indices, not values.** This is a common slip, and it's why sorting needs extra bookkeeping.
- **Negative numbers and zero:** no special handling. `[-3, 4, 3, 90]` with target 0 gives `[0, 2]`, and `[0, 4, 3, 0]` with target 0 gives `[0, 3]`.
- **Insert after the lookup.** If you insert `num` first, an element can match itself (for example `nums = [3,2,4]`, target 6 would wrongly return `[0,0]`).
- **No overflow concern in Python.** In C++ or Java, `target - num` stays within roughly ±2 x 10^9, so use `long long` in C++ to be safe.

---

## Interview Follow-Ups

- **"What if the array is sorted?"** Use two pointers in O(n) time and O(1) space (LC 167).
- **"What if there can be multiple solutions, or you need all pairs?"** Use a hash map of value → list of indices, or sort and use two pointers while skipping duplicates (the pattern in 3Sum).
- **"What if memory is constrained?"** Sort with two pointers over the values, accepting O(n log n) time. If you need original indices you must still store them, so the savings only apply when you need the values, not the indices.
- **"What if numbers arrive as a stream?"** This is a data structure design problem (LC 170): store counts in a hash map, then `add` is O(1) and `find` is O(n).
- **"What if the array is too large for memory?"** Hash-partition the values by `x` and `target - x` into the same bucket, so each pair lands together, then solve each bucket in memory.

---

## Related Problems

- **167. Two Sum II (Input Array Is Sorted):** two pointers, O(1) space
- **15. 3Sum:** sort + two pointers, skipping duplicates
- **18. 4Sum:** generalization of 3Sum
- **653. Two Sum IV (BST):** the same idea on a binary search tree
- **170. Two Sum III (Data Structure Design):** streaming version
- **560. Subarray Sum Equals K:** prefix sums with a hash map, the same "look up the complement" idea
- **454. 4Sum II:** split into two halves and use a hash map of pair sums

---

Send the next problem, or paste your own Two Sum solution and I'll compare it against these notes. When you're ready, I can also combine 1 and 217 (Python and C++) into a single study document.
