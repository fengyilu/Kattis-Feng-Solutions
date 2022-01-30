# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Triangle Area

# * Link: https://open.kattis.com/contests/kp9a7t/problems/triarea ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-10-27 10:46:58

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.05 */

data = input().split()
#formualr for area of a triangle
area = int(data[0]) * int((data[1]))
print(area/2)