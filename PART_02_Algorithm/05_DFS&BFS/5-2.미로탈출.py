# page.152
'''
[문제]
N x M 크기의 미로
동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재
한 번에 한 칸씩 이동 가능
괴물이 있는 부분은 0, 없는 부분은 1
동빈이 탈출하기 위해 움직여야 하는 최소 칸의 개수 구하기 (시작과 끝 칸을 모두 포함하여 계산)

[풀이]
(1, 1) 지점에서부터 BFS 를 수행하여 모든 노드의 값을 거리 정보로 채우기
특정한 노드를 방문할 경우 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다
'''

from collections import deque

# 입력값 받기
n, m = map(int, input().split())

graph_map = []
for _ in range(n):
    graph_map.append(list(map(int, input())))

# 이동할 방향 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1, 1]

# BFS 정의
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 제외
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 공간의 경우 제외
            if graph_map[nx][ny] == 0:
                continue
            # 해당 노드가 처음 방문하는 곳인 경우 최단 거리 기록
            if graph_map[nx][ny] == 1: 
                graph_map[nx][ny] = graph_map[x][y] + 1
                queue.append((nx, ny))
    return graph_map[n-1][m-1]

print(bfs(0, 0))
