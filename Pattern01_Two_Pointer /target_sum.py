arr = [1, 2, 3, 4, 6, 8, 9]
target = 11

left = 0
right = len(arr) - 1

while left < right:
    sum = arr[left] + arr[right]
    
    if sum < target:
        left += 1
    elif sum > target:
        right -= 1
    elif sum == target:
        break

print("Found")
