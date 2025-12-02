# 🔺 Project 2 — Triangle Triplets Problem

## 📖 Description
This program determines all **triangular triplets** in a given array.  
A triplet `(P, Q, R)` is *triangular* if it satisfies the triangle inequality rules:
1. `A[P] + A[Q] > A[R]`
2. `A[Q] + A[R] > A[P]`
3. `A[R] + A[P] > A[Q]`

Instead of only checking for the existence of one valid triplet, this implementation **counts all unique triangular triplets** and optionally returns them.

---

## 🧠 Example

### Example 1
```
Input:  [10, 50, 1]
Output: (0, [])
Explanation: No triplet satisfies the triangle inequality.
```

### Example 2
```
Input:  [10, 2, 5, 1, 8, 20]
Output: (5, [(8, 16, 20), (10, 16, 20), (5, 16, 20), (5, 8, 10), (8, 10, 16)])
Explanation: There are 5 valid triangular triplets.
```

---

## ⚙️ Input / Output Format

- **Input:**  
  Comma-separated integers (e.g., `10,2,5,1,8,20`)

- **Output:**  
  Displays both:
  - The total count of valid triangular triplets  
  - The actual triplets themselves (if found)

---

## 🧩 Algorithm Steps
1. Read the array from user input (comma-separated string).
2. Parse the string manually to extract integers.
3. Initialize a counter `count` and a list `triplets` to store valid results.
4. Iterate through all possible triplets `(P, Q, R)` such that:
   - `0 ≤ P < Q < R < N`
5. For each triplet, check the triangle conditions:
   - `A[P] + A[Q] > A[R]`
   - `A[Q] + A[R] > A[P]`
   - `A[R] + A[P] > A[Q]`
6. If all three are true, count it and save it.
7. Return `(count, triplets)` as the output.
8. Display the input array and output result clearly.

---

## 🧾 Pseudo-code
```text
FUNCTION is_triangular_triplet(A)
{
    n := length(A)
    count := 0
    triplets := []

    For P := 0 to n - 3 step 1 do
    {
        For Q := P + 1 to n - 2 step 1 do
        {
            For R := Q + 1 to n - 1 step 1 do
            {
                If A[P] + A[Q] > A[R] AND 
                   A[Q] + A[R] > A[P] AND 
                   A[R] + A[P] > A[Q] then
                {
                    count := count + 1
                    triplets.append((A[P], A[Q], A[R]))
                }
            }
        }
    }

    print("Input: nums = ", A)
    print("Output: (", count, ", ", triplets, ")")
}
```

---

## 🧮 Time & Space Complexity
| Component | Complexity |
|------------|-------------|
| Outer loop (P) | O(n) |
| Middle loop (Q) | O(n) |
| Inner loop (R) | O(n) |
| **Total Time Complexity** | **O(n³)** |
| **Space Complexity** | **O(k)**, where k is number of valid triplets |

---

## 💻 Sample Run
```bash
Enter the numbers in the array separated by commas: 10,2,5,1,8,20

Input: nums = [10, 2, 5, 1, 8, 20]
Output: (5, [(8, 16, 20), (10, 16, 20), (5, 16, 20), (5, 8, 10), (8, 10, 16)])
```

---

## ✨ Notes
- The code can be extended to allow:
  - Searching within a specific range `[start, end]`.
  - Returning triplets only if a flag `return_triplets=True` is set.
- It provides flexibility for custom analysis of triangle triplets in subsets.

---

## 👨‍💻 Author
- **Name:** Ibrahim Hamdy  
- **Role:** Helwan National University  
- **Email:** ihamdy719@gmail.com
