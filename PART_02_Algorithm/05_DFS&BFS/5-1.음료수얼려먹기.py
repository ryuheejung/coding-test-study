# page.149
'''
[문제]
N x M 크기의 얼음 틀
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수 구하기

[풀이]
특정한 지점의 주변 상하좌우 를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
방문한 지점에서 다시 상화좌우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.
DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문하는 프로그램을 작성.
'''

# 입력값 받기
n, m = map(int, input().split())

graph_mold = []
for _ in range(n):
    mold_row = list(map(int, input()))
    graph_mold.append(mold_row)

# DFS 정의
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 방문하지 않은 노드라면
    if graph_mold[x][y] == 0:
        # 방문처리
        graph_mold[x][y] = 1
        # 현재 노드의 상하좌우 에 위치한 노드 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)