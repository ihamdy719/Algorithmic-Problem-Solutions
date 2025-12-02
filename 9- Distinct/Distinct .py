def count_distinct_stream():
    n = int(input("Enter number of elements (N): "))

    distinct_values = set()  # لتخزين القيم المميزة فقط
    print("\nEnter the numbers one by one:")

    for i in range(n):
        num = int(input(f"A[{i}]: "))

        # نضيف الرقم لو مش موجود
        if num not in distinct_values:
            distinct_values.add(num)

    print("\n=========================================")
    print(f"Distinct values found: {len(distinct_values)}")
    print(f"Unique elements: {list(distinct_values)}")
    print("=========================================")

    return len(distinct_values)


# تشغيل البرنامج
count_distinct_stream()


# ==========================================================
#                   PSEUDO-CODE
# ==========================================================
'''
FUNCTION count_distinct_stream()
{
    READ n
    distinct_values := empty set

    FOR i := 0 TO n-1 DO
        READ num
        IF num NOT IN distinct_values THEN
            ADD num TO distinct_values
        END IF
    END FOR

    PRINT "Distinct values found:", LENGTH(distinct_values)
    PRINT "Unique elements:", distinct_values
    RETURN LENGTH(distinct_values)
}
'''


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
'''
Let n = number of elements in the stream.

- For each element:
    - Checking existence in a set: O(1)
    - Adding new value to set: O(1)
- Total for n elements: O(n)

=> Time Complexity: O(n)
=> Space Complexity: O(k)
   where k = number of distinct values (k ≤ n)
'''
