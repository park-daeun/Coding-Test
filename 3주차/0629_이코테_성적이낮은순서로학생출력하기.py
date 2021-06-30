n = int(input())  # 학생의 수

# n명의 학생의 이름과 점수를 입력받아 리스트에 저장하기
array = []
for i in range(n):
    name, score = input().split()
    array.append([name, int(score)])

# key를 이용하여 정렬 (점수를 이용하여 정렬)


def setting(data):
    return data[1]


array = sorted(array, key=setting)

# 정렬된 리스트의 이름을 공백으로 구분하여 출력
for a in array:
    print(a[0], end=' ')

'''
입력 예시
2
홍길동 95
이순신 77

출력 예시
이순신 홍길동

코드 리뷰
기본 정렬 문제였다. 굉장히 쉬웠고 작성한 코드도 책의 해설과 비슷하다.

배운 점
다음과 같은 세 줄의 코드를
def setting(data):
    return data[1]
array = sorted(array, key=setting)

다음과 같이 한 줄로 작성할 수 있다.
array = sorted(array, key = lambda data: data[1])
'''
