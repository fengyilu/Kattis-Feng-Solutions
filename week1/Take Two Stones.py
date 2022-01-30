# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Take Two Stones

# * Link: https://open.kattis.com/contests/kp9a7t/problems/twostones ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-10-26 15:17:56

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.06 */

data = int(input())
number = data%2

if number == 0:
    print("Bob")
else:
    print("Alice")