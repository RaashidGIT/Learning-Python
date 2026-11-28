# 347. Top K Frequent Elements

**Difficulty:** Medium | **Topics:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

**Link:** https://leetcode.com/problems/top-k-frequent-elements/

---

## Problem Description

Given an integer array `nums` and an integer `k`, return the **k most frequent elements**. You may return the answer in **any order**.

**Example 1**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2**
```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow-up:** Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

---

## Intuition and Key Insight

Two steps: **count** how often each value appears, then **select the k values with the highest counts**.

Counting is a hash map, O(n). Selection is where the approaches differ:
- Sort all distinct values by count: O(n log n), which the follow-up forbids.
- Keep a min-heap of size k: O(n log k).
- **Bucket sort by frequency:** a value can appear at most n times, so make an array of n + 1 buckets where bucket `c` holds the values that appear exactly `c` times. Then walk from the highest bucket down and collect k values. This is O(n).

Your solution is the bucket sort approach, which is the one that meets the follow-up in the strongest way.

**Pattern to recognize:** "top k by frequency" → count with a hash map, then heap (O(n log k)) or bucket sort (O(n)) because frequencies are bounded by n.

---

## Approaches

### 1. Sort by Frequency

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [num for num, _ in sorted(count.items(), key=lambda x: -x[1])[:k]]
```

- **Time:** O(n log n), dominated by sorting the distinct values (up to n of them)
- **Space:** O(n)
- **Verdict:** Simple and correct, but it does not satisfy the follow-up. Mention it as the baseline.

### 2. Min-Heap of Size k

```python
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []                                   # (frequency, value), smallest frequency on top
        for num, c in count.items():
            heapq.heappush(heap, (c, num))
            if len(heap) > k:
                heapq.heappop(heap)                 # evict the least frequent of the k+1
        return [num for _, num in heap]
```

- **Time:** O(n log k), since each of up to n distinct values costs O(log k)
- **Space:** O(n) for the map, O(k) for the heap
- **Verdict:** The common interview answer, and a good fit when k is much smaller than n. It beats O(n log n) whenever k is small. A one-liner alternative is `heapq.nlargest(k, count.keys(), key=count.get)`.

### 3. Bucket Sort by Frequency (Your Solution, Optimal)

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}                                  # value -> frequency
        freq = [[] for i in range(len(nums) + 1)]   # freq[c] = values appearing exactly c times

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):       # highest frequency first
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```

- **Time:** O(n), with one pass to count, one to fill buckets, and at most n + 1 buckets to scan
- **Space:** O(n) for the map and the buckets
- **Verdict:** Optimal and satisfies the follow-up. The array has `len(nums) + 1` slots because a frequency can be anywhere from 1 to n, and index 0 is unused.

### 4. Quickselect

```python
import random
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_idx):
            pivot_freq = count[unique[pivot_idx]]
            unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]
            store = left
            for i in range(left, right):
                if count[unique[i]] < pivot_freq:
                    unique[store], unique[i] = unique[i], unique[store]
                    store += 1
            unique[right], unique[store] = unique[store], unique[right]
            return store

        def select(left, right, k_smallest):
            if left == right:
                return
            p = partition(left, right, random.randint(left, right))
            if p == k_smallest:
                return
            elif k_smallest < p:
                select(left, p - 1, k_smallest)
            else:
                select(p + 1, right, k_smallest)

        n = len(unique)
        select(0, n - 1, n - k)                     # put the k most frequent at the end
        return unique[n - k:]
