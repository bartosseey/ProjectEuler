summ = 0

a = 0 
b = 1

while b < 4000000:
    c = a + b
    a = b 
    b = c
    if c%2 == 0:
        summ += c

print(summ)