#move all the zeroes at the end of array and non-zero to the start

nums = [0, 1, 0, 3, 12]

slow = 0
fast = 0

while fast < len(nums):
    if nums[fast] != 0:
        nums[slow],nums[fast] = nums[fast],nums[slow]
        fast += 1
        slow += 1
    else:
        fast += 1
print(nums)
