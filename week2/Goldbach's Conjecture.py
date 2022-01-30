# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Goldbach's Conjecture

# * Link: https://open.kattis.com/contests/guve43/problems/goldbach2 ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-01 21:50:06

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.75 */

data = int(input())
primes = [2] #stores all prime numbers
lastInput = 3
map = {"2":True}
for i in range(data):
    output = [] #stores the end output in strings
    dataNumber = input()
    counter = 0 
    for num in range(lastInput , int(dataNumber) + 1, 2):
       # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               map[str(num)] = True
               primes.append(num)
        
    for prime1 in primes: 
        if prime1 > int(dataNumber)/2:
            break
        else:
            prime = int(dataNumber) - prime1
            if str(prime) in map:
                counter += 1
                output.append(str(prime1) + "+" + str(prime))
                
    print(dataNumber + " has " + str(counter) + " representation(s)")
    for message in output:
        print(message)
    lastInput = int(dataNumber) + 1