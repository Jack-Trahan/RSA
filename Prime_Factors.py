import random
from functools import reduce

def isPrime(n):
    # Return True if n is prime using the Miller-Rabin Primality test
    
    '''
    How It Works
    1) Choose an integer a < n,
    2) Let n-1 = (2**s)*d where d is odd
    3) By Fermat's Little Theorem and Euclid's Lemma,
        if 
            a**d ≢ 1 mod n 
        and
            a**(2**r *d) ≢ -1(mod n) for all (0 ≤ r ≤ s−1)
        then
            n is compostie and a is a witness.
            Otherwise n may, or may not be prime. Thats why we test multiple, random values of a.
    '''
    
    # If n is even and n != 2, then n is not prime
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    
    # Find the values of s and d for n-1 = (2**s)*d
    s = 0
    d = n-1
    while True:
        quotient, r = divmod(d,2)
        if r == 1: break
        s += 1
        d = quotient
        
    # test if a is a witness for n being composite
    def test_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
    
    # Select and test for different random a values
    for _ in range(4):
        a = random.randint(2,n-1)
        if test_composite(a):
            return False
 
    return True # no base tested showed n as composite, therefore n is supposed to be prime
        
def PrimeFactors(n):
    # returns the prime factorization of n
    
    # If (n < 2) or n is prime, return n
    if n <= 2:
        return n
    if isPrime(n):
        return n
    
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i            
            factors.append(i)
            
    if n > 1:
        factors.append(n)
    return factors

def Phi(n):
    # return the output from Euler's totient function of n
    
    # consider only distinct prime factors of n
    distinct_prime_factors = set(PrimeFactors(n))
    # calculate phi using n*(1-1/P1)(1-1/p2)...(1-1/Pk) where P is a distinct prime factor of n
    return int(reduce(lambda x, y: x*y, map(lambda x: (1-(1/x)), distinct_prime_factors))*n)

