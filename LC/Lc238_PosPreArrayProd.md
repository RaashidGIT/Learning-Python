# 238. Product of Array Except Self

**Difficulty:** Medium | **Topics:** Array, Prefix Sum

**Link:** https://leetcode.com/problems/product-of-array-except-self/

---

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` **except** `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a 32-bit integer.

You must write an algorithm that runs in **O(n) time** and **without using the division operation**.

**Example 1**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints**
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` fits in a 32-bit integer.

**Follow-up:** Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

---

## Intuition and Key Insight

The product of everything except `nums[i]` splits into two independent parts:

```
answer[i] = (product of everything to the LEFT of i) x (product of everything to the RIGHT of i)
```

Each part is a running product, so both can be computed in a single sweep: one left to right (prefix), one right to left (suffix). Division would be the obvious shortcut (total product divided by `nums[i]`), but it is banned, and it also breaks on zeros.

Your solution does this in two passes and reuses the output array to store the prefix products, so no extra arrays are needed. That is the O(1) extra space follow-up.

**Pattern to recognize:** "result at i depends on everything except i" → prefix and suffix aggregates, combined at each index.

---

## Approaches

### 1. Brute Force: Multiply Everything Except i

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if j != i:
                    prod *= nums[j]
            res.append(prod)
        return res
```

- **Time:** O(n²)
- **Space:** O(1) extra (output excluded)
- **Verdict:** With n up to 10^5 this is about 10^10 operations, so it will time out. It also violates the O(n) requirement. Mention it as the baseline.

