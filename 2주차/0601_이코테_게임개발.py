import sys

# NxM 크기의 직사각형 맵
n, m = map(int, sys.stdin.readline().split())

# A = 현재 행, B = 현재 열, d = 현재 바라보는 방향(동, 서, 남, 북)
A, B, d = map(int, sys.stdin.readline().split())

# 전체 맵 정보 입력 받기
map = []
for y in range(n):
    map.append(list(sys.stdin.readline().split()))
    map[y] = [int(i) for i in map[y]]  # 맵 정보 str -> int

ans = 1  # 결과 값

ds = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북, 동, 남, 서
stack = [[A, B]]  # 방문한 칸 저장 -> 되돌아갈 때 이용

round = 1  # 방향을 한바퀴 돌았는 지 확인
while True:
    # 방향 북->서->남->동
    if d < 0:
        d = 3

    # 모든 방향을 다 돌았을 시에
    if round > 4:
        map[A][B] = 1
        round = 1  # round 초기화

        # 맨 처음 출발지로 돌아왔다면 종료, 즉 더 이상 뒤로 돌아갈 수 없다면 종료
        stack.pop()
        if len(stack) == 0:
            break

        # 현위치를 직전 칸으로 돌아가기
        A = stack[len(stack)-1][0]
        B = stack[len(stack)-1][1]

    # 다음 칸으로 갈 수 있다면
    if map[A + ds[d][0]][B + ds[d][1]] == 0:
        map[A][B] = 1
        round = 1 # round 초기화
        ans += 1

        # 현재 위치 다음 칸으로 옮기기
        A += ds[d][0]
        B += ds[d][1]
        stack.append([A, B])
        continue

    d -= 1
    round += 1

print(ans)

'''
입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

출력 예시
3

코드 리뷰
더 이상 갈 수 있는 길이 없어 되돌아갈 때 스택을 이용했다.
책에 나와있는 전부 0으로 된 새로운 맵을 생성한 후 가본 곳은 1로 바꾸는 방법도 좋은 것 같다.
되돌아 가는 걸 구현하는 과정에서 약간 헤맸다.

맵 정보를 int로 받지 않아서 어려움을 겪었다.
코드 상의 문제가 없어 보이는데 제대로 된 답이 나오지 않아서 오랜 시간이 걸렸는데 맵을 str로 받아서 그런 것이었다.
'''