# 5
# -5 0 -3 -4 12

# Even: 3
# Odd: 2
# Positive: 1
# Negative: 3
count = int(input())
a = list(map(int, input().split()))
even = 0
odd = 0
pos = 0
neg = 0

for num in a:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", pos)
print("Negative:", neg)


