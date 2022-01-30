# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Mirror Images

# * Link: https://open.kattis.com/contests/qkxmff/problems/mirror;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-11 12:35:26

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.08 */

testCases = input()
output = []

#function to get needed output format
def outputFormat(case):
    print("Test "+ str(case+1))
    for element in output:
        print(element)

#simple mirroring of line of string by using python syntax and inserting the line backwards into a array
for case in range(int(testCases)):
    orderOfChar = input().split()
    for row in range(int(orderOfChar[0])):
        mirror = input()[::-1]
        output.insert(0,mirror)
    outputFormat(case)
    output.clear()
    