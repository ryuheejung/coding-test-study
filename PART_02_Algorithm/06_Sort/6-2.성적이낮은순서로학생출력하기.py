# page.180
'''
[문제]
N 명의 학생의 이름과 성적 정보가 주어졌을 때, 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램 작성

[풀이]
정렬 알고리즘은 N의 개수에 따라 시간 복잡도를 고려할 것
데이터의 개수가 최대 100,000 개까지 입력될 수 있으므로 O(N)을 보장하는 계수 정렬을 이용
학생의 이름과 성적 정보 모두가 아닌 이름만 출력하므로 (점수, 이름)으로 묶어야 함
'''

# 입력값 받기
n = int(input())

array_students = []
for _ in range(n):
    student_info = input().split()
    array_students.append((student_info[0], int(student_info[1])))

# 점수를 기준으로 정렬
array_students = sorted(array_students, key=lambda student_info: student_info[1])
# print(array_students)
for student in array_students:
    print(student[0], end=" ")
