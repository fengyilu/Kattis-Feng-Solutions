# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: N-sum

# * Link: https://open.kattis.com/contests/kp9a7t/problems/nsum ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-10-28 13:53:33

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.05 */

data = int(input())
numbers = input().split()
result= 0
for number in numbers:
    result += int(number)

print(result)

