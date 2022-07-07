def factorial(a):
    if a == 1:
        return 1
    else:
        s = a*factorial(a-1)
        return s
print(factorial(5))
