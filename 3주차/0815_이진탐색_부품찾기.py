import sys

def binary_search(arr, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

a.sort()
for x in X:
    if binary_search(a, x, 0, n-1) == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

'''
입력 예시
5
8 3 7 9 2
3
5 7 9

출력 예시
no yes yes
'''