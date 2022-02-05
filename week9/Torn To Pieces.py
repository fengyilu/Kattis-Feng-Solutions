# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Torn To Pieces

# * Link: https://open.kattis.com/contests/rxgmfr/problems/torn2pieces ;

# * @author: Feng Yi Lu

# * @version 1.0, 2022-01-14 16:19:24

# * Method : dijkstra

# # Status : Accepted 

# # Runtime: 0.06*/


# function for building the graph to have all necessary connections of each stations
def buildingGraph():
    for x in range(no_nodes):
        #example input "Uptown Midtown"
        data = input().split()
        #we need to know each neighbour of a node
        childNodes = {}
        #iterate through input array except the first element in array
        for child in data[1:]:
            childNodes[child] = 1
            if child not in graph:
                graph[child] = {data[0]: 1}
            else:
                graph[child].update({data[0]: 1})

        #if first element in input data already exists in graph dictonary, update their neighbours (adding childNodes (key value) pairs into graphs at the key data[0]), 
        # else: the key of graphs get child_nodes as value
        if data[0] in graph:
            graph[data[0]].update(childNodes)
        else:
            graph[data[0]] = childNodes
        #check every child in child_nodes and do the same, to update each possible neighbour
            for child in childNodes:
                if child in graph:
                    graph[child].update({data[0]: 1})
                else:
                    graph[child]: {data[0]: 1}


#using the dijkstra algorithm to solve the problem 
def dijkstraSolution(graph, startNode, goal):
    #checking in the beginning if startNode and goal node exists 
    if startNode not in graph or goal not in graph:
        print("no route found")
        return

    path = {}
    predecessor = {}
    not_visited = graph
    infinity = float("inf")
    path = []
    for node in not_visited:
        path[node] = infinity
    path[startNode] = 0

#check every node and possible path and get predecessor of the nodes 
    while not_visited:
        currentNode = None
        for node in not_visited:
            if currentNode is None:
                currentNode = node
            elif path[node] < path[currentNode]:
                currentNode = node

        for child_node, weight in graph[currentNode].items():
            if weight + path[currentNode] < path[child_node]:
                path[child_node] = weight + path[currentNode]
                predecessor[child_node] = currentNode
        not_visited.pop(currentNode)

    current_node = goal
    #starting with goal node and recrate the path backwards until startnode
    while current_node != startNode:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print("no route found")
            break
    path.insert(0, startNode)
    if path[goal] != infinity:
        # print("Shortest distance is " + str(path[goal]))
        for i in path:
            print(i, end=" ")




graph = {}
no_nodes = int(input())
buildingGraph()
startAndEndGoal = input().split()
dijkstraSolution(graph, startAndEndGoal[0], startAndEndGoal[1])
