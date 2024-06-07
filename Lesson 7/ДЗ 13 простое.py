def is_palindrom(n):
    s = str(n)
    return s == s[::-1]

print(is_palindrom(0))
print(is_palindrom(1))
print(is_palindrom(-1))
print(is_palindrom(50))
print(is_palindrom(505))
print(is_palindrom(-505))

