def merge_and_sort_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0

    # دمج المصفوفتين بطريقة مرتبة
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # إضافة العناصر المتبقية من arr1 (لو فيه)
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # إضافة العناصر المتبقية من arr2 (لو فيه)
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array


def find_kth_element(arr1, arr2, k):
    merged_array = merge_and_sort_arrays(arr1, arr2)
    kth_element = merged_array[k-1]
    return merged_array, kth_element


# ===================== التشغيل =====================
arr1 = [int(x) for x in input("Enter numbers for the first array separated by spaces: ").split()]
arr2 = [int(x) for x in input("Enter numbers for the second array separated by spaces: ").split()]
k = int(input("Enter the value of k: "))

sorted_array, kth_element = find_kth_element(arr1, arr2)

print("\n====================================")
print(f"First Array:  {arr1}")
print(f"Second Array: {arr2}")
print(f"Merged & Sorted Array: {sorted_array}")
print(f"The {k}-th Element in the merged array is: {kth_element}")
print("====================================")


# ==========================================================
#                   PSEUDO-CODE
# ==========================================================
'''
FUNCTION merge_and_sort_arrays(arr1, arr2)
{
    merged_array := []
    i := 0
    j := 0

    WHILE i < length(arr1) AND j < length(arr2) DO
        IF arr1[i] < arr2[j] THEN
            APPEND arr1[i] TO merged_array
            i := i + 1
        ELSE
            APPEND arr2[j] TO merged_array
            j := j + 1
        END IF
    END WHILE

    WHILE i < length(arr1) DO
        APPEND arr1[i] TO merged_array
        i := i + 1
    END WHILE

    WHILE j < length(arr2) DO
        APPEND arr2[j] TO merged_array
        j := j + 1
    END WHILE

    RETURN merged_array
}

FUNCTION find_kth_element(arr1, arr2, k)
{
    merged_array := merge_and_sort_arrays(arr1, arr2)
    kth_element := merged_array[k - 1]
    RETURN (merged_array, kth_element)
}

MAIN PROGRAM
{
    READ arr1
    READ arr2
    READ k
    (sorted_array, kth_element) := find_kth_element(arr1, arr2, k)
    PRINT sorted_array
    PRINT kth_element
}
'''


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
'''
Let:
n = length(arr1)
m = length(arr2)

- Merging two sorted arrays takes O(n + m)
- Accessing k-th element takes O(1)
=> Total Time Complexity: O(n + m)
=> Space Complexity: O(n + m)
'''
