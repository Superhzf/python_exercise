# The question is that given a number n, determine whether it is
# a prime number or not

ddef isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 1
    while 6 * i - 1 <= n:
        if 6*i-1 == n or 6*i + 1 == n:
            return True
        i += 1

    return False
