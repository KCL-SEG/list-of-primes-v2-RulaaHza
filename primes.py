"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError('Positive number expected for list size')
    
    prime_list = []
    num = 2

    while len(prime_list) < number_of_primes:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
        num += 1

    return prime_list
