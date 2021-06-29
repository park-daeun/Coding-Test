import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

map_graph = []
for i in range(n):
    map_graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        ds = [[x-1, y], [x, y-1], [x+1, y], [x, y+1]]

        for d in ds:
            if d[0] < 0 or d[0] >= n or d[1] < 0 or d[1] >= m:
                continue
            if map_graph[d[0]][d[1]] == 0:
                continue
            if map_graph[d[0]][d[1]] == 1:
                map_graph[d[0]][d[1]] = map_graph[x][y] + 1
                queue.append((d[0], d[1]))

    return map_graph[n-1][m-1]


print(bfs(0, 0))

'''
입력 예시
5 6
101010
111111
000001
111111
111111

출력 예시
10

코드 리뷰
마찬가지로 책에 있는 코드를 참고했다.
DFS/BFS를 많이 연습해야될 듯 하다.
'''
