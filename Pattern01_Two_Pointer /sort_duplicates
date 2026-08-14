#Re-arrange the duplicate values from the array and sort them.

arr = [1, 1, 2, 2, 3, 3, 4]

slow = 0
fast = 1

while fast < len(arr):
    if arr[fast] == arr[slow]:
        fast += 1
    elif arr[fast] != arr[slow]: 
        slow += 1
        arr[slow] = arr[fast]
        fast += 1

print(arr)
