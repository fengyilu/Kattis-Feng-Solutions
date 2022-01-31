# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Torn To Pieces

# * Link: https://open.kattis.com/contests/rxgmfr/problems/torn2pieces;

# * @author: Feng Yi Lu

# * @version 1.0, 2022-01-14 16:19:24

# * Method : dijkstra

# # Status : Accepted 

# # Runtime: 0.06*/


# function for building the graph to have all necessary connections of each stations
def build_graph():
    for x in range(no_nodes):
        data = input().split()
        child_nodes = {}
        for child in data[1:]:
            child_nodes[child] = 1
            if child not in graph:
                graph[child] = {data[0]: 1}
            else:
                graph[child].update({data[0]: 1})

        if data[0] in graph:
            graph[data[0]].update(child_nodes)
        else:
            graph[data[0]] = child_nodes
            for child in child_nodes:
                if child in graph:
                    graph[child].update({data[0]: 1})
                else:
                    graph[child]: {data[0]: 1}


#using the dijkstra algorithm to solve the problem 
def dijkstra(graph, start, goal):
    if start not in graph or goal not in graph:
        print("no route found")
        return

    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph
    infinity = float("inf")
    path = []
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)

    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print("no route found")
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        # print("Shortest distance is " + str(shortest_distance[goal]))
        for i in path:
            print(i, end=" ")




graph = {}
no_nodes = int(input())
build_graph()
# print(graph)
start_goal = input().split()
dijkstra(graph, start_goal[0], start_goal[1])
