n = int(input())
def is_prime(n):
    if n == 1: return False
    result = True
    for i in range(2, n):
        if i >= ((n // 2) + 1):
            break
        if n % i == 0:
            result = False
            break
    return result
 

def get_lower_prime_count(n):
    counter = 0
    for i in range(1, n):
        if is_prime(i):
            counter += 1
    return counter


def get_divisor(n):
    counter = 0
    for i in range(1, n):
        if i >= ((n // 2) + 1):
            break
        if n % i == 0 and is_prime(i):
            counter += 1

    return counter


stones = list()
price = 0
for i in range(n):
    stones.append(int(input()))

for stone in stones:
    if is_prime(stone):
        price += get_lower_prime_count(stone)
    else:
        price += get_divisor(stone)

if is_prime(price):
    price = price - get_lower_prime_count(price)
    print(price)
else:
    price = price - get_divisor(price)
    print(price)

