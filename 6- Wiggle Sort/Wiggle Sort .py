def wiggle_sort(nums):
    print("Original array:", nums)

    # الخطوة 1: نرتب المصفوفة
    nums.sort()
    print("\nSorted array:", nums)

    n = len(nums)
    half = n // 2

    # الخطوة 2: نجهز النصفين
    small = nums[:half][::-1]   # النصف الأصغر بالعكس
    large = nums[half:][::-1]   # النصف الأكبر بالعكس

    print("\nSmaller half:", small)
    print("Larger half:", large)

    # الخطوة 3: ندمجهم بطريقة الموجة
    wiggle = []
    for i in range(n):
        if i % 2 == 0:  # الأماكن الزوجية (0,2,4..) ناخد من الصغير
            if small:
                wiggle.append(small.pop(0))
        else:           # الأماكن الفردية (1,3,5..) ناخد من الكبير
            if large:
                wiggle.append(large.pop(0))

    print("\nWiggle Sorted Array:", wiggle)
    return wiggle


# ======== تجربة ========
nums_input = input("Enter the array elements separated by commas: ")

# تحويل الإدخال إلى أرقام
nums = []
number = ""
for ch in nums_input:
    if ch == ",":
        if number != "":
            nums.append(int(number))
            number = ""
    else:
        number += ch
if number != "":
    nums.append(int(number))

# تشغيل الدالة
wiggle_sort(nums)


# ==========================================================
#                   PSEUDO-CODE
# ==========================================================
'''
FUNCTION wiggle_sort(nums)
{
    PRINT "Original array:", nums
    SORT nums
    n := length(nums)
    half := n // 2

    small := reverse(nums[0 : half])
    large := reverse(nums[half : n])

    wiggle := []

    FOR i := 0 TO n - 1 DO
        IF i is even THEN
            IF small not empty THEN
                ADD small[0] TO wiggle
                REMOVE small[0]
        ELSE
            IF large not empty THEN
                ADD large[0] TO wiggle
                REMOVE large[0]
    END FOR

    PRINT "Wiggle Sorted Array:", wiggle
    RETURN wiggle
}
'''


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
'''
- Sorting the array: O(n log n)
- Splitting and reversing: O(n)
- Merging in wiggle order: O(n)
=> Total Time Complexity: O(n log n)
=> Space Complexity: O(n)
'''
