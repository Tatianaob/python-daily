# Problem 1: Reverse an Array (Easy)
# Given an array, reverse the order of its elements.
# Example:
# Input: nums = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

my_array = [1,2,3,4,5,5]
reversed_array = my_array[::-1]
print(reversed_array)

# second approach
new_array =[1,2,3,4,5,6,7,8]
my_array_2 = []
for i in range(len(new_array)-1,-1,-1):
    my_array_2.append(new_array[i])
print(my_array_2)

########################################################

# Problem 2 Find Maximum in an Array
#  Given an array of integers, find the maximum element in the array.
# Input: nums = [3, 7, 2, 9, 5]
# Output: 9

def max_nums(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
print(max_nums([3, 7,40, 2, 9, 5,10]))

def another_max(nums):
    return(max(nums))
print(another_max([1,2,7,56,9,6]))

#########################################################

# - Two Sum (Leetcode #1)
# Description: Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

# nums = [2,7,11,15]
# target = 9
# Output: [0,1]

def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return num_map[complement], i
        num_map[num] = i

print(twoSum([2,7,11,15,1,8], 9))

# - Move Zeros to the End

def moveZeros(numeros):
    posicion = 0
    for num in numeros:
        if num != 0:
            numeros[posicion] = num
            posicion += 1
    while posicion < len(numeros):
        numeros[posicion] = 0
        posicion += 1
    return numeros

print(moveZeros([0, 1, 0, 3, 12]))



# First Missing Positive Integer - LeetCode 41
# Given an unsorted integer array nums,
# return the smallest missing positive integer.
# nums = [1,2,0] output = 3

def firstMissingPositive(nums):
    num_set = set(nums)
    i = 1
    while True:
        if i not in num_set:
            return i
        i += 1

print(firstMissingPositive([1, 2, 0]))        # ➞ 3
print(firstMissingPositive([3, 4, -1, 1]))    # ➞ 2
print(firstMissingPositive([7, 8, 9, 11, 12]))# ➞ 1