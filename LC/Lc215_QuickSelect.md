# 215. Kth Largest Element in an Array

**Difficulty:** Medium | **Topics:** Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect

**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/

---

## Problem Description

Given an integer array `nums` and an integer `k`, return the **k-th largest element** in the array.

Note that it is the k-th largest element in **sorted order**, not the k-th distinct element.

Can you solve it without sorting?

**Example 1**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2**
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints**
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Intuition and Key Insight

The k-th largest element is the element at index `n - k` of the **sorted** array. Sorting finds it in O(n log n), but you do not need the whole array sorted, only one element in its correct position.

Three ways to avoid a full sort:
- **Min-heap of size k:** keep the k largest values seen so far. The heap's top is the k-th largest. O(n log k).
- **Quickselect:** partition around a pivot as in quicksort, but recurse into only the side that contains index `n - k`. Average O(n).
- **Counting sort:** values lie in a small range (-10^4 to 10^4), so counting works in O(n + range).

Your two solutions are the sorting baseline and quickselect.

**Pattern to recognize:** "k-th largest or smallest, or top k" → heap of size k, or quickselect.

---

## Approaches

### 1. Sorting (Your First Solution)

```python
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]              # k-th largest sits at index n - k
```

- **Time:** O(n log n)
- **Space:** O(n) in the worst case for Timsort's auxiliary space (O(1) extra conceptually)
- **Verdict:** Correct, shortest, and fine to say first in an interview. It does not meet the "without sorting" follow-up, so move on to a heap or quickselect.

### 2. Min-Heap of Size k

```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)             # drop the smallest, keep the k largest
        return heap[0]                          # smallest of the k largest = k-th largest
```

- **Time:** O(n log k)
- **Space:** O(k)
- **Verdict:** The most common interview answer. It is predictable, has no bad worst case, and works on streams. A shortcut is `heapq.nlargest(k, nums)[-1]`.

### 3. Quickselect (Your Second Solution, Optimal on Average)

```python
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k                       # target index in sorted order

        def quickSelect(l, r):
            pivot, p = nums[r], l               # pivot is the last element, p is the store index
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1                      # grow the "<= pivot" region
            nums[p], nums[r] = nums[r], nums[p] # place the pivot at its final index

            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)
```

- **Time:** O(n) average, **O(n²) worst case** (for example a sorted array with a last-element pivot)
- **Space:** O(log n) average recursion depth, O(n) worst case
- **Verdict:** Average-case optimal and meets the follow-up. The last-element pivot is a real weakness: on sorted or all-equal input it degrades to O(n²), and LeetCode has tests that exploit this (see the improvement below).

### 4. Quickselect with a Random Pivot (Safer)

```python
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickSelect(l, r):
            rand = random.randint(l, r)
            nums[rand], nums[r] = nums[r], nums[rand]   # move a random pivot to the end
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > target: return quickSelect(l, p - 1)
            elif p < target: return quickSelect(p + 1, r)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)
```

- **Time:** O(n) expected, with an extremely low chance of O(n²)
- **Space:** O(log n) expected
- **Verdict:** One extra swap makes the bad case essentially impossible. This is the version to write in an interview.

### 5. Counting Sort (Uses the Small Value Range)

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        OFFSET = 10_000
        count = [0] * (2 * OFFSET + 1)
        for num in nums:
            count[num + OFFSET] += 1
        for v in range(2 * OFFSET, -1, -1):     # scan from the largest value down
            k -= count[v]
            if k <= 0:
                return v - OFFSET
