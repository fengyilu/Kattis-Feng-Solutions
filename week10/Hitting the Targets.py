# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Hitting the Targets

# * Link: https://open.kattis.com/contests/pvcykt/problems/hittingtargets;

# * @author: Feng Yi Lu

# * @version 1.0, 2022-01-24 09:41:14

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.06*/




#calculating how many hits we have 
def howManyHits():
    for i in range(num_shots):
        hits = 0
        x, y = [int(x) for x in input().split()]

#check if the hit coordinates are in between of the targets
        for x1, y1, x2, y2 in rectangles:
            if x1 <= x <= x2 and y1 <= y <= y2:
                hits += 1

        for x_center, y_center, r in circles:
            # Pythagoras
            if (x - x_center) ** 2 + (y - y_center) ** 2 <= r ** 2:
                hits += 1
        print(hits)

#getting the targets
def targets():
    for i in range(num_targets):
        data = input().split()

        if data[0] == "rectangle":
            rectangles.append([int(x) for x in data[1:]])
        else:
            circles.append([int(x) for x in data[1:]])



rectangles = []
circles = []

num_targets = int(input())
targets()
num_shots = int(input())
howManyHits()