# ⚖️ Project 3 — Balanced String Problem

## 📖 Description
A **string** is called *balanced* if it:
1. Contains **exactly two different characters**, and  
2. Both characters appear **the same number of times**.

The program finds the **longest balanced substring** within a given string `S`.  
A substring means a sequence of **consecutive characters** in the original string.

---

## 🧠 Examples

### Example 1
```
Input:  "cabbacc"
Output: 4
Explanation: The substring "abba" is the longest balanced substring.
```

### Example 2
```
Input:  "abababa"
Output: 6
Explanation: "ababab" and "bababa" are the longest balanced substrings.
```

### Example 3
```
Input:  "aaaaaaa"
Output: 0
Explanation: No balanced substring exists because there’s only one unique character.
```

---

## ⚙️ Input / Output Format

- **Input:**  
  A single string (e.g., `"cabbacc"`)

- **Output:**  
  The longest balanced substring and its length.

---

## 🧩 Algorithm Steps

1. Read a string `S` from the user.  
2. Loop through all possible substrings `(S[i:j])`.  
3. For each substring:
   - Count the occurrences of each character manually.
   - Ensure it contains exactly two distinct characters.
   - Check if both characters appear the same number of times and each count > 1.
4. Keep track of:
   - The longest balanced substring.
   - Its length.
5. Return `(max_len, longest_sub)` as the result.
6. Print the result neatly.

---

## 🧾 Pseudo-code
```text
FUNCTION longest_balanced_substring(S)
{
    n := length(S)
    max_len := 0
    longest_sub := ""

    FOR i := 0 to n - 1 DO
        FOR j := i + 1 to n DO
            sub := substring of S from i to j
            IF sub has exactly two distinct characters AND
               each appears the same number of times AND
               both counts > 1 THEN
               IF length(sub) > max_len THEN
                   max_len := length(sub)
                   longest_sub := sub
               END IF
            END IF
        END FOR
    END FOR

    RETURN (max_len, longest_sub)
}
```

---

## 🧮 Time & Space Complexity

| Operation | Complexity |
|------------|-------------|
| Outer loop (i) | O(n) |
| Inner loop (j) | O(n) |
| Checking balance (is_balanced) | O(n) |
| **Total Time Complexity** | **O(n³)** |
| **Space Complexity** | **O(n)** |

---

## 💻 Sample Run
```bash
Enter a string: cabbacc

Input String: cabbacc
Longest Balanced Substring: 'abba'
Length: 4
```

---

## ⚠️ Edge Cases
| Input | Expected Output |
|--------|----------------|
| `"aaaaaa"` | No balanced substring |
| `"abcabc"` | 0 (because more than two distinct letters) |
| `"aabb"` | Balanced substring: "aabb" (length 4) |

---

## 👨‍💻 Author
- **Name:** Ibrahim Hamdy  
- **Role:** Helwan National University
- **Email:** ihamdy719@gmail.com
