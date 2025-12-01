N,A,B = map(int,input().split())
sum = 0
for i in range(1,N+1):
    j = i
    dsum = 0
    while j > 0:
        k = j % 10
        dsum+=k
        j=j//10
    if dsum >= A and dsum <= B:
        sum+=i    
print(sum)

