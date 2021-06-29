import sys

n = int(sys.stdin.readline())
meeting_list = []

for i in range(n):
    meeting_list.append(list(map(int, input().split())))

print(sorted(meeting_list))
possible_list = []

for meeting in sorted(meeting_list):
    if len(possible_list) == 0:
        possible_list.append([meeting[1]])
        print(possible_list)
        continue

    p = 0
    for i in range(len(possible_list)):
        if meeting[0] >= possible_list[i][len(possible_list[i])-1]:
            p = 1
            possible_list[i].append(meeting[1])
        else:
            p = 0

    if p == 0:
        possible_list.append([meeting[1]])

print(possible_list)

len_list = []
for possible in possible_list:
    len_list.append(len(possible))

print(max(len_list))

'''
입력 예시
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

출력 예시
4

코드 리뷰
'''
