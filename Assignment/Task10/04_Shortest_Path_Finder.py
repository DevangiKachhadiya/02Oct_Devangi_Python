# Shortest Path Finder (Using Dijkstra's Algorithm)
'''You are given a weighted graph representing cities connected by roads. Each road has a distance
(weight) associated with it. Write a Python program to determine the shortest path from a specified
start city to a destination city using Dijkstra's Algorithm.
Your program should:
• Accept a graph represented by cities (nodes) and distances (weighted edges).
• Take input for the start city and the destination city.
• Clearly print the shortest path and the total distance.
Example Input:
cities = {
'A': {'B': 5, 'C': 10},
'B': {'A': 5, 'C': 3, 'D': 9},
'C': {'A': 10, 'B': 3, 'D': 1},
'D': {'B': 9, 'C': 1}
}
start_city = 'A'
destination_city = 'D'
'''

import heapq

def dijkstra(cities, start_city, destination_city):
    distances = {city: float('inf') for city in cities}
    previous = {city: None for city in cities}
    distances[start_city] = 0
    pq = [(0, start_city)]
    
    while pq:
        current_distance, current_city = heapq.heappop(pq)
        if current_city == destination_city:
            break
        for neighbor, weight in cities[current_city].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(pq, (distance, neighbor))
    
    path = []
    current_city = destination_city
    while current_city:
        path.append(current_city)
        current_city = previous[current_city]
    path.reverse()
    
    return path, distances[destination_city]

cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}
start_city = 'A'
destination_city = 'D'
path, distance = dijkstra(cities, start_city, destination_city)
print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(path)}")
print(f"Total distance: {distance}")