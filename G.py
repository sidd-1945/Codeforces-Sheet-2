a = int(input())

for _ in range(a):
    b = int(input())
    fact = 1
    for i in range(1, b + 1):
        fact *= i
    print(fact)

