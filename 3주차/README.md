## 📚 3주차 배운 점
<br>

- 정렬 라이브러리
    - result = sorted(array) #정렬된 리스트를 따로 만듦
    - array.sort() #리스트의 내부 원소가 바로 정렬됨
<br>

- key로 정렬하기
    - def setting(data): ; return data[1]; result = sorted(array, key=setting)
    - array = sorted(array, key = lambda data: data[1])
<br>

- 내림차순 정렬
    - array.sort(); array.reverse()
    - array = sorted(array, reverse=True)
<br>

- 리스트 스와프
    - array[0], array[1] = array[1], array[0]
