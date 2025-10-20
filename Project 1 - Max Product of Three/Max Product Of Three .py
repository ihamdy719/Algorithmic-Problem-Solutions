# تقسيم النص يدويًا بدل split()
def manual_split(text, separator):
    current = ""
    result = []
    for ch in text:
        if ch == separator:
            result.append(current)
            current = ""
        else:
            current += ch
    result.append(current)
    return result


# التحقق أن النص يمثل عدد صحيح فقط (يدويًا)
def is_integer_string(s):
    s = s.strip()
    if s == "" or s == "-" or s == "+":
        return False
    start = 1 if s[0] in ['-', '+'] else 0
    for c in s[start:]:
        if c < '0' or c > '9':
            return False
    return True


# تحويل النصوص إلى أعداد صحيحة يدويًا
def manual_to_int_list(str_list):
    result = []
    for s in str_list:
        s = s.strip()
        if not is_integer_string(s):
            raise ValueError("Non-integer value found")
        num = 0
        negative = False
        if s[0] == "-":
            negative = True
            s = s[1:]
        for c in s:
            num = num * 10 + (ord(c) - ord('0'))
        if negative:
            num = -num
        result.append(num)
    return result


# دالة ترتيب يدوي (Bubble Sort)
def manual_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


# دالة ترجع الأكبر بين قيمتين
def manual_max(a, b):
    if a > b:
        return a
    else:
        return b


# قراءة الأرقام من المستخدم (Int فقط)
def get_numbers_from_user():
    while True:
        user_input = input("Enter the numbers separated by commas: ")

        try:
            str_list = manual_split(user_input, ',')
            nums = manual_to_int_list(str_list)
        except:
            print("Error: Please enter integers only, separated by commas.\n")
            continue

        if len(nums) < 3:
            print("Error: You must enter at least 3 numbers.\n")
            continue

        return nums


# حساب الناتج النهائي
def max_product(nums):
    print("Input array:", nums)

    print("\nSorting the array...")
    manual_sort(nums)
    print("Sorted array:", nums)

    print("\nCalculating possible products...")
    product1 = nums[-1] * nums[-2] * nums[-3]
    print("Product of largest three numbers:", nums[-3], "*", nums[-2], "*", nums[-1], "=", product1)

    product2 = nums[0] * nums[1] * nums[-1]
    print("Product of two smallest and largest number:", nums[0], "*", nums[1], "*", nums[-1], "=", product2)

    result = manual_max(product1, product2)
    print("\nThe maximum product of any triplet is:", result)

    # حفظ النتيجة في ملف
    f = open("results.txt", "a")
    f.write("Input: " + str(nums) + " -> Max Product: " + str(result) + "\n")
    f.close()

    print("\nProcess finished successfully.\n")
    return result


def main():
    print("Max Product of Three - Process Start\n")

    while True:
        nums = get_numbers_from_user()
        max_product(nums)
        
# تشغيل البرنامج
main()



# ==========================================================
#                 PSEUDO-CODE
# ==========================================================
# 1. Start
# 2. Read input as comma-separated string
# 3. Split it manually into substrings
# 4. For each substring:
#      a. Check that it represents an integer only (no letters or decimals)
#      b. Convert it manually to int
# 5. If less than 3 integers -> show error
# 6. Sort the numbers manually (Bubble Sort)
# 7. Compute:
#       product1 = last * second_last * third_last
#       product2 = first * second * last
# 8. Compare both manually and take the larger
# 9. Print and save result in file
# 10. Ask user to retry
# 11. End


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
# manual_split()        → O(n)
# is_integer_string()   → O(m)
# manual_to_int_list()  → O(n * m)
# manual_sort()         → O(n²)
# manual_max()          → O(1)
# Overall Time Complexity: O(n²)
# Space Complexity: O(n)
