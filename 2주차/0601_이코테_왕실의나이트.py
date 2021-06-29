import sys

l = sys.stdin.readline() #현재 위치
ans = 0 #출력값

if ord(l[0]) + 2 <= ord('h'):
    if int(l[1]) + 1 <= 8:
        ans += 1
    if int(l[1]) - 1 >= 1:
        ans += 1

if ord(l[0]) + 1 <= ord('h'):
    if int(l[1]) + 2 <= 8:
        ans += 1
    if int(l[1]) - 2 >= 1:
        ans += 1

if ord(l[0]) - 1 >= ord('a'):
    if int(l[1]) + 2 <= 8:
        ans += 1
    if int(l[1]) - 2 >= 1:
        ans += 1

if ord(l[0]) - 2 >= ord('a'):
    if int(l[1]) + 1 <= 8:
        ans += 1
    if int(l[1]) - 1 >= 1:
        ans += 1

print(ans)


'''
입력 예시
a1

c2

출력 예시
2

6

코드 리뷰
나이트가 이동할 수 있는 8가지의 모든 경우의 수(-2,-1 / -1,-2 / 1,-2 / 2,-1 / 2,1 / 1,2 / -1,2 / -2,1)를 전부 if문으로 만들었다.
알파벳끼리의 대소를 비교할 때는 아스키코드를 사용하였다.
책에 있는 방법처럼 steps라는 리스트를 만들어 8가지의 경우의 수를 넣고 for문을 사용하는 것이 더 나을 것 같다.
'''