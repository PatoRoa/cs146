s = "Malay alam"


def check_palindrome(string):
    temp_array = s.lower()
    array = []
    
    for i in temp_array:
        if i.isalnum():
            array.append(i)

    print("array = ", array)

    t = array[::-1]

    for i in range(len(array)):
        if array == t:
            continue
        else:
            return print("'" + s + "'" + " is not a palindrome.")

    return print("'" + s + "'" + " is a palindrome.")

check_palindrome(s)
