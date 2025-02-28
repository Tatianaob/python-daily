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
# - Move Zeros to the End
# - (Bonus) First Missing Positive Integer