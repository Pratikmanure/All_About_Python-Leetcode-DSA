#sort the duplicates by approving atmost 2 duplicates

nums = [1,1,1,2,2,3]

slow = 2

for fast in range(2, len(nums)):

    if nums[fast] != nums[slow - 2]:
        nums[slow] = nums[fast]
        slow += 1

print(nums[:slow])
