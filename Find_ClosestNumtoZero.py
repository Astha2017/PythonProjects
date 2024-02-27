def closest_to_zero(nums):
    closest_num = float('inf')
    max_value = float('-inf')

    for num in nums:
        if abs(num) < abs(closest_num) or (abs(num) == abs(closest_num) and num > closest_num):
            closest_num = num
            max_value = num
        elif abs(num) == abs(closest_num) and num < closest_num:
            max_value = max(max_value, num)

    return max_value

nums = [-4,-2,1,4,8]

result = closest_to_zero(nums)

print("Number closest to 0 with largest value:", result)
