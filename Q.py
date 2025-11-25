# a = int(input())

# for _ in range(a):
#     b = int(input())
#     c = []
#     while b > 0:
#         k = b%10
#         c.append(k)
#         b = b//10
#     space = ""
#     for i in c:
#         print(f"{space}{i}",end="")
#         space=" "   
a = int(input())

for _ in range(a):
    b = int(input())
    c = []

    if b == 0:
        c.append(0)
    else:
        while b > 0:
            k = b % 10
            c.append(k)
            b = b // 10

    space = ""
    for i in c:
        print(f"{space}{i}", end="")
        space = " "
    print()
