# 217. Contains Duplicate

**Difficulty:** Easy | **Topics:** Array, Hash Table, Sorting

## Problem Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1**
```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2**
```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

**Constraints**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Intuition and Key Insight

The question is "have I seen this value before?" Whenever a problem asks that, think **hash set**, which gives O(1) average lookup and insertion. Checking before inserting lets you return as soon as the first duplicate appears.

**Pattern to recognize:** existence or duplicate checks → hash set, or sort and compare neighbors.

---

## Approaches

### 1. Brute Force: Compare Every Pair

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
```

- **Time:** O(n²)
- **Space:** O(1)
- **Verdict:** With n up to 10^5 that's about 10^10 comparisons, so it will time out. Mention it in an interview to show you can reason from the baseline, then move on.

### 2. Sorting

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

- **Time:** O(n log n), dominated by the sort
- **Space:** O(1) extra if sorting in place, but Python's Timsort uses O(n) auxiliary space in the worst case. If you don't want to mutate the input, `sorted(nums)` costs O(n).
- **Verdict:** A good answer when memory is tight, since it avoids the extra hash set. The tradeoff is slower time and mutating the input.

### 3. Hash Set, Single Pass (Optimal)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()                  # values encountered so far
        for num in nums:
            if num in seen:           # O(1) average lookup
                return True           # early exit on first duplicate
            seen.add(num)             # record this value
        return False                  # finished with no repeats
```

- **Time:** O(n), one pass with O(1) average operations
- **Space:** O(n), since the set holds up to n elements when there are no duplicates
- **Verdict:** This is the expected interview answer. It trades O(n) space for linear time, and the early exit means it can finish well before the end when a duplicate appears early.

### 4. One-Liner (Pythonic)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

- **Time:** O(n)
- **Space:** O(n)
- **Verdict:** Concise and fine in practice. It always builds the full set, so it has no early exit. In an interview, write approach 3 first, since it shows you understand the mechanics, and mention this as a shortcut.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n²) | O(1) | TLE on large inputs |
| Sorting | O(n log n) | O(1) to O(n) | Mutates input, saves memory |
| Hash set (single pass) | **O(n)** | **O(n)** | **Optimal, early exit** |
| `len(set(nums))` | O(n) | O(n) | Concise, no early exit |

---

## Walkthrough (Hash Set)

`nums = [1, 2, 3, 1]`

| Step | num | In `seen`? | Action | `seen` |
|---|---|---|---|---|
| 1 | 1 | No | add | {1} |
| 2 | 2 | No | add | {1, 2} |
| 3 | 3 | No | add | {1, 2, 3} |
| 4 | 1 | **Yes** | return `True` | |

---

## Edge Cases and Pitfalls

- **Single element** (`[5]`): no duplicate is possible, so return `False`. The loop handles it naturally.
- **All identical** (`[2,2,2,2]`): returns `True` at the second element.
- **Negative numbers and zero:** sets handle these without special treatment.
- **Check before adding.** If you add first and then check, every element looks like a duplicate.
- **Worst-case hashing:** set operations are O(1) on average, but pathological hash collisions can degrade them. This almost never comes up in interviews, but it's worth knowing the "average" qualifier exists.

---

## Interview Follow-Ups

- **"What if memory is limited?"** Use sorting, which gives O(1) extra space apart from the sort itself, at O(n log n) time.
- **"What if the array is already sorted?"** Compare adjacent elements in O(n) time and O(1) space.
- **"What if the array is too large for memory?"** Use external sorting, or hash-partition the data into buckets that fit in memory and check each bucket.
- **"What if values fall in a small known range?"** Use a boolean array or bitset as the lookup table instead of a hash set.

---

## Related Problems

- **219. Contains Duplicate II:** duplicates within distance k (hash map or sliding window)
- **220. Contains Duplicate III:** duplicates within value difference t and index distance k (bucketing)
- **1. Two Sum:** hash map for complement lookup
- **242. Valid Anagram:** frequency counting
- **287. Find the Duplicate Number:** O(1) space using Floyd's cycle detection
- **136. Single Number:** XOR trick

---

Send over the next problem, or paste your own 217 solution and I'll compare it against these notes.
