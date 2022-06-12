
largest = 0
largestcounter = 0

def palindrome(x):
    counter=0
    string = str(x)
    for ii in range(int(len(string)/2)):
        if string[ii]!=string[-ii-1]:
            break
        counter +=1
    return counter


for ii in range(999, 99, -1):
    for jj in range(ii, ii-100, -1):
        product = ii*jj
        lengthofpal = palindrome(product)
        if lengthofpal>largestcounter:
            largestcounter = lengthofpal
            largest = product

print(largestcounter, largest)