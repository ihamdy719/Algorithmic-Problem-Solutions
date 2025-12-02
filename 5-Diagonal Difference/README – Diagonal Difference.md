# 🔢 Project 5 — Diagonal Difference

## 📖 Description
This program calculates the **absolute difference** between the sums of the two diagonals of a **square matrix**.

It also checks whether the two diagonals have **equal sums** — if yes, it returns `True`; otherwise, `False`.

---

## 🧠 Example

### Example 1
```
Input:
3
11 2 4
4 5 6
10 8 -12

Output:
Left-to-right diagonal sum  = 28
Right-to-left diagonal sum  = 19
Absolute difference         = 9
Are the diagonals equal?    = False
```

### Example 2
```
Input:
3
1 2 3
4 5 6
7 8 9

Output:
Left-to-right diagonal sum  = 15
Right-to-left diagonal sum  = 15
Absolute difference         = 0
Are the diagonals equal?    = True
```

---

## ⚙️ Input / Output Format

- **Input:**
  - An integer `n` → the number of rows and columns.
  - `n` lines, each containing `n` space-separated integers.

- **Output:**
  - The two diagonal sums.
  - Their absolute difference.
  - A boolean value (`True` or `False`) depending on whether the diagonals are equal.

---

## 🧩 Algorithm Steps

1. Ask the user to enter the matrix size `n`.
2. Read the `n × n` matrix row by row.
3. Initialize two sums:
   - `left_to_right` → main diagonal (top-left to bottom-right)
   - `right_to_left` → secondary diagonal (top-right to bottom-left)
4. Loop through the matrix indices:
   - Add `matrix[i][i]` to `left_to_right`.
   - Add `matrix[i][n - i - 1]` to `right_to_left`.
5. Compute the **absolute difference** between both sums.
6. Check if they are equal → `is_equal = (difference == 0)`
7. Display all results neatly.

---

## 🧾 Pseudo-code
```text
FUNCTION diagonal_difference()
{
    READ n
    matrix := []

    FOR i := 0 TO n-1 DO
        READ n space-separated integers into row
        APPEND row TO matrix
    END FOR

    left_to_right := 0
    right_to_left := 0

    FOR i := 0 TO n-1 DO
        left_to_right := left_to_right + matrix[i][i]
        right_to_left := right_to_left + matrix[i][n - i - 1]
    END FOR

    difference := ABS(left_to_right - right_to_left)
    is_equal := (difference == 0)

    PRINT "Left-to-right diagonal sum =", left_to_right
    PRINT "Right-to-left diagonal sum =", right_to_left
    PRINT "Absolute difference =", difference
    PRINT "Are the diagonals equal? =", is_equal

    RETURN difference, is_equal
}
```

---

## 🧮 Time & Space Complexity

| Operation | Complexity |
|------------|-------------|
| Reading matrix | O(n²) |
| Summing diagonals | O(n) |
| Absolute difference & comparison | O(1) |
| **Total Time Complexity** | **O(n²)** |
| **Space Complexity** | **O(n²)** |

---

## 💻 Sample Run
```bash
Enter the size of the square matrix: 3
Enter the matrix elements row by row (space separated):
Row 1: 11 2 4
Row 2: 4 5 6
Row 3: 10 8 -12

=========================================
Left-to-right diagonal sum  = 28
Right-to-left diagonal sum  = 19
Absolute difference         = 9
Are the diagonals equal?    = False
=========================================
```

---

## ⚠️ Edge Cases
| Input | Expected Output |
|--------|----------------|
| Matrix with all zeros | Difference = 0, True |
| Negative values | Works correctly (absolute difference used) |
| 1x1 matrix | Difference = 0, True |

---

## 👨‍💻 Author
- **Name:** Ibrahim Hamdy  
- **Role:** Helwan National University  
- **Email:** ihamdy719@gmail.com
