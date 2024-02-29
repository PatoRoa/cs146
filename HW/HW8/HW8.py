# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that
# can be built with those letters.
#
# Letters are case-sensitive, for eresultample, "Aa" is not considered a palindrome here.
#
# Again, your problem has additional details:
#
# Constraints:
#     - 1 <= s.length <= 2000
#     - s consists of lowercase and/or uppercase English letters only.

from collections import Counter

def longestPalindrome(s):
    count = Counter(s)
    result = 0

    for i in count.values():
        result += i - (i & 1)
        result += (result & 1 ^ 1) and (i & 1)

    return print(result)



string = "Abccccdd"
longestPalindrome(string)
