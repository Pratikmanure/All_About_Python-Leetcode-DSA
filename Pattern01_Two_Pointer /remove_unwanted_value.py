# Re-arrange the array by moving unwanted element/val to the last and useful ones to front.

nums = [3, 2, 2, 3]
val = 3

slow = 0
fast = 0

while fast < len(nums):
    if nums[fast] != 3:
        nums[slow],nums[fast] = nums[fast],nums[slow]
        fast += 1
        slow += 1
    else:
        fast += 1
print(nums)