```

- **Time:** O(n + R), where R = 20001 is the value range
- **Space:** O(R)
- **Verdict:** Linear time, no recursion, and no bad worst case. It depends on the bounded range, so it is a good "use the constraints" answer.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Sort | O(n log n) | O(1) to O(n) | Simplest, not the "without sorting" answer |
| Min-heap of size k | O(n log k) | O(k) | Reliable, works on streams |
| **Quickselect, last pivot (yours)** | **O(n) avg, O(n²) worst** | **O(log n)** | **Fast on average, vulnerable to sorted input** |
| **Quickselect, random pivot** | **O(n) expected** | **O(log n)** | **Preferred form** |
| Counting sort | O(n + R) | O(R) | Uses the value bound |

---

## Walkthrough (Your Quickselect)

`nums = [3, 2, 1, 5, 6, 4]`, `k = 2`, so the target index is `6 - 2 = 4`.

**Call 1:** `l = 0`, `r = 5`, pivot = `4`, `p = 0`

| i | nums[i] | <= 4? | Action | nums | p |
|---|---|---|---|---|---|
| 0 | 3 | Yes | swap with p=0 | [3,2,1,5,6,4] | 1 |
| 1 | 2 | Yes | swap with p=1 | [3,2,1,5,6,4] | 2 |
| 2 | 1 | Yes | swap with p=2 | [3,2,1,5,6,4] | 3 |
| 3 | 5 | No | skip | [3,2,1,5,6,4] | 3 |
| 4 | 6 | No | skip | [3,2,1,5,6,4] | 3 |

Place the pivot: swap `nums[3]` and `nums[5]` → `[3,2,1,4,6,5]`, `p = 3`.
`p (3) < target (4)`, so recurse on the right side: `quickSelect(4, 5)`.

**Call 2:** `l = 4`, `r = 5`, pivot = `5`, `p = 4`

| i | nums[i] | <= 5? | Action | p |
|---|---|---|---|---|
| 4 | 6 | No | skip | 4 |

Place the pivot: swap `nums[4]` and `nums[5]` → `[3,2,1,4,5,6]`, `p = 4`.
`p == target`, so return `nums[4] = 5`.

Result: `5`.

---

## Why It Works

After partitioning, the pivot sits at index `p`, which is its **final sorted position**. Everything to its left is `<=` it, and everything to its right is `>` it. If `p` equals the target index, the pivot is the answer. If `p` is larger, the target lies in the left part, and if smaller, in the right part. Only one side is ever explored, which is why the average cost is n + n/2 + n/4 + ... = O(n), instead of quicksort's O(n log n).

**Why `k = n - k`:** quickselect finds an index in ascending order, and the k-th largest is the (n - k)-th smallest, counting from 0.

**Why the heap works:** a min-heap of size k keeps the k largest values seen. Its top is the smallest of those, which is exactly the k-th largest.

---

## Edge Cases and Pitfalls

- **Single element** (`[5]`, `k = 1`): target index 0, the partition is trivial, and it returns 5.
- **Duplicates** (`[3,2,3,1,2,4,5,5,6]`, `k = 4`): the k-th largest counts duplicates, so the answer is `4`, not the 4th distinct value.
- **All equal** (`[2,2,2,2]`): with `<=` and a last-element pivot, every element moves into the "<= pivot" region, so `p` ends at `r` each time and the recursion shrinks by only one element. That makes it O(n²) and risks deep recursion (Python's default limit is about 1000, and n goes up to 10^5). This is the realistic way the submitted version fails.
- **Sorted input:** the same O(n²) behavior with the last-element pivot. Random pivots, or the three-way partition below, fix it.
- **Off-by-one on k:** `n - k` for the k-th largest. `k = 1` is the maximum, at index `n - 1`.
- **Mutating the input:** both solutions reorder `nums`. Copy first if the caller needs the original.
- **Recursion limit:** worst-case quickselect recursion in Python can hit `RecursionError`. An iterative loop (`while l <= r`) avoids it.
- **Heap direction:** use a min-heap of size k, not a max-heap of everything, to get O(n log k).
- **Style note:** your code is correct. The `//` separator and two classes in one cell must be split before submitting, and `list[int]` needs Python 3.9+ (LeetCode's template uses `List[int]`).

---

## Interview Follow-Ups

- **"Can you avoid the O(n²) worst case?"** Use a random pivot (expected O(n)), a three-way partition for many duplicates, or median of medians for a guaranteed O(n), though that is rarely worth the complexity.
- **"What if the data is a stream?"** Keep a size-k min-heap, updating it on each arrival (LC 703).
- **"What if the data doesn't fit in memory?"** Use a heap, which needs only O(k) memory, or do a distributed quickselect by counting values per range.
- **"What is the difference between heap and quickselect here?"** The heap is O(n log k), stable in performance, and streamable. Quickselect is O(n) average, in place, and needs the whole array in memory.
- **"Return the top k elements, not just the k-th?"** After quickselect, the elements at indices `n - k` and above are the k largest (unordered).
- **"Smallest k-th instead?"** Use target index `k - 1`.
- **"Can you do better than O(n)?"** No, you must look at every element at least once.

---

## Related Problems

- **347. Top K Frequent Elements:** top k by frequency, bucket sort or heap
- **973. K Closest Points to Origin:** top k by distance, heap or quickselect
- **703. Kth Largest Element in a Stream:** size-k min-heap
- **378. Kth Smallest Element in a Sorted Matrix:** heap or binary search
- **295. Find Median from Data Stream:** two heaps
- **912. Sort an Array:** quicksort, heap sort, merge sort
- **75. Sort Colors:** three-way partition (Dutch national flag)
- **692. Top K Frequent Words:** heap with a custom comparator
- **414. Third Maximum Number:** tracking the top 3

---
