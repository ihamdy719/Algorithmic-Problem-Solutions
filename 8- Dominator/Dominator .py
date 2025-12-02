def dominator():     
    count1 = 0 
    my_list = [] 
    numbers = int(input("How many elements to add: ")) 

    # إدخال عناصر المصفوفة
    for i in range(numbers): 
        num = int(input(f"my_list[{i}]: ")) 
        my_list.append(num) 

    # حساب عدد العناصر
    for i in range(numbers): 
        count1 += 1 

    half_len = count1 / 2 
    count2 = 0 
    dom_list = [] 

    # البحث عن العنصر المسيطر (dominator)
    for i in range(numbers): 
        for j in range(numbers): 
            if my_list[i] == my_list[j]: 
                count2 += 1 
                dom_list.append(j)

        # لو العنصر ظهر أكتر من نص المصفوفة
        if count2 > half_len: 
            print(f"\nDominator Value: {my_list[i]}")
            print(f"Indices of Dominator: {dom_list}")
            return dom_list             
        else: 
            count2 = 0 
            dom_list.clear() 

    # لو مفيش عنصر متكرر كفاية
    print("\nNo dominator found.")
    return -1 


# تشغيل البرنامج
dominator()


# ==========================================================
#                   PSEUDO-CODE
# ==========================================================
'''
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

    FOR i := 0 TO numbers - 1 DO
        count1 := count1 + 1
    END FOR

    half_len := count1 / 2
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
'''


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
'''
Let n = number of elements in the array

- Outer loop runs n times
- Inner loop runs n times for each outer iteration
=> Total operations = n * n = O(n²)
- Space used for dom_list up to O(n)

=> Time Complexity: O(n²)
=> Space Complexity: O(n)
'''
