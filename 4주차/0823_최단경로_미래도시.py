import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, sys.stdin.readline().split())

# 플로이드
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = graph[1][K] + graph[K][X]

if ans >= INF:
    print(-1)
else:
    print(ans)

'''
입력 예시
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4

출력 예시
3

-1
'''