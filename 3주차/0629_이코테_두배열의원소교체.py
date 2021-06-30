n, k = map(int, input().split())  # n:원소 개수, k:바꿔치기 연산 수
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순으로 정렬, B는 내림차순으로 정렬
A = sorted(A)
B = sorted(B, reverse=True)

# 두 배열을 k번 비교하며 A의 합이 최대값이 되도록 바꿔치기하기
for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

# A의 합을 출력
print(sum(A))

'''
입력 예시
5 3
1 2 5 4 3
5 5 6 6 5

출력 예시
26

코드 리뷰
두 배열의 원소의 크기를 비교하지 않고 바꾸도록 코드를 짰다.
현재 예시로는 문제가 없으나 잘못된 코드이다.
따라서 비교하는 과정을 추가하였다.

배운 점
스와프하기
array[0], array[1] = array[1], array[0]
'''
