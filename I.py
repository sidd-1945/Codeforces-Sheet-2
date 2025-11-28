a = int(input())

original = a
rev = 0

while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10


if rev == original:
    print(rev)
    print("YES")
else:
    print(rev)
    print("NO")


