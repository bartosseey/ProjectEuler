def isDivisible(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    return True



number = 2520
while True:
    if isDivisible(number):
        break
    number += 2520

print(number)