# Problem 1: Reverse an Array (Easy)
# Given an array, reverse the order of its elements.

# Example:
# Input: nums = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

my_array = [1,2,3,4,5,5]
reversed_array = my_array[::-1]
print(reversed_array)

### second approach
new_array =[1,2,3,4,5,6,7,8]
my_array_2 = []
for i in range(len(new_array)-1,-1,-1):
    my_array_2.append(new_array[i])
print(my_array_2)



