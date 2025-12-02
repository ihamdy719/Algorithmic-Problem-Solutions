# 🧩 Project 1 — Max Product of Three

## 📖 Description
This program finds the **maximum possible product** of any three numbers from a non-empty array of integers.  
Unlike normal implementations, this version is fully **manual** — it doesn’t use any built-in functions like `split()`, `sort()`, or `max()`.

---

## 🧠 Example

### Example 1
```
Input:  [1, 2, 3]
Output: 6
```

### Example 2
```
Input:  [1, 2, 3, 4]
Output: 24
```

---

## ⚙️ Input / Output Format
- **Input:**  
  Comma-separated integers entered by the user (e.g., `-3,1,2,-2,5,6`).

- **Output:**  
  Displays step-by-step calculations including:
  - Sorted array  
  - Products computed  
  - The final maximum product  
  - Result stored in `results.txt`

---

## 🧩 Algorithm Steps
1. Ask the user to input numbers separated by commas.  
2. **Split** the input manually into substrings (no use of `.split()`).
3. **Validate** that each substring represents a valid integer (no letters, symbols, or decimals).
4. **Convert** each substring to integer manually using ASCII conversion.
5. If fewer than 3 integers are entered → show an error.
6. **Sort** the list manually using **Bubble Sort**.
7. Calculate two possible products:
   - `product1 = last * second_last * third_last`
   - `product2 = first * second * last`
8. Find the larger of the two manually.
9. Print the result clearly and **save it to file** `results.txt`.
10. Ask the user if they want to try again.

---

## 🧾 Pseudo-code
```text
1. Start
2. Read input as comma-separated string
3. Split it manually into substrings
4. For each substring:
     a. Check that it represents an integer only (no letters or decimals)
     b. Convert it manually to int
5. If less than 3 integers -> show error
6. Sort the numbers manually (Bubble Sort)
7. Compute:
     product1 = last * second_last * third_last
     product2 = first * second * last
8. Compare both manually and take the larger
9. Print and save result in file
10. Ask user to retry
11. End
```

---

## 🧮 Time & Space Complexity
| Function | Complexity |
|-----------|-------------|
| `manual_split()` | O(n) |
| `is_integer_string()` | O(m) |
| `manual_to_int_list()` | O(n × m) |
| `manual_sort()` | O(n²) |
| `manual_max()` | O(1) |
| **Overall Time Complexity** | **O(n²)** |
| **Space Complexity** | **O(n)** |

---

## 💻 Sample Run
```bash
Max Product of Three - Process Start

Enter the numbers separated by commas: -3, 1, 2, -2, 5, 6

Input array: [-3, 1, 2, -2, 5, 6]

Sorting the array...
Sorted array: [-3, -2, 1, 2, 5, 6]

Calculating possible products...
Product of largest three numbers: 2 * 5 * 6 = 60
Product of two smallest and largest number: -3 * -2 * 6 = 36

The maximum product of any triplet is: 60

Process finished successfully.
```

---

## 👨‍💻 Author
- **Name:** Ibrahim Hamdy  
- **Role:** Helwan National University  
- **Email:** ihamdy719@gmail.com
