def ways_to_attend_class(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 8
    if n == 4:
        return 15

    return ways_to_attend_class(n-1) + ways_to_attend_class(n-2) + ways_to_attend_class(n-3) + ways_to_attend_class(n-4)




n = 6

total_ways = ways_to_attend_class(6)

probality = str(pow(2,n) - total_ways) + "/" + str(total_ways)

print(total_ways, probality)
