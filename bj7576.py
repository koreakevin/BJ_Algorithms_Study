from collections import deque

M, N = map(int, input().split())
tots = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if tots[i][j] == 1:
            queue.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# bfs 시작
while queue:
    row, col = queue.popleft()

    for k in range(4):
        _row = row + dy[k]
        _col = col + dx[k]

        # 안익은게 있다면, 익은 것으로 바꿔준다.
        if 0 <= _row < N and 0 <= _col < M and tots[_row][_col] == 0:
            tots[_row][_col] = tots[row][col] + 1
            queue.append([_row, _col])
# bfs 끝

# -1이 존재해서 -2 값으로 비교
result = -2
# 안익은게 있는지 체크
check_tot = False

for i in tots:
    for j in i:
        if (j == 0):
            check_tot = True
        result = max(result, j)

if check_tot:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)

# 토마토의 위치를 queue에 저장 해줌.
# 그래프 탐색 알고리즘인 BFS와 DFS 중 정점과 같은 레벨에 있는 노드들(형제 노드들)을 먼저 탐색하는 방식 사용함.
# BFS가 정점과 같은 레벨에 있는 노드들(형제 노드들)을 먼저 탐색하는 방식이기 때문에 저장된 위치를 기준으로 BFS를 사용하여 상,하,좌,우를 검사해주어 0인 값을 찾기 위함임.
# 찾아는 과정에서 기준이 되는 숫자에 +1을 해주어 더해감.
# 만약 BFS함수를 실행하고 나서도 0이 있다면 -1을 출력하고, 가장 큰 값이 -1이면 0을 출력하고, 둘다 아니면 제일 큰 값에 -1을 한 값을 출력시킴.

