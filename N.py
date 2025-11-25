b = input()
a = int(input())          
nums = input().split()    

result = []

for i in range(a):        
    result.append(int(nums[i]))
for i in range(len(result)):
    for j in range(result[i]):
        if b == '+':
            print('+',end = "")
        elif b == '-':
            print('-',end = "")
        elif b == '*':
            print('*',end = "")
        else:
            print('/',end = "")     
    print()                  