def Birthday_cake(): 
    num_candles = int(input("How many candles To add it: ")) 
    height_candles = [] 

    for i in range(num_candles): 
        candle_per_height = int(input(f"Enter The height of The candle its position {i + 1}: ")) 
        height_candles.append(candle_per_height) 

    center = int(num_candles / 2) 
    max_height = 0 
    count1 = 0 
    count2 = 0 

    # حساب عدد الشموع
    for i in height_candles: 
        count1 += 1 

    # إيجاد أطول شمعة
    for i in range(count1): 
        if height_candles[i] > max_height: 
            max_height = height_candles[i] 

    # التحقق إذا كانت الشمعة الأطول في المنتصف
    if height_candles[center] == max_height: 
        print(f"The tallest candle is {max_height} and locate in The center = {center + 1}") 

        # حساب عدد الشموع الأطول
        for i in range(count1): 
            if max_height == height_candles[i]: 
                count2 += 1 
        print(f"number of tallest candle is {count2}") 

        # التحقق من التماثل (symmetry)
        j = 1 
        for i in range(center): 
            if num_candles % 2 != 0: 
                if height_candles[center - j] != height_candles[center + j]: 
                    return "Is symmetric: False" 
            else: 
                return "Is symmetric: False" 
            j += 1 
        return "Is symmetric: True" 
    else: 
        return "tallest candle must be in the center" 


# تشغيل البرنامج
print(Birthday_cake())


# ==========================================================
#                   PSEUDO-CODE
# ==========================================================
'''
FUNCTION Birthday_cake()
{
    PRINT "How many candles To add it: "
    READ num_candles
    height_candles := []
    max_height := 0
    count1 := 0
    count2 := 0

    FOR i := 0 TO num_candles - 1 DO
        PRINT "Enter The height of The candle its position", (i+1)
        READ candle_per_height
        APPEND candle_per_height TO height_candles
    END FOR

    center := num_candles / 2

    FOR each element in height_candles DO
        count1 := count1 + 1
    END FOR

    FOR i := 0 TO count1 - 1 DO
        IF height_candles[i] > max_height THEN
            max_height := height_candles[i]
        END IF
    END FOR

    IF height_candles[center] == max_height THEN
        PRINT "The tallest candle is", max_height, "and locate in The center =", center+1

        FOR i := 0 TO count1 - 1 DO
            IF height_candles[i] == max_height THEN
                count2 := count2 + 1
            END IF
        END FOR

        PRINT "number of tallest candles is", count2

        j := 1
        FOR i := 0 TO center - 1 DO
            IF num_candles % 2 != 0 THEN
                IF height_candles[center - j] != height_candles[center + j] THEN
                    RETURN "Is symmetric: False"
                END IF
            ELSE
                RETURN "Is symmetric: False"
            END IF
            j := j + 1
        END FOR

        RETURN "Is symmetric: True"
    ELSE
        RETURN "tallest candle must be in the center"
    END IF
}
'''


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
'''
- Reading input heights: O(n)
- Counting total candles: O(n)
- Finding maximum height: O(n)
- Counting tallest candles: O(n)
- Checking symmetry: O(n/2) ≈ O(n)

=> Total Time Complexity: O(n)
=> Space Complexity: O(n)
'''
