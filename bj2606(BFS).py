from sys import stdin
read=stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1]=set()
for j in range(int(read())):
    a,b=map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic):
    queue=[start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
visited=[]
bfs(1,dic)
print(len(visited)-1)

# 동일한 방식에서 bfs 방식은 큐 방식을 사용해서 문제를 해결함
