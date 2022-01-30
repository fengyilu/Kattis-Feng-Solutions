# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Quality-Adjusted Life-Year

# * Link: https://open.kattis.com/contests/kp9a7t/problems/qaly ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-10-26 15:15:02

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.06 */

data = input()
iterations = int(data)
a = 0
#each inputline consists of 2 floats, the floats in a row will be mutiplied and the product will be added to a
for x in range(iterations):
    inputs = input().split()
    y = float(inputs[0]) * float(inputs[1])
    a+= y

print(a)