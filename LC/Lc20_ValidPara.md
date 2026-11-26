# 20. Valid Parentheses

**Difficulty:** Easy | **Topics:** String, Stack

**Link:** https://leetcode.com/problems/valid-parentheses/

---

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is **valid**.

An input string is valid if:
1. Open brackets must be closed by the **same type** of bracket.
2. Open brackets must be closed in the **correct order**.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1**
```
Input: s = "()"
Output: true
```

**Example 2**
```
Input: s = "()[]{}"
Output: true
```

**Example 3**
```
Input: s = "(]"
Output: false
```

**Example 4**
```
Input: s = "([])"
Output: true
```

**Constraints**
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only: `'()[]{}'`

---

## Intuition and Key Insight

Brackets nest like a stack of plates: the **most recently opened** bracket must be the **first one closed**. That is last-in, first-out, so a stack is the natural structure.

- On an **open** bracket, push it.
- On a **close** bracket, the top of the stack must be its matching opener. If so, pop it. If the stack is empty or the top is a different type, the string is invalid.
- At the end, the stack must be **empty**, otherwise some opener was never closed.

**Pattern to recognize:** "matching or nested pairs, most recent first" → stack.

---

## Approaches

### 1. Brute Force: Repeatedly Remove Matched Pairs

```python
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""
```

- **Time:** O(n²), since each pass is O(n) and up to n / 2 passes may be needed (for example `"((((....))))"`)
- **Space:** O(n) for the new strings
- **Verdict:** Cute and correct, but quadratic. Mention it as the baseline, then move to the stack.

### 2. Stack with a Close-to-Open Map (Your Solution, Optimal)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:                        # c is a closing bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()                         # matched, discard the opener
                else:
                    return False                        # empty stack or wrong type
            else:
                stack.append(c)                         # c is an opening bracket

        return True if not stack else False             # leftover openers mean invalid
```

- **Time:** O(n), one pass with O(1) work per character
- **Space:** O(n) in the worst case (for example all openers)
- **Verdict:** Optimal and the expected interview answer. The final line can be shortened to `return not stack`.

### 3. Stack Pushing the Expected Closer

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in openToClose:
                stack.append(openToClose[c])            # push what we expect to see later
            elif not stack or stack.pop() != c:
                return False
        return not stack
```

- **Time:** O(n)
- **Space:** O(n)
- **Verdict:** A compact variant. Instead of comparing against the opener, you push the closer you are waiting for, so each closing character is simply compared with what `pop()` returns. Note that `stack.pop() != c` pops as a side effect, which is fine because a mismatch returns immediately.

### 4. Early Exit on Odd Length (Minor Optimization)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:                                  # odd length can never pair up
            return False
        # ... then the stack solution above
```

- **Time:** O(n)
- **Space:** O(n)
- **Verdict:** A cheap check that rejects half of all inputs instantly. It is worth mentioning, but not required.

---

## Complexity Summary

| Approach | Time | Space | Notes |
|---|---|---|---|
| Repeated replace | O(n²) | O(n) | Baseline |
| **Stack + close-to-open map (yours)** | **O(n)** | **O(n)** | **Optimal, standard** |
| Stack of expected closers | O(n) | O(n) | Compact variant |

---

## Walkthrough (Your Solution)

`s = "([{}])"`

| c | Type | Stack before | Action | Stack after |
|---|---|---|---|---|
| ( | open | [] | push | [ ( ] |
| [ | open | [ ( ] | push | [ (, [ ] |
| { | open | [ (, [ ] | push | [ (, [, { ] |
| } | close | [ (, [, { ] | top `{` matches, pop | [ (, [ ] |
| ] | close | [ (, [ ] | top `[` matches, pop | [ ( ] |
| ) | close | [ ( ] | top `(` matches, pop | [] |

Stack is empty at the end, so the answer is `True`.

Failing cases:
- `"(]"`: at `]` the top is `(`, which is not `[`, so return `False`.
- `"(("`: the loop finishes with `[ (, ( ]` left, so return `False`.
- `"))"`: the first `)` finds an empty stack, so return `False`.

---

## Why It Works

At any moment the stack holds exactly the openers that are still waiting to be closed, in the order they were opened. A valid string requires each closer to match the **innermost** unclosed opener, which is the top of the stack. So the check at each closer is both necessary and sufficient. The final empty-stack check catches openers that never found a closer.

---

## Edge Cases and Pitfalls

- **Closer with an empty stack** (`")"`): must return `False`. This is why `stack and ...` is checked before indexing `stack[-1]`, which would raise an `IndexError` on an empty list.
- **Leftover openers** (`"(("`): the loop ends normally, so the final empty check is essential.
- **Right count, wrong order** (`")("`): same number of each, still invalid, because the closer comes first.
- **Right count, wrong type** (`"([)]"`): invalid because the `)` meets `[` on top of the stack.
- **Odd length:** always invalid.
- **Single character:** always invalid, because it is either an unmatched opener or closer.
- **Only counting each bracket type:** a counter per type fails on `"([)]"`. Order matters, so you need a stack.
- **Style note:** `return True if not stack else False` works, but `return not stack` is the idiomatic form. `closeToOpen` is a clear name, and the logic is clean.

---

## Interview Follow-Ups

- **"Only one bracket type?"** A single counter is enough. Increment on `(`, decrement on `)`, fail if it goes negative, and require 0 at the end (O(1) space).
- **"Return the index of the first error?"** Push indices alongside the brackets, and return the index of the failing closer or the bottom-most leftover opener.
- **"Minimum insertions or removals to make it valid?"** Track unmatched closers and leftover openers (LC 921, LC 1249).
- **"Longest valid substring?"** Stack of indices or DP (LC 32).
- **"What if other characters can appear?"** Ignore characters that are not brackets.
- **"Generate all valid strings?"** Backtracking, LC 22.
- **"Can you do better than O(n) space?"** Not for multiple bracket types in general. With one type, a counter gives O(1).

---

## Related Problems

- **22. Generate Parentheses:** generate all valid strings
- **32. Longest Valid Parentheses:** longest valid substring
- **921. Minimum Add to Make Parentheses Valid:** counting
- **1249. Minimum Remove to Make Valid Parentheses:** stack of indices
- **678. Valid Parenthesis String:** with wildcards, greedy range
- **301. Remove Invalid Parentheses:** BFS or backtracking
- **150. Evaluate Reverse Polish Notation:** stack evaluation
- **739. Daily Temperatures:** monotonic stack
- **155. Min Stack:** stack design

---
