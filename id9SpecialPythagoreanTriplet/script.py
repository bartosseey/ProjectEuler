def find_product(sum):
     for a in range(1, sum):
         for b in range(1, sum - a):
             c = sum - a - b
             if a**2 + b**2 == c**2:
                   print(a*b*c)
                   return a*b*c


find_product(1000)
