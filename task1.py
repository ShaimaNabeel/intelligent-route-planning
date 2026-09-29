from queue import Queue
from queue import PriorityQueue
from collections import deque

graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138), ('Drobeta', 120)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
}

def bfs_search(graph, start, goal):
    queue = deque([(start, [start], 0)])

    while queue:
        current_city, path, distance = queue.popleft()

        if current_city == goal:
            return path, distance  

        for neighbor, edge_distance in graph.get(current_city, []):
            new_path = path + [neighbor]
            new_distance = distance + edge_distance
            queue.append((neighbor, new_path, new_distance))

    return None, 0  

def greedy_best_first_search(graph, start, goal, h):
    explored = set()
    queue = PriorityQueue()
    queue.put((h[start], start, [start], 0))

    while not queue.empty():
        _, current_city, path, distance = queue.get()

        if current_city not in explored:
            explored.add(current_city)

            if current_city == goal:
                return path, distance 

            for neighbor, edge_distance in graph.get(current_city, []):
                new_path = path + [neighbor]
                new_distance = distance + edge_distance
                queue.put((h[neighbor], neighbor, new_path, new_distance)) 
    return None, 0 

def astar_search(graph, start, goal, h):
    explored = set()
    queue = PriorityQueue()
    queue.put((h[start], 0, start, [start])) 

    while not queue.empty():
        _, cost, current_city, path = queue.get()

        if current_city not in explored:
            explored.add(current_city)

            if current_city == goal:
                return path, cost  

            for neighbor, edge_distance in graph.get(current_city, []):
                new_path = path + [neighbor]
                new_cost = cost + edge_distance
                queue.put((new_cost + h[neighbor], new_cost, neighbor, new_path)) 

    return None, 0

start_city = 'Arad'
goal_city = 'Bucharest'

bfs_path, bfs_distance = bfs_search(graph, start_city, goal_city)
if bfs_path:
    print(f'BFS Path from {start_city} to {goal_city}: {bfs_path} - Distance: {bfs_distance} km')
else:
    print(f'No path found from {start_city} to {goal_city} using BFS')

heuristic_values = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Fagaras': 176,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Pitesti': 100,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}
greedy_path, greedy_distance = greedy_best_first_search(graph, start_city, goal_city, heuristic_values)
if greedy_path:
    print(f'Greedy Best-First Search Path from {start_city} to {goal_city}: {greedy_path} - Distance: {greedy_distance} km')
else:
    print(f'No path found from {start_city} to {goal_city} using Greedy Best-First Search')

astar_path, astar_distance = astar_search(graph, start_city, goal_city, heuristic_values)
if astar_path:
    print(f'A* Search Path from {start_city} to {goal_city}: {astar_path} - Distance: {astar_distance} km')
else:
    print(f'No path found from {start_city} to {goal_city} using A* Search')






















