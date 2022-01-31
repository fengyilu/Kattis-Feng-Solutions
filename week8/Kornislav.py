# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Kornislav

# * Link: https://open.kattis.com/contests/nytf6n/problems/kornislav;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-12-20 15:47:56

# # Status : Accepted 

# # Runtime: 0.05 */

#reading input into array "a"
a = [int(t) for t in input().split()]

#sort array and spreading value into 2 new arrays, one contains the smaller number of each possible side of a rectangle and one the bigger number
a.sort()
aklein=[a[0], a[1]]
aGroß= [a[2], a[3]]

#now we compare in the array of the smaller number which of boths numbers is smaller / the same with the array with the bigger numbers 
akleinereZahl = min(aklein)
agroßeZahl = min(aGroß)

#these two numbers mutiplied are the size of the possible enclosed rectangle that can be created 
output = agroßeZahl * akleinereZahl

print(output)