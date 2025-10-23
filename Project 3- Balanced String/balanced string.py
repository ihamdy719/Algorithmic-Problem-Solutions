def is_balanced(sub):
    # نحسب تكرار كل حرف في الـ substring
    freq = {}
    for ch in sub:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    # لازم يكون فيها حرفين مختلفين بالظبط
    if len(freq) != 2:
        return False

    # نجيب عدد التكرارات
    values = list(freq.values())

    # لازم يكونوا متساويين وكل واحد فيهم > 1
    return values[0] == values[1] and values[0] > 1


def longest_balanced_substring(S):
    n = len(S)
    max_len = 0
    longest_sub = ""

    # نجرب كل substring ممكنة
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = S[i:j]
            if is_balanced(sub):
                if len(sub) > max_len:
                    max_len = len(sub)
                    longest_sub = sub

    return max_len, longest_sub


# أخذ الإدخال من المستخدم
S = input("Enter a string: ")

length, substring = longest_balanced_substring(S)

print(f"\nInput String: {S}")
if length > 0:
    print(f"Longest Balanced Substring: '{substring}'")
    print(f"Length: {length}")
else:
    print("No balanced substring found.")


# ==========================================================
#                   PSEUDO-CODE
# ==========================================================
'''
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
'''


# ==========================================================
#             TIME COMPLEXITY ANALYSIS
# ==========================================================
'''
- Outer loop (i): runs n times
- Inner loop (j): runs up to n times
- Checking each substring (is_balanced): O(n) worst case
=> Total Time Complexity: O(n³)
=> Space Complexity: O(n)
'''
