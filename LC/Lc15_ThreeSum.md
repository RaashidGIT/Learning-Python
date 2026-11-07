# 15. 3Sum

**Difficulty:** Medium | **Topics:** Array, Two Pointers, Sorting

**Link:** https://leetcode.com/problems/3sum/

---

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must **not contain duplicate triplets**. The order of the triplets and the order within each triplet do not matter.

**Example 1**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

**Example 2**
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

**Example 3**
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

**Constraints**
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

---

## Intuition and Key Insight

This is Two Sum with one extra loop. Fix one number `a`, then you need two other numbers that sum to `-a`. If the array is **sorted**, the two-number search becomes a two-pointer sweep from both ends:

- Sum too big → move the right pointer left (smaller value).
- Sum too small → move the left pointer right (larger value).
- Sum equals 0 → record the triplet, then move on.

Sorting also solves the hardest part of the problem, **duplicates**. Equal values sit next to each other, so you can skip repeats of the fixed number and repeats of the left pointer without needing a set.

**Pattern to recognize:** "find k numbers that sum to a target, with no duplicate combinations" → sort, fix k-2 elements, then two pointers on the rest.

---

## Approaches

### 1. Brute Force: Three Nested Loops

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        found = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        found.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return [list(t) for t in found]
```

- **Time:** O(n³)
- **Space:** O(m), where m is the number of unique triplets (the set of results)
- **Verdict:** With n up to 3000 that is about 4.5 x 10^9 triples, so it will time out. Mention it as the baseline.

### 2. Hash Set (Two Sum Inside a Loop)

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue                            # skip duplicate first element
            seen = set()
            j = i + 1
            while j < len(nums):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.append([nums[i], complement, nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1                      # skip duplicate second element
                seen.add(nums[j])
                j += 1
        return res
```

- **Time:** O(n²)
- **Space:** O(n) for the set
- **Verdict:** The same time as two pointers, but it uses extra space and the duplicate handling is harder to get right. Know it as the "Two Sum inside a loop" idea, then prefer two pointers.

### 3. Sort + Two Pointers (Your Solution, Optimal)

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:      # skip duplicate first element
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1                      # sum too big, need smaller
                elif threeSum < 0:
                    l += 1                      # sum too small, need bigger
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1                  # skip duplicate second element

        return res
```

- **Time:** O(n²), since sorting is O(n log n) and each fixed `i` costs one O(n) two-pointer sweep
- **Space:** O(1) extra, or O(n) to O(log n) depending on the sort implementation (output excluded)
- **Verdict:** Optimal and the expected interview answer. No hash set is needed because sorting makes duplicates adjacent.

### 4. Sort + Two Pointers with Early Exit (Minor Optimization)

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break                           # smallest is positive, no way to reach 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
```

- **Time:** O(n²)
- **Space:** O(1) extra
- **Verdict:** Same complexity, with an early `break` once the smallest number is positive and a cleaner bounds check order (`l < r` is tested first). Moving `r` as well after a match is also fine, because the old `r` cannot pair with the new `l` to reach 0.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n³) | O(m) | TLE |
| Hash set per element | O(n²) | O(n) | Duplicate handling is tricky |
| **Sort + two pointers (yours)** | **O(n²)** | **O(1)** | **Optimal, expected answer** |
| Two pointers + early exit | O(n²) | O(1) | Slightly faster in practice |

---

## Walkthrough (Your Solution)

`nums = [-1, 0, 1, 2, -1, -4]` → sorted: `[-4, -1, -1, 0, 1, 2]`

| i | a | l | r | sum | Action | res |
|---|---|---|---|---|---|---|
| 0 | -4 | 1 | 5 | -4 + -1 + 2 = -3 | < 0, `l = 2` | |
| 0 | -4 | 2 | 5 | -4 + -1 + 2 = -3 | < 0, `l = 3` | |
| 0 | -4 | 3 | 5 | -4 + 0 + 2 = -2 | < 0, `l = 4` | |
| 0 | -4 | 4 | 5 | -4 + 1 + 2 = -1 | < 0, `l = 5`, loop ends | |
| 1 | -1 | 2 | 5 | -1 + -1 + 2 = 0 | match, record, `l = 3` | [[-1,-1,2]] |
| 1 | -1 | 3 | 5 | -1 + 0 + 2 = 1 | > 0, `r = 4` | |
| 1 | -1 | 3 | 4 | -1 + 0 + 1 = 0 | match, record, `l = 4` | [[-1,-1,2],[-1,0,1]] |
| 2 | -1 | | | | same as previous, skipped | |
| 3 | 0 | 4 | 5 | 0 + 1 + 2 = 3 | > 0, `r = 4`, loop ends | |
| 4, 5 | | | | | not enough elements on the right | |

