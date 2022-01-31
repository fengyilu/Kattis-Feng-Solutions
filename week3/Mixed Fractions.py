# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Mixed Fractions

# * Link: https://open.kattis.com/contests/qkxmff/problems/mixedfractions;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-08 17:34:36


# # Status : Accepted 

# # Runtime: 0.09 */

#simple math formular to get needed numbers 
def mixedFraction(dataInputs):
        rest = int(dataInputs[0])% int(dataInputs[1])                
        ganzZahl = int(dataInputs[0]) // int(dataInputs[1])         
        print(str(ganzZahl) +" "+ str(rest) + " / " + dataInputs[1] )

#reading inputs and define breaking condition 
while True:
    n = input().split()
    if n[0]== "0" and n[1]=="0":
        break
    mixedFraction(n)