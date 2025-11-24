a = int(input())
found = -1
for i in range(1,a+1):
    if i % 2 == 0:
        print(i)
        found = 1
if found != 1:
    print(-1)         