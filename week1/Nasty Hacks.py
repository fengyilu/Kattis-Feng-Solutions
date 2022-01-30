# Ausgewählte Probleme aus dem ACM Programming Contest  SS 2018 

# * Problem: Nasty Hacks

# * Link: https://open.kattis.com/contests/kp9a7t/problems/nastyhacks ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-01 13:59:14

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.06 */

amount = int(input())
feedback = ["advertise", "does not matter", "do not advertise"]
for i in range(amount):
    data = input().split()
    number = int(data[1]) - int(data[2])
    mainProfit = int(data[0])
    if number > mainProfit:
        print(feedback[0])
    elif number == mainProfit:
        print(feedback[1])
    elif number < mainProfit:
        print(feedback[2])