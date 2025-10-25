# 🎂 Project 4 — Birthday Cake Candles

## 📖 Description
You are responsible for the birthday cake of a child.  
Each candle on the cake represents one year of their age.  
The child can only blow out the **tallest candles**.  

This program counts:
1. The **maximum height** of the candles.  
2. The **number of candles** that have the maximum height.  
3. Checks if the **tallest candles are symmetrically positioned** around the center.  

If not symmetric, the program suggests rearranging elements to make it symmetric.

---

## 🧠 Example

### Example 1
```
Input:
4
4 4 1 3

Output:
Max height: 4
Number of tallest candles: 2
Is symmetric: False
```

### Example 2
```
Input:
5
3 2 5 2 3

Output:
Max height: 5
Number of tallest candles: 1
Is symmetric: True
```

---

## ⚙️ Input / Output Format

- **Input:**
  - An integer `n` → the number of candles.
  - A list of integers representing the candle heights.

- **Output:**
  - Maximum height value.
  - Number of tallest candles.
  - Whether or not the tallest candles are symmetric.

---

## 🧩 Algorithm Steps

1. Ask the user to enter the number of candles.  
2. For each candle, read its height.  
3. Find the **maximum height** manually.  
4. Count how many candles have this maximum height.  
5. Determine the **center position** of the array.  
6. Check symmetry by comparing mirror elements around the center:
   - If `candles[center - j] == candles[center + j]` for all valid `j`, it's symmetric.
7. Print:
   - Maximum height
   - Number of tallest candles
   - Whether symmetric or not  
8. If not symmetric → suggest rearrangement.

---

## 🧾 Pseudo-code
```text
FUNCTION Birthday_cake()
{
    READ num_candles
    height_candles := []
    FOR i := 0 TO num_candles - 1 DO
        READ candle_height
        APPEND candle_height TO height_candles
    END FOR

    center := num_candles / 2
    max_height := 0
    count := 0

    FOR each height IN height_candles DO
        IF height > max_height THEN
            max_height := height
        END IF
    END FOR

    FOR each height IN height_candles DO
        IF height == max_height THEN
            count := count + 1
        END IF
    END FOR

    IF height_candles[center] == max_height THEN
        symmetric := True
        FOR j := 1 TO center DO
            IF height_candles[center - j] != height_candles[center + j] THEN
                symmetric := False
            END IF
        END FOR
    ELSE
        symmetric := False
    END IF

    PRINT "Max height:", max_height
    PRINT "Number of tallest candles:", count
    PRINT "Is symmetric:", symmetric
}
```

---

## 🧮 Time & Space Complexity

| Operation | Complexity |
|------------|-------------|
| Finding max height | O(n) |
| Counting tallest candles | O(n) |
| Checking symmetry | O(n/2) ≈ O(n) |
| **Total Time Complexity** | **O(n)** |
| **Space Complexity** | **O(n)** |

---

## 💻 Sample Run
```bash
How many candles To add it: 4
Enter The height of The candle its position 1: 4
Enter The height of The candle its position 2: 4
Enter The height of The candle its position 3: 1
Enter The height of The candle its position 4: 3

The tallest candle is 4 and locate in The center = 2
number of tallest candle is 2
Is symmetric: False
```

---

## ⚠️ Edge Cases
| Input | Expected Output |
|--------|----------------|
| `[5,5,5,5,5]` | Symmetric → True |
| `[4,1,4]` | Symmetric → True |
| `[4,4,1,3]` | Not symmetric → False |

---

## 👨‍💻 Author
- **Name:** Ibrahim Hamdy  
- **Role:** Helwan National University  
- **Email:** ihamdy719@gmail.com
