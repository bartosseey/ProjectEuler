import functools

@functools.lru_cache
def fibonacci(n):
    a = 0
    b = 1
     
    if n == 0:
        return 0
       
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

x = 0
counter = 1
while len(str(x)) < 1000:
    x = fibonacci(counter)
    counter += 1

print(counter)
print(x)
print(len(str(x)))
