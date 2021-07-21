## 📚 3주차 배운 점

### 🔎 정렬
- <b>정렬 라이브러리</b>
    - result = sorted(array) #정렬된 리스트를 따로 만듦
    - array.sort() #리스트의 내부 원소가 바로 정렬됨
<br>

- <b>key로 정렬하기</b>
    - def setting(data): return data[1]<br>result = sorted(array, key=setting)
    - array = sorted(array, key = lambda data: data[1])
<br>

- <b>내림차순 정렬</b>
    - array.sort()<br>array.reverse()
    - array = sorted(array, reverse=True)
<br>

- <b>리스트 스와프</b>
    - array[0], array[1] = array[1], array[0]
<br>

### 🔎 이진 탐색
- <b>순차 탐색</b>
    - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
<br>

- <b>이진 탐색</b>
    - 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
    - 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법
<br>

### 💡 빠르게 입력받기
- import sys<br>input_data = sys.stdin.readline().rstrip()
- ※ rstrip: 줄바꿈문자 제거하기위해 꼭 입력해야함!
