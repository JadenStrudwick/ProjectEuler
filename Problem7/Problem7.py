# Prime checker
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

primes = []
n = 0

while len(primes) < 10001:
    n += 1
    if is_prime(n):
        primes.append(n)
        print(len(primes))

print(primes[10000])