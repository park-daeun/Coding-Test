import sys
n = int(sys.stdin.readline())
warehouses = list(map(int, sys.stdin.readline().split()))

d = [0] * n

for i in range(n):
    #print(d)

    if i == 0 or i == 1:
        d[i] = warehouses[i]
    
    d[i] = warehouses[i] + max(d[i-2], d[i-3])

#print(d)

print(max(d))

'''
입력 예시
4
1 3 1 5

5
1 3 1 5 11

6
1 3 1 5 11 9

4
1 2 3 1

출력 예시
8

14

17

4

리뷰
DP 테이블을 생각해보았더니 쉽게 해결되었다.
'''