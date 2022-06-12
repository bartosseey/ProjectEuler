import math

def prime(n):
    while n % 2 ==0:
        n=n/2
    
    for ii in range(3, int(math.sqrt(n))+1, 2):
        while n%ii ==0:
            print(ii)
            n = n/ii

    if n > 2:
        print(n)

prime(600851475143)
