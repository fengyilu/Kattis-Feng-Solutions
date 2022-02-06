# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Goldbach's Conjecture

# * Link: https://open.kattis.com/contests/guve43/problems/goldbach2 ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-01 21:50:06

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.75 */
#representation of a number x as a sum of two primes. 

data = int(input())
primes = [2] #stores all prime numbers
#lastInput is used for optimising the Runtime, we dont have to check the same numbers again in the for loop
lastInput = 3
map = {"2":True}
for i in range(data):
    output = [] #stores the end output in strings
    #dataNumber is the prime that is given by the problem 
    dataNumber = input()
    #counts how many representation we have for dataNumber
    counter = 0 
    for num in range(lastInput , int(dataNumber) + 1, 2):
       # all prime numbers are greater than 1
       if num > 1:
           #starting the for loop from 2 to num, we break the loop if num modulo i(current for loop index) equals 0 that means num is not a prime
           for i in range(2, num):
               if (num % i) == 0:
                   break
           #if num is a prime then we put it into our map and give it a value "True"
           else:
               map[str(num)] = True
            #adding the prime into our prime array
               primes.append(num)

    for prime1 in primes: 
        if prime1 > int(dataNumber)/2:
            break
        else:
            #we check if one of the prime numbers in our prime array substracted from the given value of the problem is a prime, if thats the case we have found a reprensetation of the given prime
            prime = int(dataNumber) - prime1
            if str(prime) in map:
                counter += 1
                output.append(str(prime1) + "+" + str(prime))
                
    print(dataNumber + " has " + str(counter) + " representation(s)")
    for message in output:
        print(message)
    lastInput = int(dataNumber) + 1