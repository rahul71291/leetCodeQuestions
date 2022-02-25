def findSum(n,m):
    bit_sum = 0 
    res = 0
    multiplier = 1
    while(n  or m ):
        bit_sum = (n%10) + (m%10)
        bit_sum %= 10
        res = (bit_sum * multiplier) + res
        multiplier *= 10
        n /= 10
        m /= 10
    return res

n = 121
m = 999

print(findSum(n,m))

