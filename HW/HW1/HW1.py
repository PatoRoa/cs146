s = "malayalam"


def check_palindrome(string):
    t = s[::-1]

    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            return print("'" + s + "'" + " is not a palindrome.")

    return print("'" + s + "'" + " is a palindrome.")

check_palindrome(s)
