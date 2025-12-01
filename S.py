a = int(input())

for _ in range(a):
    b,c = map(int,input().split())
    d = min(b,c)
    e = max(b,c)
    sum = 0
    for i in range(d+1,e):
        if i % 2 != 0:
            sum += i 
    print(sum)        