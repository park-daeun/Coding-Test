import sys

n, k = map(int, sys.stdin.readline().split())
count = 0

while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    count += 1
print(count)

'''
입력 예시
17 4

25 5

출력 예시
3

2

코드 리뷰
1. n에서 1을 뺀다
2. n에서 k로 나눈다(나누어 떨어질 때)
'''
