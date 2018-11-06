import math

num = int(input())

def is_prime(n):
    if n <= 1:
        return ('Not prime')
    if n <= 3 and n > 1:
        return ('Prime')
    for i in range(2, int(math.sqrt(n))):
        if n % i is 0:
            return ('Not prime')
    return ('Prime')


for _ in range(num):
    nn = int(input())
    print (is_prime(nn))
