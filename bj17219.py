import  sys
input = lambda : sys.stdin.readline().rstrip()

a, b = map(int, input().split())
arr = dict(input().split() for _ in range(a))

for _ in range(b):
    site = input()
    print(arr.get(site))