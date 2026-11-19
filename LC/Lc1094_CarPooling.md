# 1094. Car Pooling

**Difficulty:** Medium | **Topics:** Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum

**Link:** https://leetcode.com/problems/car-pooling/

---

## Problem Description

There is a car with `capacity` empty seats. The vehicle only drives **east** (it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengers_i, from_i, to_i]` indicates that the i-th trip has `numPassengers_i` passengers, and the locations to pick them up and drop them off are `from_i` and `to_i` respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or `false` otherwise.

**Example 1**
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

**Example 2**
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

**Constraints**
- `1 <= trips.length <= 1000`
- `trips[i].length == 3`
- `1 <= numPassengers_i <= 100`
- `0 <= from_i < to_i <= 1000`
- `1 <= capacity <= 10^5`

---

## Intuition and Key Insight

The only question is: **at any point on the road, are there ever more than `capacity` passengers in the car?** Each trip adds passengers at `from` and removes them at `to`. Passengers who get off at a location free their seats **before** new ones board at that same location, so a trip occupying `[from, to)` is a half-open interval.

There are two natural ways to track the load:
- **Event simulation:** process pickups in order of location, and use a min-heap keyed by drop-off point to remove passengers who have already left (your first solution).
- **Difference array (sweep line):** record `+n` at `from` and `-n` at `to`, then take a running sum across the road (your second solution). Because locations are at most 1000, a fixed array works.

**Pattern to recognize:** "overlapping intervals with weights, is the maximum overlap within a limit" → sweep line or difference array, or sort plus a min-heap of end times. The same family covers Meeting Rooms II and My Calendar III.

---

## Approaches

### 1. Brute Force: Check the Load at Every Location

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for loc in range(1001):
            load = 0
            for num, start, end in trips:
                if start <= loc < end:              # trip is on board at loc
                    load += num
            if load > capacity:
                return False
        return True
```

- **Time:** O(n x L), where n is the number of trips and L = 1001 is the number of locations
- **Space:** O(1)
- **Verdict:** About 10^6 operations here, which passes. It is the baseline that shows the question being asked. The two solutions below remove the inner scan.

### 2. Sort + Min-Heap (Your First Solution)

```python
import heapq

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])              # process pickups in order of start

        minHeap = []                                # (end, numPassengers) of trips on board
        curPass = 0
        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:   # drop off everyone who has arrived
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)

            curPass += numPass                      # pick up the new passengers
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True
```

- **Time:** O(n log n), for the sort plus n heap pushes and pops
- **Space:** O(n) for the heap
- **Verdict:** Correct, and the general-purpose version. It works for any coordinate range, including huge or non-integer locations, because it only looks at the trips themselves.

### 3. Difference Array / Sweep Line (Your Second Solution, Optimal for These Constraints)

```python
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        passChange = [0] * 1001                     # net passenger change at each location

        for numPass, start, end in trips:
            passChange[start] += numPass            # pick up
            passChange[end] -= numPass              # drop off

        curPass = 0
        for i in range(1001):
            curPass += passChange[i]                # running load after events at i
            if curPass > capacity:
                return False
        return True
```

- **Time:** O(n + L), where L = 1001 is the coordinate range
- **Space:** O(L)
- **Verdict:** Optimal here, and the simplest to code. Both the pickup and drop-off at the same location are folded into one net change, so the "drop before pickup" rule happens automatically.

### 4. Sort Events (Sweep Line Without a Fixed Range)

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, start, end in trips:
            events.append((start, num))             # +num at pickup
            events.append((end, -num))              # -num at drop-off

        events.sort()                               # ties: negative deltas sort first
        load = 0
        for _, delta in events:
            load += delta
            if load > capacity:
                return False
        return True
