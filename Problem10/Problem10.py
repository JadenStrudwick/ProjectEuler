# Prime checker
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

primes = []
n = 0

while n < 2000000:
    n += 1
    if is_prime(n) == True:
        primes.append(n)
        print(n)

print(primes)
print(sum(primes))