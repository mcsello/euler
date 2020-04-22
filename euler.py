def is_prime(n, primes_smaller=None):
    if primes_smaller:
        for i in primes_smaller:
            if n%i == 0:
                return False    
        return True
    else:
        if n == 2 or n == 3:
            return True
        if n == 1 or n%2 == 0: 
            return False
        for i in range(
            3, 
            int(n**0.5) + 1,
            2
        ):
            if n%i == 0:
                return False    
        return True

def n_digits(n):
    return len(str(n))