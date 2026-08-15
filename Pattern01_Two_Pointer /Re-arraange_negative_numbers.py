#re-arrage array by moving non-negative numbers to front and negative numbers to last

arr = [3, -1, 5, -2, 8, -4]

slow = 0
fast = 0

while fast < len(arr):
    if arr[fast] >= 0:
        arr[slow],arr[fast] = arr[fast],arr[slow]
        fast += 1
        slow += 1
    else:
        fast += 1
print(arr)
    
