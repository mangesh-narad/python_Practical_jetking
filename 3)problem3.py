def is_palindrome(n: int) -> bool:
    if n < 0:
        return False
    return str(n) == str(n)[::-1]
number = 121
print(is_palindrome(number))
