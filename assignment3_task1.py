def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = 5     
result = factorial(num)
print("Factorial of", num, "is", result)
