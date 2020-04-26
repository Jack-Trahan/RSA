#!/usr/bin/env python
'''
Sieve of Eratosthenes Program
Finds all Prime number in range 0...n

@author: Jack Trahan
'''

def sieve(n):
    '''
    Create a boolean array "prime[0..n]" and initialize
    all entries in it as true. A value in prime[i] will
    finally be false if 'i' is Not a prime, else true.
    
    Example
    ----------------
    >>>sieve(10)
    
    2
    3
    5
    7
    '''
    prime = [True for i in range(n+1)]
    prime[1] = False
    
    p = 2
    while p**2 <= n:
        if prime[p] == True:
            for i in range(p*2, n+1, p): # mark all multiples of p as False
                prime[i] = False
        p += 1
        
    # Print all Primes from 0...n
    for i in range(1, n+1):
        if prime[i] == True:
            print(i)

def main():
    print("Find all Prime numbers from 1 to n")
    while True:
        try:
            n = int(input("Enter an integer for n: "  ))
        except ValueError:
            print("n must be a valid integer!\n")
        else:
            sieve(n)
            if input("Do another (y/n)? ").lower() != 'y':
                print("Have a nice day! Goodbye...")
                break
    
    
if __name__ == '__main__':
    main()  

        