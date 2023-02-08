a = int(input())
b = int(input())

def is_prime(n):
    if n == 1:
        return("{} is not prime".format(n))
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return("{} is not prime".format(n))
    print(n)

for i in range(a,(b + 1)):
    is_prime(i)