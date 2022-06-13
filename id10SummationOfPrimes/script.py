n = int(input('n = '))
summ = 0
if n < 2:
    print("Brak liczb pierwszych w podanym zakresie")
else:
    lst = [False] * (n + 1)
    i = 2
    while i * i <= n:
        if  not lst[i]:
            j = i * i            
            while j <= n:
                lst[j] = True
                j += i
        i += 1
    for i in range(2, n+1):
        if not lst[i]:
            summ += i

print(summ)