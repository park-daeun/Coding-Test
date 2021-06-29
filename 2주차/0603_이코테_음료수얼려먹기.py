import sys

n, m = map(int, sys.stdin.readline().split())

ice_matrix = []
for i in range(n):
    ice_matrix.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if ice_matrix[x][y] == 0:
        ice_matrix[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            ans += 1

print(ans)

'''
입력 예시
4 5
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

출력 예시
3

8

코드 리뷰
30분 내에 못 풀어서 책에 있는 코드를 봤다.
DFS/BFS를 공부해놓고 다른 방법으로 풀려고(스택으로) 계속 시도했다.
DFS는 재귀함수쓰는거 꼭 기억하기.
'''
