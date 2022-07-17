import math

x = str(int(float(math.pow(2, 1000))))
sum = 0
for ii in x:
    sum += int(ii)
print(sum)