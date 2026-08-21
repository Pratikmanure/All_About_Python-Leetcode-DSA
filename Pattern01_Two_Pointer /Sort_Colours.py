#sort the given array considering 3 colours using dutch national flag method.

nums = [2, 0, 2, 1, 1, 0]

low = 0
mid = 0
right = len(nums) - 1

while mid <= right:
    if nums[mid] == 0:
        nums[low],nums[mid] = nums[mid],nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
         mid += 1
    else:
        nums[right],nums[mid] = nums[mid],nums[right]
        right -= 1

print(nums)

#O/P = [ 0, 0, 1, 1, 2, 2]
