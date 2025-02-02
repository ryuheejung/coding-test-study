# page.182
'''
[문제]
N 개의 자연수로 이루어진 두 배열 A, B
최대 K번의 바꿔치기 연산을 수행할 수 있음
배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라 두 원소를 바꾸는 것이 바꿔치기 연산
K번 이하의 바꿔치기 연산을 통해 배열 A의 모든 원소의 합이 최대가 되도록 만들기

[풀이]
배열 A 는 오름차순, 배열 B 는 내림차순으로 정렬
배열 A, B를 첫 번째 인덱스부터 차례대로 비교하면서 A의 원소가 B의 원소보다 작은 경우 교체, 이 과정을 최대 k번 반복
'''

# 입력값 받기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# sorting
a = sorted(a)
b = sorted(b, reverse=True)


for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
