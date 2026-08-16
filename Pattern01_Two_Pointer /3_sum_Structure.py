#use the concept of two pointers and find the valid triplets which equals to zero.

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
print(nums)

result = []

for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            result.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
print(result)
