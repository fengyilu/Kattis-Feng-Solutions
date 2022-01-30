# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Jumbo Javelin

# * Link: https://open.kattis.com/contests/kp9a7t/problems/jumbojavelin ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-01 13:08:37

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.05 */

#calculating the total length if all javelin would be combined / keeping in mind that on the connecting end that they lose cm 
data = int(input())
cm = 0
for i in range(data):
    cm += int(input())

print(cm-(data-1))

