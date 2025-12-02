# 🔢 Project 8 — Dominator

## 📖 Description

An array `A` of `N` integers is given. The **dominator** of array `A` is the value that occurs in **more than half** of the elements in `A`.

The goal is to write an efficient algorithm that returns the **indices of any element** of array `A` where the dominator occurs. If the array has no dominator, return -1.

Constraints:

* N is an integer within `[0..100,000]`
* Each element of `A` is an integer within `[−2,147,483,648 ... 2,147,483,647]`

---

## 🧠 Examples

### Sample Input

```
A = [3, 4, 3, 2, 3, -1, 3, 3]
```

### Sample Output

```
Dominator Value: 3
Indices of Dominator: 0, 2, 4, 6, 7
```

---

## ⚙️ Input / Output Format

* **Input:**

  * Number of elements, `N`
  * Array elements, one by one

* **Output:**

  * Dominator value (if exists)
  * List of indices where dominator occurs
  * `-1` if no dominator exists

---

## 🧩 Algorithm Steps

1. Read the number of elements from the user.
2. Read all elements into an array.
3. Count occurrences of each element.
4. Determine if any element occurs more than `N/2` times.
5. If a dominator exists, collect all its indices.
6. Print the dominator and its indices; otherwise, print -1.

---

## 🧾 Pseudo-code

```text
FUNCTION dominator()
{
    count1 := 0
    my_list := []

    PRINT "How many elements to add:"
    READ numbers

    FOR i := 0 TO numbers - 1 DO
        PRINT "my_list[", i, "]:"
        READ num
        APPEND num TO my_list
    END FOR

    half_len := numbers / 2
    count2 := 0
    dom_list := []

    FOR i := 0 TO numbers - 1 DO
        FOR j := 0 TO numbers - 1 DO
            IF my_list[i] == my_list[j] THEN
                count2 := count2 + 1
                APPEND j TO dom_list
            END IF
        END FOR

        IF count2 > half_len THEN
            PRINT "Dominator Value =", my_list[i]
            PRINT "Indices =", dom_list
            RETURN dom_list
        ELSE
            count2 := 0
            CLEAR dom_list
        END IF
    END FOR

    PRINT "No dominator found."
    RETURN -1
}
```

---

## 💻 Sample Run

```bash
How many elements to add: 8
my_list[0]: 3
my_list[1]: 4
my_list[2]: 3
my_list[3]: 2
my_list[4]: 3
my_list[5]: -1
my_list[6]: 3
my_list[7]: 3

Dominator Value: 3
Indices of Dominator: 0, 2, 4, 6, 7
```

---

## 🧮 Time & Space Complexity

| Step                              | Complexity |
| --------------------------------- | ---------- |
| Nested loops to count occurrences | O(n²)      |
| Space for storing indices         | O(n)       |
| **Total Time Complexity**         | **O(n²)**  |
| **Space Complexity**              | O(n)       |

---

## ⚠️ Edge Cases

| Input           | Output  |
| --------------- | ------- |
| A = []          | -1      |
| A = [5]         | 0       |
| A = [1,2,3,4,5] | -1      |
| A = [7,7,7,7,2] | 0,1,2,3 |

---

## 👨‍💻 Author

* **Name:** Ibrahim Hamdy
* **Role:** Helwan National University
* **Email:** [ihamdy719@gmail.com](mailto:ihamdy719@gmail.com)
