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

def longestPalindrome(s: str) -> int:
    hash = {}

    counter = 0
    for i in s:
        if i in hash:
            hash.pop(i)
            counter += 1

        else:
            hash[i] = 1

    if hash:
        return counter * 2 + 1

    return counter * 2


s = "abccccdd"

longestPalindrome(s)
