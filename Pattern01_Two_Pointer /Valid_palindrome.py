#check if the given string is valid palindrome by skipping atmost 1 letter.

s = "abca"

def is_palindrome(left, right):
    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        if s[left] == s[right]:
            left += 1
            right -= 1

        else:
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

    return True


print(valid_palindrome(s))
