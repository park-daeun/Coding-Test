import sys
import heapq

INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
time = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if time[node] < dist:
            continue

        for i in graph[node]:
            #print(graph[node])
            cost = dist + i[1]

            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
total = 0
for t in time:
    if t != INF and t != 0:
        count += 1
        total = max(total, t)

print(count, total)


'''
입력 예시
3 2 1
1 2 4
1 3 2

출력 예시
2 4
'''