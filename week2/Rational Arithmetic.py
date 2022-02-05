# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Rational Arithmetic

# * Link: https://open.kattis.com/contests/guve43/problems/rationalarithmetic ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-07 21:15:47

# * Method : GGT größte gemeinsamer teiler 

# # Status : Accepted 

# # Runtime: 0.75 */


firstInput = int(input())
def ggT(x, y):
   z = x % y
   if z == 0:
      return y
   return ggT(y, z)
   
for iteration in range(4):
    data = input().split()
    if data[2] == "+" or data[2]== "-":
        zaehler1 = int(data[1]) * int(data[3])
        nenner = int(data[1]) * int(data[4])
        zaehler2 = int(data[0]) * int(data[4])
        addiert = zaehler1 + zaehler2
        subrahiert = zaehler2 - zaehler1
        if data[2]== "+":
            print(str(addiert/ggT(addiert, nenner)).replace(".0","") +" / " +  str(nenner/ggT(addiert, nenner)).replace(".0",""))
        else: 
            print(str(subrahiert/ggT(subrahiert, nenner)).replace(".0","") +" / " + str(nenner/ggT(subrahiert, nenner)).replace(".0",""))
    if data[2]== "/" and data[1]!= "0" and data[3]!= "0" and data[4]!= "0":
        zaehler = (int(data[0]) * int(data[4]))
        nenner = (int(data[1]) * int(data[3])) 
        print(str(zaehler/ ggT(zaehler, nenner) ).replace(".0","") + " / " + str(nenner / ggT(zaehler, nenner)).replace(".0",""))
    if data[2] == "*":
        nenner = int(data[1]) * int(data[4])
        zaehler = int(data[0]) * int(data[3])
        print(str(zaehler / ggT(zaehler, nenner)).replace(".0","") + " / " + str(nenner / ggT(zaehler, nenner)).replace(".0",""))

        