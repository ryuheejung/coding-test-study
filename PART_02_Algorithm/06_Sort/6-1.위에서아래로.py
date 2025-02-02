# page.178
'''
[문제]
수열을 내림차순으로 정렬하는 프로그램 만들기

[풀이]
제한하는 수의 개수가 500개 이하로 매우 적으므로
어떠한 정렬 알고리즘을 사용해도 무방
여러 정렬 알고리즘을 이용해서 풀어보기
'''

# 입력값 받기
n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

# 내림차순 정렬
# (파이썬 기본 정렬 라이브러리 이용)
array = sorted(array, reverse=True)

for element in array:
    print(element, end=" ")

# (선택 정렬)
# (삽입 정렬)
# (퀵 정렬)
# (계수 정렬)
