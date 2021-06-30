n = int(input())  # 수열에 속해있는 개수

# n개의 정수 입력받아 리스트에 저장하기
array = []
for i in range(n):
    array.append(int(input()))

array.sort()  # 오름차순 정렬
array.reverse()  # 내림차순 정렬

for a in array:
    print(a, end=' ')  # 정렬된 수열을 공백으로 구분하여 출력

'''
입력 예시
3
15
27
12

출력 예시
27 15 12

코드 리뷰
기본 정렬 문제였다. 굉장히 쉬웠고 작성한 코드도 책의 해설과 비슷하다.

배운 점
array.sort(); array.reverse() 두 줄을 
array = sorted(array, reverse=True) 한 줄로 변경할 수 있다.
'''
