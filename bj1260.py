from sys import stdin
n, m, v = map(int, stdin.readline().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    line=list(map(int, stdin.readline().split()))
    matrix[line[0]][line[1]]=1
    matrix[line[1]][line[0]]=1

def bfs(start):
    visited=[start]
    queue=[start]
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c]==1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return  visited

def dfs(start, visited):
    visited += [start]
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return  visited

print(*dfs(v,[]))
print(*bfs(v))

# BFS와 DFS의 개념이 필요함

# BFS(Breadth-First Search)란 너비 우선 탐색을 말함
# 개념
# 루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법
# 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점은 나중에 방문하는 순회 방법
# 깊게(deep)탐색하기 전에 넓게(wide)탐색 하는 것
# 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 사용됨
# 특징
# 시작 노드에서 시작해서 거리에 따라 단계별로 탐색해 직관전이지 않은 면이 있음
# 재귀적으로 동작하지 않음
# 방문한 노드를 차례로 저장한 후 꺼낼 수 있는 자료 구조인 큐(Queue)를 사용해 반복적인 형태로 구현하는 것이 좋음 - 즉, 선입선출(FIFO)원친으로 탐색
# 'Prim','Dijkstra' 알고리즘과 유사함
# (공통점)이 알고리즘을 구현할 때 가장 중요한 것은 그래프 탐색의 경우  어떤 노드를 방문했었는지 여부를 반드시 검사해야함-이를 검사하지 않을 경우 무한루프에 빠질 위험이 있음
# python 기본 코드
# 1 def bfs(graph, start_node):
# 2  visit = list()
# 3  queue = list()
# 4
# 5  queue.append(start_node)
# 6
# 7  while queue:
# 8     node = queue.pop(0)
# 9     if node not in visit:
# 10        visit.append(node)
# 11        queue.extend(graph[node])
# 12
# 13 return visit
# (2~3) 방문했던 노드 목록을 차례대로 저장할 리스트와, 다음으로 방문할 노드의 목록을 차례대로 저장할 리스트(큐)를 만들어줌
#
# (5) 우선 맨 처음에는 당연히 시작 노드를 큐에 넣어줌
#
# (7) 큐의 목록이 바닥날때까지(더 이상 방문할 노드가 없을 때까지) loop를 돌려줌
#
# (8) 큐의 맨 앞에있는 노드를 꺼내옴
#
# (9) 해당 노드가 아직 방문 리스트에 없다면,
#
# (10) 방문 리스트에 추가해주고,
#
# (11) 해당 노드의 자식 노드들을 큐에 추가함

# DFS(Depth-First Search)란 깊이 우선 탐색을 말함
# 개념
# 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완변하게 탐색하는 방법
# 미로를 탐색할때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 이곳으로부터 다른 방향으로 다시 탐색하는 방법과 유사함
# 넓게(wide)탐색하기 전에 깊게(deep)탐색 하는 것
# 모든 노드를 방문하고자 하는 경우에 사용됨
# 특징
# 자기 자신을 호출하는 순환 알고리즘의 형태임
# 전위 순회(Pre-Order Traversals)를 포함한 다른 형태의 트리 순회는 모두 DFS의 한 종류
# (공통점)이 알고리즘을 구현할 때 가장 중요한 것은 그래프 탐색의 경우  어떤 노드를 방문했었는지 여부를 반드시 검사해야함-이를 검사하지 않을 경우 무한루프에 빠질 위험이 있음
# python 기본 코드
# 1 def dfs(graph, start_node):
# 2  visit = list()
# 3  queue = list()
# 4
# 5  queue.append(start_node)
# 6
# 7  while stack:
# 8     node = stack.pop()
# 9     if node not in visit:
# 10        visit.append(node)
# 11        queue.extend(graph[node])
# 12
# 13 return visit
# queue의 변수명이 stack으로 바뀌었고, 8번 라인에서 pop(0) 을 하던 부분이 pop() 으로 바뀌었음

# 리스트에서 pop()을 하게되면 맨 마지막에 넣었던 아이템을 가져오게 되므로 stack과 동일하게 동작하게 됨.

# 반대로 pop(0)을 하게되면 맨 앞에있는 요소를 가져오므로 queue와 동일하게 동작했던 것임.

# DFS와 BFS를 구현하기 위해서 트리나 그래프의 구조를 가지고 있어야 서로 연결된 노드를 파악 할 수 있음 하지만 해당 문제에서는 class node를 하면서  node를 만들고 연결해서 문제를 해결하기에는 무리임
# 인접행렬 방식으로 행과 열을 통해서 값을 해당 숫자들이 연결되어 있는지 확인 해줌
# N개의 숫자가 있으므로 N+1 x N+1의 행렬을 리스트를 통해서 만들고 0으로 채워줌
# 인덱스와 값을 일치시키기 위해서 N+1개의 숫자를 사용함. 0행 0열은 숫자가 없으므로 당연히 0 값으로 비어있음
# 연결된 숫자들 값을 입력받아서 해당 행과 열의 값을 1로 바꿔줌.이를 통해서 행의 숫자와 열의 숫자가 연결 되어 있다는 표시를 해줌
# DFS와 BFS를 구현한 후 해당 값 출력