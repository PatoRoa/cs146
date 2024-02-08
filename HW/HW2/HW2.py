# We will be solving another homework problem! Here's the problem statement:
#
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version,
# all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of
# calls to the API.

def list_from_1_to_n(n):
    return list(range(1,n+1))


def check_first_bad(versions, low, high, bad_version):
    # Base case
    if high >= low:
        mid = (high + low) // 2

        # If the bad version is in the middle
        # original: if versions[mid] == bad_version:
        if isBadVersion(versions[mid]):
            return mid

        # If the bad version is in the left subarray
        elif versions[mid] > bad_version:
            return check_first_bad(versions, low, mid - 1, bad_version)

        else:
            return check_first_bad(versions, mid + 1, high, bad_version)

    else:
        # If there are no bad versions
        return -1


n = 10
versions = list_from_1_to_n(n)
bad_version = 9

result = check_first_bad(versions, 0, len(versions) - 1, bad_version)

if result != -1:
    print("The first bad version is ", str(result))

else:
    print("There are no bad versions")
