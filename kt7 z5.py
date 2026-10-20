from collections import deque

n = 6
s = 1
roads = [
    (1, 2, 1),
    (2, 3, -1),
    (3, 2, -1),
    (3, 4, 1),
    (1, 6, 4),
]

graph = [[] for _ in range(n + 1)]
for start, finish, cost in roads:
    graph[start].append(finish)

INF = 10 ** 18
distance = [INF] * (n + 1)
distance[s] = 0
for _ in range(n - 1):
    updated = False
    for start, finish, cost in roads:
        if distance[start] < INF and distance[start] + cost < distance[finish]:
            distance[finish] = distance[start] + cost
            updated = True
    if not updated:
        break

unlimited = [False] * (n + 1)
queue = deque()
for start, finish, cost in roads:
    if distance[start] < INF and distance[start] + cost < distance[finish] and not unlimited[finish]:
        unlimited[finish] = True
        queue.append(finish)
while queue:
    city = queue.popleft()
    for nxt in graph[city]:
        if not unlimited[nxt]:
            unlimited[nxt] = True
            queue.append(nxt)

for city in range(1, n + 1):
    if unlimited[city]:
        print("-")
    elif distance[city] >= INF:
        print("*")
    else:
        print(distance[city])
