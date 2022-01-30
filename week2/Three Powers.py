# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Three Powers

# * Link: https://open.kattis.com/problems/threepowers ;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-11-29 13:37:08

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.10 */

#solving problem with bit shifting
def print_set(n):
    shifts = 0
    elements = 0
    print('{', end='')
    while n > 0:
        if n & 1 == 1:
            if elements == 0:
                print(' {:d}'.format(3**shifts), end='')
            else:
                print(', {:d}'.format(3**shifts), end='')
            elements += 1
        n >>= 1
        shifts += 1
    print(' }')

while True:
    n = int(input())
    if n == 0:
        break
    print_set(n-1)