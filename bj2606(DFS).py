from sys import stdin
read=stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1]=set()
for j in range(int(read())):
    a,b=map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i,dic)
visited=[]
dfs(1,dic)
print(len(visited)-1)

# 흔히 dfs와 bfs문제를 풀때, 트리 방식으로 생각해서 문제를 해결하는 경우가 많음
# 그러나 이번 문제는 딱히, 상위 노드와 하위 노드가 정해저 있지 않기 때문에 그래프 방식을 사용함
# 그래프 방식은
#           A
#         /   \
#        C     B
#         \   / \
#          \ D   E
#           \   /
#             F
#   graph={'A': set(['B','C']),
#          'B': set(['A','D','E']),
#          'C': set(['A','F']),
#          'D': set(['B']),
#          'E': set(['B','F']),
#          'F': set(['C','E'])
# 이러한 방식으로 A노드와 연결된 다른 노드들을 set집합 연산자를 통해서 표현함
# 같은 방식으로 이번 문제에서도 1에서 7까지으 컴퓨터에 대해서 연결된 것을 그래프 형식으로 표현하면 됨
# 소스코드 dic가 그림의 graph와 동일하다고 생각함
# 예제 입력 1번의 노드를 연결한 결과가 아래와 같이 나타낼거임
# dic = {1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 4: {7}, 5: {1, 2, 6}, 6: {5}, 7: {4}}
# 이제 재귀 방식의 dfs를 통해 바이러스가 걸린 컴퓨터를 찾아냄
# 바이러스가 걸린 경로들을 visited엦 저장한 후 최종 출력에서는 본인 1을 제외한 나머지 노드들의 개수를 출력함