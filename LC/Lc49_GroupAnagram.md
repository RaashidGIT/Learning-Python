# 49. Group Anagrams

**Difficulty:** Medium | **Topics:** Array, Hash Table, String, Sorting

**Link:** https://leetcode.com/problems/group-anagrams/

---

## Problem Description

Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.

An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.

**Example 1**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
- There is no string in strs that can be rearranged to form "bat".
- "nat" and "tan" are anagrams, as they can be rearranged to form each other.
- "ate", "eat", and "tea" are anagrams, as they can be rearranged to form each other.
```

**Example 2**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3**
```
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints**
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Intuition and Key Insight

Two strings are anagrams exactly when they have the same **letter counts**. So if you can compute a **canonical key** that is identical for every anagram of a word, you can drop each word into a hash map under its key and read off the groups at the end.

There are two standard keys:
- **Sorted string:** `"eat"`, `"tea"` and `"ate"` all become `"aet"`. Cost is O(k log k) per word.
- **Character count tuple:** a 26-slot frequency array, converted to a tuple so it is hashable. Cost is O(k) per word. This is what your solution does.

**Pattern to recognize:** "group items that are equivalent under some rearrangement" → compute a canonical form and use it as a hash map key.

---

## Approaches

### 1. Brute Force: Compare Every Pair

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        used = [False] * len(strs)
        res = []
        for i in range(len(strs)):
            if used[i]:
                continue
            group = [strs[i]]
            used[i] = True
            for j in range(i + 1, len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    used[j] = True
            res.append(group)
        return res
```

- **Time:** O(n² x k log k), where n is the number of strings and k is the max string length
- **Space:** O(n x k) for the output
- **Verdict:** Works but is wasteful, since it compares strings pairwise instead of hashing them to a shared key. Mention it as the baseline, then optimize.

### 2. Hash Map with Sorted String as Key

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))        # all anagrams share this key
            groups[key].append(s)
        return list(groups.values())
```

- **Time:** O(n x k log k), since each word is sorted
- **Space:** O(n x k) for the map and output
- **Verdict:** The shortest and most readable solution, and usually the first one to write in an interview. The log factor on k is tiny because k is at most 100.

### 3. Hash Map with Character Count Key (Your Solution, Optimal)

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)             # count tuple -> list of anagrams

        for s in strs:
            count = [0] * 26                # one slot per letter a..z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)     # lists aren't hashable, so convert to tuple

        return list(res.values())
```

- **Time:** O(n x k), where n is the number of strings and k is the average (or max) string length. Each word costs O(k) to count, plus O(26) to build the tuple key.
- **Space:** O(n x k) for the output, plus O(n x 26) for the keys
- **Verdict:** Optimal. It beats sorting by a log factor on k and is the answer interviewers usually want for the "can you do better than sorting?" follow-up.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n² x k log k) | O(n x k) | Pairwise comparison, slow |
| Sorted string key | O(n x k log k) | O(n x k) | Shortest code, easy to explain |
| **Count tuple key (yours)** | **O(n x k)** | **O(n x k)** | **Optimal, avoids sorting** |

*Here n = number of strings and k = maximum string length.*

---

## Walkthrough (Your Solution)

`strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

| s | Count key (only non-zero shown) | Map after |
|---|---|---|
| "eat" | a1 e1 t1 | {a1e1t1: ["eat"]} |
| "tea" | a1 e1 t1 | {a1e1t1: ["eat","tea"]} |
| "tan" | a1 n1 t1 | {..., a1n1t1: ["tan"]} |
| "ate" | a1 e1 t1 | {a1e1t1: ["eat","tea","ate"], ...} |
| "nat" | a1 n1 t1 | {..., a1n1t1: ["tan","nat"]} |
| "bat" | a1 b1 t1 | {..., a1b1t1: ["bat"]} |

Result: `[["eat","tea","ate"], ["tan","nat"], ["bat"]]` (group order may vary).

The real key is a 26-length tuple such as `(1,0,0,0,1,0,...,1,0,0,0,0,0)`, and the table above shows only its non-zero entries for readability.

---

## Why It Works

Two strings are anagrams if and only if their letter-frequency vectors are equal. A tuple of the 26 counts is an exact fingerprint of that vector, so equal tuples mean anagrams and different tuples mean non-anagrams. There are no false positives (unlike a hash of the characters' sum, which can collide).

---

## Edge Cases and Pitfalls

- **Empty string** (`[""]`): the count is all zeros, so it gets its own group. Result is `[[""]]`. Multiple empty strings group together.
- **Single string:** returns a single group containing it.
- **No anagrams:** every word is its own group.
- **All identical words:** one group containing all of them.
- **Lists can't be dict keys.** Use `tuple(count)`. Using `count` directly raises `TypeError: unhashable type: 'list'`.
- **Missing import:** `defaultdict` needs `from collections import defaultdict`. LeetCode adds it for you, but add it in your own environment or an interview.
- **Lowercase only:** the `ord(c) - ord("a")` indexing relies on the constraint that all letters are `a` to `z`. For uppercase, digits or Unicode, switch to a `Counter` or a `dict`-based key (for example `tuple(sorted(Counter(s).items()))`) or use the sorted string.
- **Bad keys:** using `sum(ord(c) for c in s)` as a key is wrong, because different words can share a sum (for example `"ad"` and `"bc"`).
- **Style note on your code:** `list[str]` annotations need Python 3.9+ (LeetCode's template uses `List[str]`), and `res` is a slightly vague name for a map. `groups` communicates better in an interview. Neither affects correctness.

---

## Interview Follow-Ups

- **"Can you do better than sorting each word?"** Yes, use the 26-count tuple key, as in your solution.
- **"What if the strings contain Unicode or uppercase letters?"** Use a `Counter` based key, or the sorted string key, since the fixed 26 slot array no longer applies.
- **"What if the dataset is too large for memory?"** Hash each word's key to a bucket, spill buckets to disk, and group each bucket independently, which is a map-reduce style approach.
- **"What if words arrive as a stream?"** Keep the hash map and append to a group as each word arrives. Each insertion is O(k).
- **"Could you shrink the key?"** Encode the counts as a string like `"#1#0#0..."`, or use a prime-product hash, though prime products overflow in fixed-width languages and need big integers.
- **"Return groups sorted?"** Sort each group, and optionally sort the groups, adding O(n x k log n) or so.

---

## Related Problems

- **242. Valid Anagram:** the single-pair version of the same idea
- **438. Find All Anagrams in a String:** sliding window with a frequency count
- **567. Permutation in String:** sliding window with a frequency count
- **760. Find Anagram Mappings:** value to index mapping
- **2273. Find Resultant Array After Removing Anagrams:** adjacent anagram check
- **205. Isomorphic Strings:** canonical form or pattern mapping
- **890. Find and Replace Pattern:** canonical pattern as key
- **1. Two Sum:** the same hash map lookup mindset

---
