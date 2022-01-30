# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Planting Trees

# * Link: https://open.kattis.com/contests/nytf6n/problems/plantingtrees;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-12-20 15:23:33

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.08*/

# "a" array that saves the days that a seed needs to grow
a = []
counter = 0
days = 1
#first input is not needed in my solution
leer = input()

#filling the array
a = [int(t) for t in input().split()]

#list is sorted reversed (or sorted in Descending order)
a.sort(reverse= True)

#earliest day when the party can be organized when all trees are grown = adding up the days that the seed need and the days that he are spending to plant them 
for index, seed in enumerate(a):
    seed += days
    seed += 1
    a[index] = seed
    days+=1
#check the highest number inside of "a" this is the ealiest time when the party can start after max(a) days
output = max(a)
print(output)