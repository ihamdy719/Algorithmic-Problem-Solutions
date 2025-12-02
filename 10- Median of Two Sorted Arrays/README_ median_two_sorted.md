# 🔢 Project 10 — Median of Two Sorted Arrays

## 📖 Description
Given **two sorted arrays** `nums1` and `nums2` of size `m` and `n` respectively, the task is to **return the median** of the merged sorted array.

**Constraints:**
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

## 🧠 Examples

### Example 1
```
Input:
nums1 = [1, 3]
nums2 = [2]
Output: 2
```

### Example 2
```
Input:
nums1 = [1, 2]
nums2 = [3, 4]
Output: 2.5
```

---

## ⚙️ Input / Output Format

- **Input:**
  - Two space-separated sorted arrays  

- **Output:**
  - Median value of the combined array

---

## 🧩 Algorithm Steps

1. Read both sorted arrays from the user.  
2. Merge the arrays in sorted order.  
3. Calculate the length of the merged array.  
4. Determine the median:
   - If the total length is odd → median is the middle element.
   - If even → median is the average of the two middle elements.
5. Return and print the median.

---

## 🧾 Pseudo-code
```text
FUNCTION merge_sorted_arrays(arr1, arr2)
{
    merged := []
    i := 0
    j := 0

    WHILE i < length(arr1) AND j < length(arr2) DO
        IF arr1[i] < arr2[j] THEN
            APPEND arr1[i] TO merged
            i := i + 1
        ELSE
            APPEND arr2[j] TO merged
            j := j + 1
    END WHILE

    WHILE i < length(arr1) DO
        APPEND arr1[i] TO merged
        i := i + 1

    WHILE j < length(arr2) DO
        APPEND arr2[j] TO merged
        j := j + 1

    RETURN merged
}

FUNCTION find_median_sorted_arrays(nums1, nums2)
{
    merged := merge_sorted_arrays(nums1, nums2)
    n := length(merged)

    IF n IS ODD THEN
        median := merged[n // 2]
    ELSE
        median := (merged[n // 2 - 1] + merged[n // 2]) / 2
    END IF

    RETURN median
}
```

---

## 💻 Sample Run
```bash
Enter first sorted array (space separated): 1 3
Enter second sorted array (space separated): 2

Merged Sorted Array: [1, 2, 3]
Median: 2
```

```bash
Enter first sorted array (space separated): 1 2
Enter second sorted array (space separated): 3 4

Merged Sorted Array: [1, 2, 3, 4]
Median: 2.5
```

---

## 🧮 Time & Space Complexity

| Step | Complexity |
|------|-------------|
| Merging two arrays | O(m + n) |
| Finding median | O(1) |
| **Total Time Complexity** | O(m + n) |
| **Space Complexity** | O(m + n) |

---

## ⚠️ Edge Cases
| Input | Output |
|-------|--------|
| nums1 = [], nums2 = [1] | 1 |
| nums1 = [5], nums2 = [] | 5 |
| nums1 = [1,2,3], nums2 = [4,5,6] | 3.5 |

---

## 👨‍💻 Author
- **Name:** Ibrahim Hamdy  
- **Role:** Helwan National University  
- **Email:** ihamdy719@gmail.com