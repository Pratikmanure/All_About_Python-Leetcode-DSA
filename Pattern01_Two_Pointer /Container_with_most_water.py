#find the maximum value of water which a container can hold

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0
right = len(height) - 1
maximum = 0

while left < right:
    water = min(height[left], height[right]) * (right - left)

    if water > maximum:
        maximum = water

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(maximum)
