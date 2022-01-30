# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: How Many Digits?

# * Link: https://open.kattis.com/contests/zr36jo/problems/howmanydigits;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-17 15:56:32

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.13 */


import math
def generateOutput(n):
    if (n < 0):
        return 0
 
    # using formular that was found online for this case
    if (n <= 1):
        return 1
    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0))
 
    return math.floor(x) + 1

    #raeding input and define break condition
while True:
    try:
        
        n = int(input())
        print(generateOutput(n))
    
    except EOFError:
        break
    

    