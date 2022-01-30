# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Magic Trick

# * Link: https://open.kattis.com/contests/kp9a7t/problems/magictrick ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-01 13:56:36

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.05 */

data = input()
counter = {}
#checking if we have same letters, as soon if there are two of the same letter we cant say to 100% if something got switch or not (using dictionary)
for i in data:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

checker = False
for i in counter:
    if counter[i] >1:
        checker = True

if checker == True: 
    print(0)
else:
    print(1)
          