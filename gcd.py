import inspect

def gcd(a,b):
    # Returns the greatest common denominator of a and b using the Euclidean Algorithum
    while b:
        a, b = b, a%b
    return a

def ThreeNplusOne(N):
    # Applies the 3N+1 algoithm, and prints the number of items in the series 
    # and the final non-repeated value in the series"
    series = []
    while N not in series:
        series.append(int(N))
        if N%2 != 0:
            N = 3*N+1
        else:
            N = N/2
    #print(len(series), 'terms terminating at', series[-1])
    return(len(series), series[-1])


def Steps(a, b, m):
    # Apply the 3n+1 algorithm to the number (a*k + b)
    # print the first m iterations
    for i in range(m):
        if (a+b)%2 == 0:
            a = int(a/2)
            b = int(b/2)
            print("{}*k+{}".format(a, b))
            i += 1
        else:
            a = int(3*a)
            b = int(3*b+1)
            i += 1
            print("{}*k+{}".format(a, b))


def StepsLength(a, b):
    # Apply the 3n+1 algorithm to the number (a*k + b)
    # print the length of the series, followed by the series
    series = []
    while [a,b] not in series:
        series.append([a,b])
        if (a+b)%2 == 0:
            
            a = int(a/2)
            b = int(b/2)
            
          
        else:
            
            a = int(3*a)
            b = int(3*b+1)
        
        
    series.pop(0)        
    print("len =",len(series))
    print(*series, sep="\n")
    
def gcd_detailed(a,b):
    # Returns the greatest common denominator of a and b using the Euclidean Algorithum
    while b:
        print("a = {}, b = {}, (a)mod(b) = {}".format(a,b,a%b))
        a, b = b, a%b
    return a

