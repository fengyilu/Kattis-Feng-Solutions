# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Planina

# * Link: https://open.kattis.com/contests/kp9a7t/problems/planina ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-10-28 13:42:37

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.05 */

data = int(input())
number = 2
result = 0
#its a sequence as follow:
for i in range(data):
    number = number + (number -1)
    result = number * number
print(result)