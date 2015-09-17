import sys
import math


def nth_prime(N):
    primecount = 0;
    number = 2;
    result = number;
    listOfPrimes = []
    while primecount < N:
        if (number == 2 and primecount == 0):
            result = number
            primecount += 1
            listOfPrimes.append(number)
        else:
            if(number == 2):
                number += 1
            else:
                number += 2
            if isPrime(number, listOfPrimes) == True:
                primecount += 1
                listOfPrimes.append(number)
                result = number

    # TODO: Write code here that computes the Nth prime
    # result = N * 2 # e.g. this code finds the Nth even number
    return result

def isPrime(number, listOfPrimes):
    numberIsPrime = True
    for num in filter(lambda x: x <= math.sqrt(number), listOfPrimes):
        if number%num == 0:
           numberIsPrime = False
           break
    return numberIsPrime
        

def test_run():
    print(nth_prime(253))    

if __name__ == "__main__":
    test_run()
