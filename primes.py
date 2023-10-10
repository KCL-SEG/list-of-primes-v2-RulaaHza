"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    try:
        list = []
        num =1
        if(number_of_primes >0):
        
            while( len(list) < number_of_primes):
                if num > 1:
                   for i in range(2, num):
                       if (num % i) == 0:
                           break
                   else:
                       list.append(num)
                num+=1
            return list
    except ValueError:
        print('Positive number expected for square root operation')
