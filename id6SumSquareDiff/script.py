sum1 = 0
for i in range(1, 101):
    sum1 += i

sum1 = sum1**2
sum2 = 0
for i in range(1, 101):
    sum2 += i**2

print(sum1-sum2)