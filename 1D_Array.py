def running_sum(nums):
    running_sum = 0
    result = []
    for num in nums:
        running_sum += num
        result.append(running_sum)
    return result

# Example usage:
nums = [1, 2, 3, 4]
print(running_sum(nums))  # Output: [1, 3, 6, 10]
