

longestSeries = 0
longestSeriesii = 0

for ii in range(13,1_000_000):
    series=0
    n = ii
    while n != 1:
        if series>1_000_000:
            break
        elif n%2==0:
            n = n/2
            series +=1

        elif n%2==1:
            n=3*n+1
            series +=1
    print(ii, series)
    if series > longestSeries:
        longestSeries = series
        longestSeriesii = ii

print(longestSeriesii, longestSeries)

