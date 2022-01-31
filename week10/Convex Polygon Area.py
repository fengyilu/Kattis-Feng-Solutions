# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Convex Polygon Area

# * Link: https://open.kattis.com/contests/pvcykt/problems/convexpolygonarea;

# * @author: Feng Yi Lu

# * @version 1.0, 2022-01-23 15:59:55

# * Method : Formular for area calculation of convex polygon

# # Status : Accepted 

# # Runtime: 0.10*/


#first input describes the number of polygons
for i in range(int(input())):
    x_cords = list()
    y_cords = list()
    polyglon = input().split(" ")
    n = int(polyglon[0])
    polyglon.pop(0)
    counter=0
    #adding the cordianates into a x or y array
    for k in range(n):
        for element in polyglon:
            if counter == 0: 
                x_cords.append(int(element))
                counter +=1
            else: 
                y_cords.append(int(element))
                counter = 0
    area = 0
    #calculating the area of the polygon 
    for x in range(n-2):
        v1,v2,v3 = 0,x+1,x+2
        #formular for calculation
        tr_area = abs(0.5*(x_cords[v1]*(y_cords[v2]-y_cords[v3])+
                    x_cords[v2]*(y_cords[v3]-y_cords[v1])+
                    x_cords[v3]*(y_cords[v1]-y_cords[v2])))
        area += tr_area
    print (area)