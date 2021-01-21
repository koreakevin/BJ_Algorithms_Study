import sys
input = lambda : sys.stdin.readline().rstrip()

a,b=map(int, input().split())

arr=[0]*(b+1)

for i in range(2,b+1):
    if arr[i]==0:
        if i >=a:print(i)
        for j in range(i, b+1, i):
            arr[j]=1