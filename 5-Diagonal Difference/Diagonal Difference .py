def diagonal_difference():
    n = int(input("Enter the size of the square matrix: "))

    matrix = []
    print("\nEnter the matrix elements row by row (space separated):")
    for i in range(n):
        row_input = input(f"Row {i+1}: ")
        row = []
        number = ""
        for ch in row_input:
            if ch == " ":
                if number != "":
                    row.append(int(number))
                    number = ""
            else:
                number += ch
        if number != "":
            row.append(int(number))
        matrix.append(row)

    # حساب القطرين
    left_to_right = 0
    right_to_left = 0

    for i in range(n):
        left_to_right += matrix[i][i]
        right_to_left += matrix[i][n - i - 1]

    # حساب الفرق المطلق
    difference = left_to_right - right_to_left
    if difference < 0:
        difference *= -1

    # التحقق من المساواة
    is_equal = (difference == 0)

    # عرض النواتج بالتفصيل
    print("\n=========================================")
    print(f"Left-to-right diagonal sum  = {left_to_right}")
    print(f"Right-to-left diagonal sum  = {right_to_left}")
    print(f"Absolute difference         = {difference}")
    print(f"Are the diagonals equal?    = {is_equal}")
    print("=========================================")

    return difference, is_equal


# تشغيل البرنامج
diagonal_difference()


# ==========================================================
#                   PSEUDO-CODE
# ==========================================================
'''
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
'''


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
'''
- Reading matrix: O(n²)
- Summing diagonals: O(n)
- Absolute difference and comparison: O(1)
=> Total Time Complexity: O(n²)
=> Space Complexity: O(n²)
'''
