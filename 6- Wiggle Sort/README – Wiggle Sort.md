# 🌊 Project 6 — Wiggle Sort

## 📖 Description
The **Wiggle Sort** algorithm rearranges an array of integers so that the elements alternate between **smaller and larger values** in the following pattern:

```
nums[0] < nums[1] > nums[2] < nums[3] > nums[4] ...
```

This ensures a "wave-like" order where numbers rise and fall alternately.

It is guaranteed that a valid arrangement always exists.

---

## 🧠 Examples

### Example 1
```
Input:
nums = [1, 5, 1, 1, 6, 4]

Output:
[1, 6, 1, 5, 1, 4]   OR   [1, 4, 1, 5, 1, 6]
```

### Example 2
```
Input:
nums = [1, 3, 2, 2, 3, 1]

Output:
[2, 3, 1, 3, 1, 2]   OR   [1, 3, 2, 3, 1, 2]
```

---

## ⚙️ Input / Output Format

- **Input:**  
  A list of integers (comma-separated), e.g. `1,5,1,1,6,4`

- **Output:**  
  A new list arranged in the wiggle pattern.

---

## 🧩 Algorithm Steps

1. Read input array from the user.  
2. Sort the array in ascending order.  
3. Split it into two halves:
   - `small` → first half (reversed)
   - `large` → second half (reversed)
4. Alternate between elements from both halves:
   - Even indices → take from `small`
   - Odd indices → take from `large`
5. Merge the elements into the **wiggle** pattern.
6. Return and print the final reordered array.

---

## 🧾 Pseudo-code
```text
FUNCTION wiggle_sort(nums)
{
    PRINT "Original array:", nums
    SORT nums
    n := length(nums)
    half := n // 2

    small := reverse(nums[0 : half])
    large := reverse(nums[half : n])

    wiggle := []

    FOR i := 0 TO n - 1 DO
        IF i is even THEN
            IF small not empty THEN
                ADD small[0] TO wiggle
                REMOVE small[0]
        ELSE
            IF large not empty THEN
                ADD large[0] TO wiggle
                REMOVE large[0]
    END FOR

    PRINT "Wiggle Sorted Array:", wiggle
    RETURN wiggle
}
```

---

## 🧮 Time & Space Complexity

| Step | Complexity |
|------|-------------|
| Sorting the array | O(n log n) |
| Splitting & reversing | O(n) |
| Building wiggle pattern | O(n) |
| **Total Time Complexity** | **O(n log n)** |
| **Space Complexity** | **O(n)** |

---

## 💻 Sample Run
```bash
Enter the array elements separated by commas: 1,5,1,1,6,4

Original array: [1, 5, 1, 1, 6, 4]
Sorted array: [1, 1, 1, 4, 5, 6]

Smaller half: [1, 1, 1]
Larger half: [6, 5, 4]

Wiggle Sorted Array: [1, 6, 1, 5, 1, 4]
```

---

## ⚠️ Edge Cases
| Input | Output |
|--------|--------|
| `[1,2,3,4,5,6]` | `[3,6,2,5,1,4]` |
| `[1,1,2,2,3,3]` | `[2,3,1,3,1,2]` |
| `[5]` | `[5]` (single element → unchanged) |

---

## 👨‍💻 Author
- **Name:** Ibrahim Hamdy  
- **Role:** Helwan National University  
- **Email:** ihamdy719@gmail.com
