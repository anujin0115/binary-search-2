# Binary Search 2


PDF: https://drive.google.com/file/d/14bB72Mvr2QaOCf2f6r3CLbhEHWTM7GuC/view?usp=sharing

- Every exercise must use **binary search**.
  
---

## Exercise 1

**Problem:**

`data` is a **sorted** list with at least one number in it. `target` may or may
not be in the list.

Return the **value** (not the index) in `data` that is closest to `target`.
If two values are equally close, return the **smaller** one.

*Hint:* binary search down to the position where `target` would fit, then
compare only the two neighbours around that spot.

**Example:**

    Example Input:
        data   = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        target = 13

    Program Output:
        12          # 12 is 1 away, 16 is 3 away

    Example Input:
        target = 14

    Program Output:
        12          # both are 2 away, so return the smaller one

    Example Input:
        target = 100

    Program Output:
        91          # past the end of the list

---

## Exercise 2

**Problem:**

`integer_sqrt(n)`

`n` is a whole number, `0` or bigger. Return the **largest whole number** `r`
such that `r * r` is less than or equal to `n`.

There is no list in this problem. You are searching the **range of possible
answers**: the answer is somewhere between `0` and `n`, so binary search that
range instead of a list.

*Hint:* guess `mid`. If `mid * mid <= n`, then `mid` is a possible answer —
remember it and try bigger. Otherwise `mid` is too big, so try smaller.

**Example:**

    Example Input:
        n = 16

    Program Output:
        4           # 4 * 4 = 16

    Example Input:
        n = 24

    Program Output:
        4           # 4*4 = 16 fits, 5*5 = 25 is too big

    Example Input:
        n = 0

    Program Output:
        0

Your program must answer `integer_sqrt(10000000000000000)` instantly.
Counting upwards from 0 would take about 100,000,000 steps — binary search
takes about 54.

---