Result: `[[-1,-1,2],[-1,0,1]]`.

---

## Why It Works

**Fixing `i`:** after sorting, every triplet `(a, b, c)` with `a <= b <= c` is found when `a` is the fixed element. Skipping `i` when `nums[i] == nums[i - 1]` means each distinct value of `a` is used as the first element only once, so duplicate triplets starting with the same `a` can't appear.

**Two pointers:** for a fixed `a`, if `a + nums[l] + nums[r]` is too large, `nums[r]` cannot pair with *any* `l' >= l` (they are all at least as large as `nums[l]`), so `r` can be discarded. The same reasoning applies symmetrically when the sum is too small.

**After a match:** advancing `l` past equal values prevents the same `(a, b, c)` from being recorded twice. `r` doesn't need its own skip loop, because once `l` has moved to a new value, the old `r` produces a sum that is no longer 0, and the usual moves take care of `r`.

---

## Edge Cases and Pitfalls

- **All zeros** (`[0,0,0,0]`): the answer is a single `[0,0,0]`. The duplicate skips prevent repeats.
- **No solution** (`[0,1,1]`): returns `[]`.
- **Fewer than 3 elements:** the constraints rule it out, but in general the loop simply doesn't find anything.
- **Duplicates must be skipped, not filtered afterward.** Dedupe on the fly with sorting, which is cheaper than building a set of tuples.
- **Skip check order:** you wrote `while nums[l] == nums[l - 1] and l < r`. It works because after `l += 1` you can have `l == len(nums)` only if `r` was already at the last index and `l` passed it, which can happen when `l` becomes equal to `r + 1`. In that case `nums[l]` could be out of range. Put `l < r` first (`while l < r and nums[l] == nums[l - 1]`), so the bounds check short-circuits before indexing. This is a subtle point worth getting right.
- **Don't skip with `i > 0 and nums[i] == nums[i+1]`.** Comparing with the **previous** element is correct. Comparing with the next one would skip the first copy and miss triplets like `[-1,-1,2]`, which need two equal values.
- **Sorting mutates the input.** Copy first if you need the original order.
- **Returning indices instead of values:** a different problem. Sorting loses the original positions, so you would track them separately.
- **Style note:** naming a variable `threeSum` shadows the method name inside its own scope. It is legal but confusing, and `total` or `s` is clearer. `list[int]` needs Python 3.9+ (LeetCode's template uses `List[int]`).

---

## Interview Follow-Ups

- **"Can you do better than O(n²)?"** Not in general. 3Sum is the classic problem conjectured to need about quadratic time.
- **"What if you need 4 numbers (4Sum), or k numbers?"** Sort, fix k - 2 elements with nested loops, then two pointers, giving O(n^(k-1)). Use recursion for general k (LC 18).
- **"What if the target isn't 0?"** Replace `0` with `target`, and everything else stays the same.
- **"Find the triplet closest to the target."** Same two-pointer structure, tracking the smallest `abs(sum - target)` (LC 16).
- **"Count triplets with sum less than the target."** When `sum < target`, every index between `l` and `r` also works, so add `r - l` (LC 259).
- **"What if the input can't be modified?"** Copy and sort, using O(n) extra space.
- **"Return indices instead of values?"** Sort an array of `(value, index)` pairs.

---

## Related Problems

- **1. Two Sum:** the hash map version of the inner problem
- **167. Two Sum II (Input Array Is Sorted):** the two-pointer sweep used here
- **16. 3Sum Closest:** the same sweep tracking the closest sum
- **18. 4Sum:** one more nested loop
- **259. 3Sum Smaller:** counting with two pointers
- **454. 4Sum II:** hash map of pair sums
- **11. Container With Most Water:** two pointers from both ends
- **42. Trapping Rain Water:** two pointers with running maxima

---
