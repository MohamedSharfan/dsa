# Q6. Two Sum Problem

# Example: nums = [2, 7, 11, 15], target = 9 → Output: [0, 1]
# Hint: Use a dictionary to store complement values

def twoSum(nums, target):
    my_dict = {}
    for i, num in enumerate(nums):
        complement = target - nums[i]
        if complement in my_dict:
            return [my_dict[complement], i]
        my_dict[num] = i




if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)