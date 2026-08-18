#use the concept two pointer to find the valid quadruple of the given array

nums = [1, 0, -1, 0, -2, 2]
target = 0

nums.sort()

result = []

for i in range(len(nums) - 3):

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, len(nums) - 2):

        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = len(nums) - 1

        while left < right:

            total = nums[i] + nums[j] + nums[left] + nums[right]

            if total < target:
                left += 1

            elif total > target:
                right -= 1

            else:
                result.append([
                    nums[i],
                    nums[j],
                    nums[left],
                    nums[right]
                ])

                left += 1
                right -= 1

print(result)
