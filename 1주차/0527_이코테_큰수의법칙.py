import sys

# n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 특정한 인덱스가 더해질 수 있는 연속 횟수
n, m, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

count = 0
sum = 0

max_index = num_list.index(max(num_list))

for _ in range(0, m):
    if count >= k:
        copy_list = num_list.copy()
        copy_list.pop(max_index)
        sum += max(copy_list)
        count = 0
    else:
        sum += max(num_list)
        count += 1
print(sum)

'''
입력 예시
5 8 3
2 4 5 4 6

5 7 2
3 4 3 4 3

출력 예시
46

28

코드 리뷰
가장 큰 수와 그 다음으로 큰 수만 알면 구할 수 있다.
리스트의 최댓값을 구하는 방법을 두 번 이용하여 구했다. -> 정렬 이용하기
-> 수열 이용하기
'''
