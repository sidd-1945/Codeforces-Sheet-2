while True:
    a,b = map(int,input().split())
    sum = 0
    if a > 0 and b > 0:
        c = min(a,b)
        d = max(a,b)
        for i in range(c,d+1):
            sum += i
        for j in range(c,d+1):
            print(j,end = " ")
        print("sum =",end = "")
        print(sum)
    else:
        break         