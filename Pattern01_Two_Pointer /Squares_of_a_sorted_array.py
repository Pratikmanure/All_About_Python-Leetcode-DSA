#square the sorted array without affecting its order (smallest to largest)

nums = [-4, -1, 0, 3, 10]

left = 0
right = len(nums) - 1

result = [0] * len(nums)
position = len(nums) - 1

while left <= right:

    if abs(nums[left]) > abs(nums[right]):
        result[position] = nums[left] ** 2
        left += 1
    else:
        result[position] = nums[right] ** 2
        right -= 1

    position -= 1

print(result)
