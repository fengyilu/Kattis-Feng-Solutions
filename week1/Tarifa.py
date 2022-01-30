# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Tarifa

# * Link: https://open.kattis.com/contests/kp9a7t/problems/tarifa ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-10-28 14:01:34

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.06 */

oneMonth = int(input())
rest = 0
#calculate how many megabytes he has left in each Month this will be add onto "rest" to determine how many he has available in the N+1 month
for i in range(int(input())):
    rest += (oneMonth- int(input()))
print(rest + oneMonth)