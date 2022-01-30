# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Exact Change

# * Link: https://open.kattis.com/contests/pe4egm/problems/exactchange2;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-12-06 10:27:20

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.26 */

coins = []
test_cases_no = int(input())
while test_cases_no > 0:
  table = [float('inf')] * 30001
  table[0] = 0

  # the price we need to pay
  price = int(input())
  # the number of coins
  coins_no = int(input())

  for i in range(coins_no):
    coins.append(int(input()))
    # coins = coins + [int(input())]

  # for i in range(coins_no):
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
  coins = []