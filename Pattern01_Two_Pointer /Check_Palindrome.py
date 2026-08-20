s = "maddam"

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:

    if s[left] != s[right]:
        is_palindrome = False
        break
    else:
        left += 1
        right -= 1

if is_palindrome == True:
    print("it is a palindrome")
else:
    print("its not a palindrome")

#O/P = "it is a palindrome"
