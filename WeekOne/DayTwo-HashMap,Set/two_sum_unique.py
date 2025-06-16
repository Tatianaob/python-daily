# Problem to Solve: Two Sum II (All Unique Pairs)
# Problem Statement:
# Given an integer array nums and an integer target, 
# return all unique pairs of numbers that add up to the target.

# Return the actual numbers (not indices). 
# You may not return duplicate pairs.

# Input:  nums = [2, 4, 3, 5, 7, 8, 1, 9]
# target = 10
# Expected Output: [(2, 8), (3, 7), (1, 9)]

def twoSum(nums, target):
    seen = set()
    result = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            result.add(tuple(sorted((num, complement)))) #to avoid duplicates
        seen.add(num)
    return list(result)

print(twoSum([2, 4, 3, 5, 7, 8, 1, 9], 10))