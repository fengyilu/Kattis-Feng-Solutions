# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Pot

# * Link: https://open.kattis.com/contests/kp9a7t/problems/pot ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-10-26 15:20:49

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.05 */

data = input()
y = int(data)
result = 0
for i in range(y):
    x = input()
    quadrat = int(x[-1])
    x = int(x[:-1])
    result+= x**quadrat
    
print(result)