```

- **Time:** O(n log n)
- **Space:** O(n)
- **Verdict:** Same idea as the difference array without needing a bounded range. Sorting tuples puts `-num` before `+num` at the same location, which is exactly the "drop off before pickup" order we need.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n x L) | O(1) | Baseline, passes here |
| **Sort + min-heap (yours)** | **O(n log n)** | **O(n)** | **General, no range assumption** |
| **Difference array (yours)** | **O(n + L)** | **O(L)** | **Optimal here, simplest** |
| Sorted events | O(n log n) | O(n) | General sweep line |

*Here n = number of trips and L = coordinate range (1001).*

---

## Walkthrough (Difference Array)

`trips = [[2,1,5],[3,3,7]]`, `capacity = 4`

Build `passChange`:

| Location | 1 | 3 | 5 | 7 |
|---|---|---|---|---|
| Change | +2 | +3 | -2 | -3 |

Sweep with a running load:

| i | passChange[i] | curPass | > 4? |
|---|---|---|---|
| 0 | 0 | 0 | No |
| 1 | +2 | 2 | No |
| 2 | 0 | 2 | No |
| 3 | +3 | **5** | **Yes, return False** |

With `capacity = 5` the load peaks at exactly 5 and never exceeds it, so the answer is `True`.

## Walkthrough (Heap)

`trips = [[2,1,5],[3,3,7]]`, `capacity = 4` (already sorted by start)

| Trip | Heap before | Popped? | curPass after pickup | Result |
|---|---|---|---|---|
| [2,1,5] | empty | none | 2 | push (5, 2) |
| [3,3,7] | (5,2) | 5 <= 3? No | 5 | 5 > 4, **return False** |

---

## Why It Works

**Difference array:** after adding `+n` at `from` and `-n` at `to`, the prefix sum at location `i` equals the total passengers whose trip satisfies `from <= i < to`. That is exactly the number of people in the car after all events at `i`. The load can only increase at a pickup point, so checking it after every location covers the maximum.

**Heap:** trips are processed in order of start, so at each pickup the heap holds exactly the trips still on board. Before adding the new group, everyone whose `end <= start` is removed. Then the load is what is in the car at that pickup, and that is the only place the load can rise.

**The `<=` in the heap condition:** a passenger with `end == start` of the new trip has already left, so their seat is free. Using `<` instead would wrongly keep them on board.

---

## Edge Cases and Pitfalls

- **Drop-off and pickup at the same location** (`[[3,0,5],[3,5,8]]`, capacity 3): answer is `True`. The heap must use `<=`, and the difference array handles it automatically by netting the changes.
- **Single trip over capacity** (`[[9,0,1]]`, capacity 8): `False`.
- **Single trip within capacity:** `True`.
- **Trips that never overlap:** the load never accumulates, so `True`.
- **Locations up to 1000 inclusive:** the array must have size **1001**, not 1000. A drop-off at location 1000 would raise an `IndexError` with a size-1000 array.
- **Check the load after every location in the difference array,** not only at the end, since the peak can be in the middle.
- **Early return inside the loop:** the heap version checks the capacity right after each pickup, which is the only moment the load can increase.
- **Missing import:** `heapq` needs `import heapq`. LeetCode adds it for you, but add it in your own environment or an interview.
- **Mutating the input:** the heap version sorts `trips` in place. Copy first if that matters.
- **Style note:** your code is correct. In the heap version, `minHeap [0][0]` has a stray space before the bracket, `heapq.heappop(minHeap)` can be combined with the read as `_, n = heapq.heappop(minHeap)`, and the `//` line and the two classes sharing one cell would need to be separated before submitting. `list[list[int]]` needs Python 3.9+ (LeetCode's template uses `List[List[int]]`).

---

## Interview Follow-Ups

- **"What if locations can be up to 10^9?"** The fixed array no longer fits. Use sorted events (approach 4) or the heap, both O(n log n), or coordinate compression.
- **"Which would you choose and why?"** The difference array here, because the range is only 1001 and it is simplest. The heap or sorted events if the range is large relative to n.
- **"What if the car can turn around, or has multiple stops in any order?"** It becomes a routing problem and is no longer an interval question.
- **"Return the location where the capacity is first exceeded."** In the sweep, return the index `i` at the first violation.
- **"What if passengers can be partially dropped or trips have priority?"** Track per-trip state in the heap and decide whom to remove.
- **"Count the maximum load at any time."** Return the maximum of the running sum (the Meeting Rooms II pattern, LC 253).
- **"Can you do better than O(n)?"** No, you must read every trip at least once.

---

## Related Problems

- **253. Meeting Rooms II:** maximum overlap using a heap or sweep line
- **252. Meeting Rooms:** detect any overlap
- **731. My Calendar II:** triple-booking check with a sweep or difference map
- **732. My Calendar III:** maximum overlap over time
- **1109. Corporate Flight Bookings:** difference array, the same technique
- **370. Range Addition:** difference array
- **435. Non-overlapping Intervals:** interval greedy with sorting
- **56. Merge Intervals:** sorting by start
- **218. The Skyline Problem:** sweep line with a heap

---
