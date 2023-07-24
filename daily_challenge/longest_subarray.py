"""
Challenge: Find the Longest Subarray with Equal Number of 0s and 1s

Write a Python function called find_longest_subarray that takes a list of integers, 
nums, as input. The function should find the longest contiguous subarray within nums that has an equal number 
of 0s and 1s. If there are multiple subarrays with the same maximum length, return the first one found.

nums = [0, 1, 1, 0, 0, 1, 1, 0, 1]
result = find_longest_subarray(nums)
print(result)  # Output: [1, 1, 0, 0, 1, 1]

Challenge Notes:

The input list nums will contain only 0s and 1s (i.e., binary values).
The subarray must be contiguous, meaning all elements are adjacent and appear in consecutive positions within nums.
The length of the subarray can be zero (no 0s or 1s), in which case, return an empty list.
"""

def find_longest_subarray(nums):
    max_length = -0
    start_index = 0
    sum_map = {0: 0}
    total_sum = 0

    for i, num in enumerate(nums):
        if num == 0:
            total_sum -= 1
        else:
            total_sum += 1

        if total_sum in sum_map:
            if i - sum_map[total_sum] > max_length and start_index != -1:
                max_length = i - sum_map[total_sum]
                start_index = sum_map[total_sum] + 1
        else:
            sum_map[total_sum] = i

    if start_index == -1:
        return []  # No subarray found
    else:
        return nums[start_index: start_index + max_length - 1]
    

# Test the function
nums = [0, 1, 1, 0, 0, 1, 1, 0, 1]

# Should print [1,1,0,0,1,1]
print(find_longest_subarray(nums))  
