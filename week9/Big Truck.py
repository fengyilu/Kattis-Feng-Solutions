# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Big Truck

# * Link: https://open.kattis.com/problems/bigtruck;

# * @author: Feng Yi Lu

# * @version 1.0, 2022-01-16 19:08:01

# * Method : Dijkstra-Algorithm

# # Status : Accepted 

# # Runtime: 0.11*/
# output the length of a shortest path from location 1 to location n, followed by the maximum number of items you can pick up along the way.

#anzahl an städte
numberCity = int(input())

# Amount to pick up in city i for each city
pickups = [int(x) for x in input().split()]

#anazhl an wege
numberRoads = int(input())

# index[i][j] stores the weight of the edge from city i to city j
matrix = [[float('inf') for _ in range(numberCity)]for _ in range(numberCity)]

# Fill matrix
for _ in range(numberRoads):
    a, b, d = [int(x) for x in input().split()]
    #input starts at 1 not 0 => Remove 1 
    matrix[a-1][b-1] = d


# Initialize dijkstra costs to get to each city, starts with all infinity
costs = [float('inf') for _ in range(numberCity)]

# Will store max amount of items that can collected on the path to each city i
collected = [0 for _ in range(numberCity)]

# start with the first city 
costs[0] = 0
collected[0] = pickups[0]

#store all visited cities
seen = set()

# Returns the next node to visit. The next node is always the node that has the lowest cost to get to out of all nodes that have NOT been visited yet.node_id = None
def visit_next_node():
    node_cost = float('inf')
    for i in range(numberCity):
        if i not in seen and costs[i]<node_cost:
            node_id = i
            node_cost = costs[i]
    return node_id

not_visited_node = visit_next_node()

# While we still have unvisited nodes:
while not_visited_node is not None:
    # Calculate the costs to all reachable nodes from the current node not_visited_node: The is just the costs to get to the current node plus the costs from that node to each respective node
    cost_from_not_visited_node = [matrix[not_visited_node][i] + costs[not_visited_node] for i in range(numberCity)] 
    for i in range(numberCity):
        # If we found a cheaper way to get to node i:
        if costs[i] > cost_from_not_visited_node[i]:
            costs[i] = cost_from_not_visited_node[i] # update cost to get to node i
            # Set amount of collected items
            collected[i] = collected[not_visited_node] + pickups[i] 
        # If we didn't find a cheaper way, but a way with the same cost and we can collect more items on this way, we will use that amount
        elif costs[i] == cost_from_not_visited_node[i] and \
            collected[i] < collected[not_visited_node] + pickups[i]:
            collected[i] = collected[not_visited_node] + pickups[i]
    seen.add(not_visited_node)
    not_visited_node = visit_next_node()


# If no way to the destination node in costs[-1] there still will be infinity
if costs[-1] == float('inf'):
    print("impossible")
else:
    # Otherwise we print the cost and number of collected items of the las node
    print(costs[-1], collected[-1])



    