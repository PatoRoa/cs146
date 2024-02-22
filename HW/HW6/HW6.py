# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.
#
# Constraints:
#     The solution set must not contain duplicate triplets.
#     The order of the output and the order of the triplets does not matter.
#     3 <= nums.length <= 3000
#     -10^5 <= nums[i] <= 10^5

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
# Input: nums = [-5,0,5,10,-10,0]
# Output: [[-10,0,10],[-5,0,5]]
# Explanation: There are two possible combinations of triplets that satisfy: (-5,0,5) and (-10,0,10).


def three_sum(nums):
    nums.sort()
    n = len(nums)
    triplets = list()

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum = nums[i] + nums[j] + nums[k]
                print("sum", sum)
                if sum == 0:
                    if [nums[i], nums[j], nums[k]] not in triplets:
                        triplets.append([nums[i], nums[j], nums[k]])

    return print(triplets)


lis = [-5, 0, 5, 10, -10, 0]

three_sum(lis)
