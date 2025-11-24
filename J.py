a = int(input())
primes = []
for f in range(2,a+1):
    prime = True
    for i in range(2,f):
        if f % i == 0:
            prime = False
            break
    if prime:
        primes.append(f)
space = ""
for i in primes:
    print(f"{space}{i}",end="")
    space=" "
    