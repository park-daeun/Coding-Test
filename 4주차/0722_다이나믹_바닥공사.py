import sys

# 정수 n을 입력받기
n = int(sys.stdin.readline())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * (n+1)

# 다이나믹 프로그래밍 진행(보텀업)
for i in range(1, n+1):
    if i == 1:
        d[i] = 1
        continue
    elif i == 2:
        d[i] = 3
        continue

    d[i] = (d[i-1] + 2*d[i-2]) % 796796

# 계산된 결과 출력
print(d[n])

'''
입력 예시
3

출력 예시
5

리뷰
'''