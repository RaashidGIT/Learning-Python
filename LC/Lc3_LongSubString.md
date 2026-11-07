# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium | **Topics:** Hash Table, String, Sliding Window

**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

## Problem Description

Given a string `s`, find the length of the **longest substring** without repeating characters.

A substring is a contiguous, non-empty sequence of characters within the string.

**Example 1**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Constraints**
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Intuition and Key Insight

Maintain a **window** `[l, r]` that always contains unique characters. Expand it by moving `r` one step at a time. When `s[r]` is already inside the window, shrink from the left until the duplicate is gone, then add `s[r]`. The answer is the largest window size seen.

A set tells you in O(1) whether a character is currently in the window. Each character is added once and removed at most once, so the total work is linear.

**Pattern to recognize:** "longest/shortest contiguous segment satisfying a condition" → sliding window with two pointers and a structure tracking the window's contents.

---

## Approaches

### 1. Brute Force: Check Every Substring

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break                   # duplicate found, stop extending
                seen.add(s[j])
                res = max(res, j - i + 1)
        return res
```

- **Time:** O(n²), for each start `i`, extend until a duplicate appears (the naive version that checks every substring for uniqueness is O(n³))
- **Space:** O(min(n, m)), where m is the alphabet size
- **Verdict:** Passes on LeetCode for n up to 5 x 10^4 in many cases, but it is the baseline to beat. Mention it, then optimize.

### 2. Sliding Window with Set (Your Solution)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()                     # characters currently in the window
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:          # duplicate: shrink from the left
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])               # window is now unique again
            res = max(res, r - l + 1)       # update best window size
        return res
```

- **Time:** O(n), since `l` and `r` each move at most n times, so every character is added and removed at most once
- **Space:** O(min(n, m)), where m is the size of the character set (at most about 128 for ASCII)
- **Verdict:** Optimal in time and the standard interview answer. It is easy to reason about.

### 3. Sliding Window with Hash Map (Jump the Left Pointer, Optimal)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}                      # char -> most recent index
        l = 0
        res = 0

        for r, c in enumerate(s):
            if c in last_seen and last_seen[c] >= l:
                l = last_seen[c] + 1        # jump past the previous occurrence
            last_seen[c] = r
            res = max(res, r - l + 1)
        return res
```

- **Time:** O(n), one pass with no inner `while` loop
- **Space:** O(min(n, m))
- **Verdict:** Same complexity as the set version, but `l` jumps directly instead of creeping one step at a time, so each character is touched once. The `last_seen[c] >= l` check is essential, because the map may hold stale indices from before the window.

### 4. Fixed-Size Array Variant (ASCII Only)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128                   # last index of each ASCII char
        l = 0
        res = 0
        for r, c in enumerate(s):
            idx = ord(c)
            if last[idx] >= l:
                l = last[idx] + 1
            last[idx] = r
            res = max(res, r - l + 1)
        return res
```

- **Time:** O(n)
- **Space:** O(1), since the array has a fixed 128 slots
- **Verdict:** A micro-optimization that avoids hashing. It assumes ASCII, so use 256 or a dict if the input might contain other characters.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute force | O(n²) | O(min(n, m)) | Baseline |
| **Sliding window + set (yours)** | **O(n)** | **O(min(n, m))** | **Optimal, simplest to explain** |
| Sliding window + last-seen map | **O(n)** | O(min(n, m)) | **Optimal, left pointer jumps** |
| Last-seen array (ASCII) | O(n) | O(1) | Fastest in practice |

*Here m is the size of the alphabet.*

---

## Walkthrough (Your Solution)

`s = "abcabcbb"`

| r | s[r] | Duplicate? | Shrink action | Window | charSet | res |
|---|---|---|---|---|---|---|
| 0 | a | No | none | "a" | {a} | 1 |
| 1 | b | No | none | "ab" | {a,b} | 2 |
| 2 | c | No | none | "abc" | {a,b,c} | **3** |
| 3 | a | **Yes** | remove a, `l = 1` | "bca" | {b,c,a} | 3 |
| 4 | b | **Yes** | remove b, `l = 2` | "cab" | {c,a,b} | 3 |
| 5 | c | **Yes** | remove c, `l = 3` | "abc" | {a,b,c} | 3 |
| 6 | b | **Yes** | remove a, b, `l = 5` | "cb" | {c,b} | 3 |
| 7 | b | **Yes** | remove c, b, `l = 7` | "b" | {b} | 3 |

Result: `3`.

---

## Why It Works

At the end of each iteration of the outer loop, the window `s[l..r]` contains no duplicates. The `while` loop removes characters from the left only until `s[r]` is no longer in the set, which gives the **largest** valid window ending at `r` (shrinking more would only lose length). Taking the maximum over all `r` therefore covers the optimal substring, since the optimal substring ends at some `r`.

The window never moves left, and `l` never passes `r`, because once `s[r]` has been removed from the set the loop stops.

---

## Edge Cases and Pitfalls

- **Empty string** (`""`): the loop doesn't run and the answer is `0`.
- **Single character** (`"a"`): answer is `1`.
- **All identical** (`"bbbbb"`): answer is `1`.
- **All unique** (`"abcdef"`): the whole string, answer is `6`.
- **Substring vs subsequence:** `"pwwkew"` gives `3` (`"wke"`), not `4`. The characters must be contiguous.
- **Spaces and symbols count** as characters, so don't strip them.
- **Update `res` after adding `s[r]`**, so the window size includes the current character: `r - l + 1`.
- **Stale indices in the map version:** without the `last_seen[c] >= l` check, a character seen long before the window would wrongly pull `l` backward. For `"abba"`, this check is what prevents the bug at the final `a`.
- **Use `while`, not `if`,** in the set version. A single removal is not always enough, as the `"abcabcbb"` row at `r = 6` shows.
- **Style note:** your code is correct and clean. The only nitpick is that `charSet` is a clear name, but in an interview you could also call it `window` to reinforce the sliding window idea.

---

## Interview Follow-Ups

- **"Can you avoid the inner `while` loop?"** Yes, store each character's last index and jump `l` directly (approach 3).
- **"Return the substring itself, not just its length."** Track `start = l` whenever `res` improves, then return `s[start:start + res]`.
- **"What if at most k distinct characters are allowed?"** Use a hash map of counts and shrink while the number of distinct keys exceeds k (LC 340).
- **"What if at most two distinct characters?"** The same as above with k = 2 (LC 159).
- **"What if the input is a stream?"** The last-seen map version works, since it only needs the current window state.
- **"What about Unicode?"** Use a dict instead of a fixed array. Be aware of surrogate pairs and combining characters in other languages.
- **"Can you do better than O(n)?"** No, you must read every character at least once.

---

## Related Problems

- **159. Longest Substring with At Most Two Distinct Characters:** sliding window with counts
- **340. Longest Substring with At Most K Distinct Characters:** same, generalized
- **424. Longest Repeating Character Replacement:** sliding window with a max-frequency count
- **438. Find All Anagrams in a String:** fixed-size sliding window
- **567. Permutation in String:** fixed-size sliding window
- **76. Minimum Window Substring:** variable window with required counts
- **209. Minimum Size Subarray Sum:** variable window over numbers
- **121. Best Time to Buy and Sell Stock:** two pointers in a similar style

---

Your solution is correct and optimal. Send the next problem, or ask for the C++ version of 3. With 1, 3, 11, 49, 53, 121, 217 and 238 covered, I can also merge everything into a single study document whenever you like.