### 2. Division (Rejected by the Problem)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total, zeros = 1, 0
        for x in nums:
            if x == 0:
                zeros += 1
            else:
                total *= x
        if zeros > 1:
            return [0] * len(nums)
        if zeros == 1:
            return [0 if x != 0 else total for x in nums]
        return [total // x for x in nums]
```

- **Time:** O(n)
- **Space:** O(1) extra
- **Verdict:** Not allowed, because the problem forbids division. It is still worth knowing because interviewers often start here and then ask you to remove division. The zero handling is the tricky part: two or more zeros make everything 0, and exactly one zero makes every position 0 except the zero's own position.

### 3. Prefix and Suffix Arrays (O(n) Extra Space)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n          # prefix[i] = product of nums[0..i-1]
        suffix = [1] * n          # suffix[i] = product of nums[i+1..n-1]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i] * suffix[i] for i in range(n)]
```

- **Time:** O(n)
- **Space:** O(n) extra, for two helper arrays
- **Verdict:** The clearest version to explain and a good first answer in an interview. Then optimize it to approach 4.

### 4. Prefix and Postfix with Output Array Reuse (Your Solution, Optimal)

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix           # product of everything left of i
            prefix *= nums[i]         # extend prefix to include nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix         # multiply in product of everything right of i
            postfix *= nums[i]        # extend postfix to include nums[i]
        return res
```

- **Time:** O(n), two passes
- **Space:** O(1) extra (the output array is not counted)
- **Verdict:** Optimal, and it satisfies the follow-up. The two running variables replace the two helper arrays from approach 3.

---

## Complexity Summary

| Approach | Time | Space (extra) | Notes |
|---|---|---|---|
| Brute force | O(n²) | O(1) | TLE |
| Division | O(n) | O(1) | Not allowed, zero handling is tricky |
| Prefix + suffix arrays | O(n) | O(n) | Clearest to explain |
| **Prefix + postfix, reuse output (yours)** | **O(n)** | **O(1)** | **Optimal, meets the follow-up** |

---

## Walkthrough (Your Solution)

`nums = [1, 2, 3, 4]`

**Pass 1 (left to right):** write the product of everything to the left.

| i | nums[i] | res[i] = prefix | prefix after |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 1 | 2 | 1 | 2 |
| 2 | 3 | 2 | 6 |
| 3 | 4 | 6 | 24 |

`res = [1, 1, 2, 6]`

**Pass 2 (right to left):** multiply in the product of everything to the right.

| i | nums[i] | res[i] before | postfix used | res[i] after | postfix after |
|---|---|---|---|---|---|
| 3 | 4 | 6 | 1 | 6 | 4 |
| 2 | 3 | 2 | 4 | 8 | 12 |
| 1 | 2 | 1 | 12 | 12 | 24 |
| 0 | 1 | 1 | 24 | 24 | 24 |

`res = [24, 12, 8, 6]`

---

Here is the line-by-line breakdown:

class Solution:
Defines the class containing the method, standard for LeetCode problems.

def productExceptSelf(self, nums: list[int]) -> list[int]:
Defines the function that takes a list of integers (nums) and returns a new list of integers.

res = [1] * (len(nums))
Creates the result array res, initialized with 1s, completely matching the length of the input array.

prefix = 1
Initializes a running multiplier for the "left side" (prefix) product. It starts at 1 because there are no elements to the left of the first item.

for i in range(len(nums)):
Starts a forward loop to iterate through every index from left to right.

res[i] = prefix
Sets the current position in res to the product of all elements that came before index i.

prefix *= nums[i]
Updates the running prefix product by multiplying it by the current element, so the next index will include this number in its left-side product.

postfix = 1
Initializes a running multiplier for the "right side" (postfix) product. It starts at 1 because there are no elements to the right of the last item.

for i in range(len(nums) - 1, -1, -1):
Starts a backward loop from the last index (len(nums) - 1) down to 0.

res[i] *= postfix
Multiplies the existing value in res[i] (which currently holds the left-side product) by the postfix (the right-side product). This gives the final answer for that index.

postfix *= nums[i]
Updates the running postfix product by multiplying it by the current element, so the next index (moving leftwards) will include this number in its right-side product.

return res
Returns the fully populated result array.

---

Here is the step-by-step execution for nums = [1, 2, 3, 4].

Initial Setup

nums = [1, 2, 3, 4]

res = [1, 1, 1, 1] (Initialized to 1s matching the length of nums)

1. Forward Loop (Prefix Pass)
We track the product of all numbers to the left of the current index.

prefix = 1

i = 0 (nums[0] = 1)

res[0] = prefix ➔ res becomes [1, 1, 1, 1]

prefix = prefix * nums[0] ➔ 1 * 1 = 1

i = 1 (nums[1] = 2)

res[1] = prefix ➔ res becomes [1, 1, 1, 1]

prefix = prefix * nums[1] ➔ 1 * 2 = 2

i = 2 (nums[2] = 3)

res[2] = prefix ➔ res becomes [1, 1, 2, 1]

prefix = prefix * nums[2] ➔ 2 * 3 = 6

i = 3 (nums[3] = 4)

res[3] = prefix ➔ res becomes [1, 1, 2, 6]

prefix = prefix * nums[3] ➔ 6 * 4 = 24

State of res after the first loop: [1, 1, 2, 6]

2. Backward Loop (Postfix Pass)
We track the product of all numbers to the right of the current index and multiply it with the existing res value.

postfix = 1

i = 3 (nums[3] = 4)

res[3] = res[3] * postfix ➔ 6 * 1 = 6 ➔ res remains [1, 1, 2, 6]

postfix = postfix * nums[3] ➔ 1 * 4 = 4

i = 2 (nums[2] = 3)

res[2] = res[2] * postfix ➔ 2 * 4 = 8 ➔ res becomes [1, 1, 8, 6]

postfix = postfix * nums[2] ➔ 4 * 3 = 12

i = 1 (nums[1] = 2)

res[1] = res[1] * postfix ➔ 1 * 12 = 12 ➔ res becomes [1, 12, 8, 6]

postfix = postfix * nums[1] ➔ 12 * 2 = 24

i = 0 (nums[0] = 1)

res[0] = res[0] * postfix ➔ 1 * 24 = 24 ➔ res becomes [24, 12, 8, 6]

postfix = postfix * nums[0] ➔ 24 * 1 = 24

Final Result
The function returns [24, 12, 8, 6].

---

## Why It Works

After pass 1, `res[i]` holds the product of all elements strictly left of `i`. In pass 2, `postfix` holds the product of all elements strictly right of `i` at the moment it is applied, because it is multiplied in *before* `nums[i]` is folded into it. So `res[i]` ends up as left product x right product, which excludes `nums[i]` itself.

The order of operations inside each loop matters. Read or write first, then update the running product.

---

## Edge Cases and Pitfalls

- **One zero** (`[-1,1,0,-3,3]`): only the position of the zero gets a non-zero result (here `9`), and every other position is `0`. The prefix/postfix method handles this with no special case, unlike the division approach.
- **Two or more zeros:** every result is `0`.
- **Length 2** (`[a, b]`): result is `[b, a]`.
- **Negative numbers:** signs work out naturally.
- **Updating the running product before using it:** if you did `prefix *= nums[i]` before `res[i] = prefix`, you would include `nums[i]` itself. Use first, then update.
- **Counting the output as extra space:** the problem explicitly excludes it. Say so in an interview to make the O(1) claim clear.
- **Overflow:** not a concern in Python. In C++ the guarantee that prefix and suffix products fit in 32 bits means `int` is safe, but the *full* product may not fit, which is another reason the division trick is risky.
- **Style note on your code:** `len(nums)` in `[1] * (len(nums))` has redundant parentheses, and `list[int]` needs Python 3.9+ (LeetCode's template uses `List[int]`). Neither affects correctness.

---

## Interview Follow-Ups

- **"Can you do it without division?"** Yes, that is the prefix/postfix method.
- **"Can you use O(1) extra space?"** Reuse the output array, as your solution does.
- **"What if division were allowed?"** Compute the total product and divide, handling zeros separately as in approach 2.
- **"What if the result must be modulo a prime?"** Division then needs modular inverses, which don't exist for 0 and fail when the modulus divides an element, so prefix/suffix is the safer approach.
- **"What if the array is huge or arrives in chunks?"** Compute per-chunk products and combine prefix and suffix across chunks, which parallelizes well.
- **"Can you do it in one pass?"** Not in a single sweep, since each position needs information from both sides. Two sweeps is the practical minimum.

---

## Related Problems

- **42. Trapping Rain Water:** prefix max and suffix max arrays, the same left/right structure
- **135. Candy:** left pass and right pass over the array
- **152. Maximum Product Subarray:** product tracking with sign flips
- **724. Find Pivot Index:** prefix sum compared with suffix sum
- **560. Subarray Sum Equals K:** prefix sums with a hash map
- **1352. Product of the Last K Numbers:** prefix product design problem
- **53. Maximum Subarray:** another one-pass running-value pattern

---

Your solution is correct and optimal. Send the next problem, or ask for the C++ version of 238. Once you have a few more done, I can combine everything into one study document.
