# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Exact Change

# * Link: https://open.kattis.com/contests/pe4egm/problems/exactchange2;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-12-06 10:27:20

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.26 */

coins = []
#how many test cases we have 
test_cases_no = int(input())

while test_cases_no > 0:
  #filling table with 30001  times "infinity" 
  table = [float('inf')] * 30001
  #the first index of the array is overwirtten with 0 
  table[0] = 0

  # the price we need to pay
  price = int(input())
  # the number of coins
  coins_no = int(input())

#filling the coin array
  for i in range(coins_no):
    coins.append(int(input()))

  #iterate through every coin in our coin array
  for coin in coins:
    crt_price = price - 1
    while crt_price >= 0:
      if table[crt_price] == float('inf'):
        crt_price -= 1
        continue
      if table[crt_price + coin] > table[crt_price] + 1:
        table[crt_price + coin] = table[crt_price] + 1

      crt_price -= 1

  i = price
  while True:
    if table[i] != float('inf'):
      break
    i += 1

  print(i, table[i])

  test_cases_no -= 1
  #reset the coins array for next case 
  coins = []