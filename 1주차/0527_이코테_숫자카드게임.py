import sys

# n: 행의 개수, m: 열의 개수
n, m = map(int, sys.stdin.readline().split())
max = 0

for _ in range(0, n):
    cards = list(map(int, sys.stdin.readline().split()))
    if max < min(cards):
        max = min(cards)
print(max)

'''
입력 예시
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4

출력 예시
2

3

코드 리뷰
각 행의 최솟값들 중의 최댓값을 구하는 문제이다.
if res < min(cards):
    res = min(cards)
-> res = max(res, min(cards))로 바꿀 수 있음.
'''
