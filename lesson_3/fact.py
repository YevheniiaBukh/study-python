n = 8
fact = 1
for i in range(1, n + 1):
    fact *= i
    print(f"Current number: {i}, Factorial so far: {fact}")
print(f"Final factorial: {fact}")