```

- **Time:** O(n) average, O(n²) worst case
- **Space:** O(n)
- **Verdict:** Average linear time with no extra buckets, but the worst case and the code size make it a poor interview choice unless asked. Mention it as an option.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Sort by frequency | O(n log n) | O(n) | Fails the follow-up |
| Min-heap of size k | O(n log k) | O(n) | Best when k is small |
| **Bucket sort (yours)** | **O(n)** | **O(n)** | **Optimal, meets follow-up** |
| Quickselect | O(n) avg, O(n²) worst | O(n) | Not worth it in most interviews |

---

## Walkthrough (Your Solution)

`nums = [1, 1, 1, 2, 2, 3]`, `k = 2`

**Step 1: count**

`count = {1: 3, 2: 2, 3: 1}`

**Step 2: fill buckets** (`freq` has 7 slots, indices 0 to 6)

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Values | [] | [3] | [2] | [1] | [] | [] | [] |

**Step 3: scan from the right, collecting until `len(res) == k`**

| i | freq[i] | Action | res |
|---|---|---|---|
| 6 | [] | nothing | [] |
| 5 | [] | nothing | [] |
| 4 | [] | nothing | [] |
| 3 | [1] | append 1 | [1] |
| 2 | [2] | append 2, `len == k`, **return** | [1, 2] |

Result: `[1, 2]`.

---

## Why It Works

Bucket index equals frequency, so the buckets are already sorted by frequency. Scanning from the highest index down visits values in descending order of frequency, and stopping after k values returns the k most frequent. No comparison sorting is needed because frequencies are small integers bounded by n.

**Why `n + 1` buckets:** the maximum possible frequency is n (all elements equal), so index n must exist.

**Why the loop stops at index 1:** `range(len(freq) - 1, 0, -1)` excludes 0, which is fine because no value has frequency 0.

**Ties:** two values with the same frequency land in the same bucket. The problem guarantees a unique answer, so a tie never straddles the cutoff at k.

---

## Edge Cases and Pitfalls

- **Single element** (`[1]`, `k = 1`): count is `{1: 1}`, bucket 1 holds `[1]`, and the function returns `[1]`.
- **All elements equal** (`[5,5,5]`, `k = 1`): frequency 3 goes in bucket 3, which is why `n + 1` buckets are needed.
- **All distinct** (`[1,2,3]`, `k = 3`): everything lands in bucket 1, and the answer is all of them.
- **Negative numbers:** they are only keys in the hash map, never indices, so they cause no problem. Using the value as an array index would be a bug.
- **No explicit return after the loop:** your function falls off the end and returns `None` if `k` values are never collected. The constraints guarantee `k` is at most the number of distinct values, so the early return always fires. Adding `return res` at the end is a safe habit.
- **Stale `res` order:** the output is highest frequency first, but any order is accepted.
- **Heap with a max-heap by mistake:** Python's `heapq` is a min-heap, so keeping the **k largest** needs a size-k min-heap that evicts the smallest, as in approach 2.
- **Style note:** `for i in range(len(nums) + 1)` with an unused `i` is conventionally written `for _ in range(...)`. `list[int]` needs Python 3.9+ (LeetCode's template uses `List[int]`). Your code is otherwise clean.

---

## Interview Follow-Ups

- **"Why is this better than O(n log n)?"** Frequencies are integers in [1, n], so bucketing replaces the comparison sort with direct indexing.
- **"What if k is much smaller than n?"** The heap approach, O(n log k), is simple and uses a tiny heap, so either is reasonable.
- **"What if the data is a stream?"** Keep the count map and a size-k min-heap, updating on each arrival (or use a Count-Min Sketch for approximate counts with bounded memory).
- **"What if the data is too large for memory?"** Hash-partition values into chunks, count each chunk, and merge the per-chunk top-k lists (map-reduce style).
- **"Return the k least frequent?"** Scan the buckets from low to high.
- **"Top k frequent words, sorted with ties broken alphabetically?"** LC 692, using a heap with a custom comparator.
- **"Can you do better than O(n)?"** No, you must read every element.

---

## Related Problems

- **692. Top K Frequent Words:** the same idea with ordering rules
- **215. Kth Largest Element in an Array:** quickselect or heap
- **451. Sort Characters By Frequency:** bucket sort by count
- **973. K Closest Points to Origin:** heap or quickselect
- **703. Kth Largest Element in a Stream:** size-k min-heap
- **295. Find Median from Data Stream:** two heaps
- **49. Group Anagrams:** hash map grouping
- **169. Majority Element:** frequency counting (k = 1 with a threshold)

---
