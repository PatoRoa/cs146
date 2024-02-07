# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

nums = [1, 3, 5, 7, 9]

target = 6

def term_indices (numbers, sum):
    for i in numbers:
        if sum - i in numbers:
            if numbers.index(i) == numbers.index(sum - 1):
                print("Term indices cannot be repeated")
                return
            else:
                print("Indices: " + str(numbers.index(i)) + ", " + str(numbers.index(sum - i)))
                return
        else:
            print("Not enough terms that can add up to", target)
            return

term_indices(nums, target)
