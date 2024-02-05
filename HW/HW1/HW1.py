s = "bird rib"


def check_palindrome(string):
    t = ""

    for i in s:
        if i.isalnum():
            t += i

    u = t[::-1]

    for j in range(len(t)):

        if t[j] == u[j]:
            continue
        else:
            return print("'" + s + "'" + " is not a palindrome.")

    return print("'" + s + "'" + " is a palindrome.")

check_palindrome(s)
