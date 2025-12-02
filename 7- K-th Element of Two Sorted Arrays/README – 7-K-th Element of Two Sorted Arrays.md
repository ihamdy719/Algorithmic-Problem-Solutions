# 🔢 Project 7 — K-th Element of Two Sorted Arrays

## 📖 Description

The **K-th Element of Two Sorted Arrays** problem involves **finding the element that would be at the k-th position** if two sorted arrays were merged into a single sorted array.

Both arrays are already sorted, and it is guaranteed that `1 <= k <= m + n`.

---

## 🧠 Examples

### Example 1

```
Input:
Array 1 = [2, 3, 6, 7, 9]
Array 2 = [1, 4, 8, 10]
k = 5

Output:
Merged & Sorted Array: [1, 2, 3, 4, 6, 7, 8, 9, 10]
5-th Element: 6
```

### Example 2

```
Input:
Array 1 = [100, 112, 256, 349, 770]
Array 2 = [72, 86, 113, 119, 265, 445, 892]
k = 7

Output:
Merged & Sorted Array: [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]
7-th Element: 256
```

---

## ⚙️ Input / Output Format

* **Input:**

  * Two space-separated sorted arrays
  * An integer `k`

* **Output:**

  * The merged & sorted array
  * The k-th element in this array

---

## 🧩 Algorithm Steps

1. Read both sorted arrays from the user.
2. Merge the two arrays while maintaining sorted order.
3. Access the element at the `k-1` index of the merged array.
4. Return and print the merged array and the k-th element.

---

## 🧾 Pseudo-code

```text
FUNCTION merge_and_sort_arrays(arr1, arr2)
{
    merged_array := []
    i := 0
    j := 0

    WHILE i < length(arr1) AND j < length(arr2) DO
        IF arr1[i] < arr2[j] THEN
            APPEND arr1[i] TO merged_array
            i := i + 1
        ELSE
            APPEND arr2[j] TO merged_array
            j := j + 1
    END WHILE

    WHILE i < length(arr1) DO
        APPEND arr1[i] TO merged_array
        i := i + 1

    WHILE j < length(arr2) DO
        APPEND arr2[j] TO merged_array
        j := j + 1

    RETURN merged_array
}

FUNCTION find_kth_element(arr1, arr2, k)
{
    merged_array := merge_and_sort_arrays(arr1, arr2)
    kth_element := merged_array[k - 1]
    RETURN (merged_array, kth_element)
}

MAIN PROGRAM
{
    READ arr1
    READ arr2
    READ k
    (sorted_array, kth_element) := find_kth_element(arr1, arr2, k)
    PRINT sorted_array
    PRINT kth_element
}
```

---

## 💻 Sample Run

```bash
Enter numbers for the first array separated by spaces: 2 3 6 7 9
Enter numbers for the second array separated by spaces: 1 4 8 10
Enter the value of k: 5

First Array:  [2, 3, 6, 7, 9]
Second Array: [1, 4, 8, 10]
Merged & Sorted Array: [1, 2, 3, 4, 6, 7, 8, 9, 10]
The 5-th Element in the merged array is: 6
```

---

## 🧮 Time & Space Complexity

| Step                      | Complexity   |
| ------------------------- | ------------ |
| Merging two arrays        | O(m + n)     |
| Accessing k-th element    | O(1)         |
| **Total Time Complexity** | **O(m + n)** |
| **Space Complexity**      | O(m + n)     |

---

## ⚠️ Edge Cases

| Input                                     | Output |
| ----------------------------------------- | ------ |
| Array 1 = [], Array 2 = [1,2,3], k=2      | 2      |
| Array 1 = [5], Array 2 = [], k=1          | 5      |
| Array 1 = [1,2,3], Array 2 = [4,5,6], k=6 | 6      |

---

## 👨‍💻 Author

* **Name:** Ibrahim Hamdy
* **Role:** Helwan National Unive
