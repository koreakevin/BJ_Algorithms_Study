import sys
input=sys.stdin.readline

N=int(input())
dp=[0 for _ in range(N+3)]
arr=[0 for _ in range(N+3)]
for k in range(1,N+1):
    arr[k]=int(input())

dp[1]=arr[1] # 1층
dp[2]=arr[1]+arr[2] # 2층
dp[3]=max(arr[1]+arr[3], arr[2]+arr[3]) # 3층

for i in range(4,N+1): # N 층
    dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
print(dp[N])

# 계단 i칸까지 오를때의 최댓값을 dp[i]라고 놓고 문제의 입력(해당 계단의 숫자)를 arr[k] 놓음.
# 이것으로 3층까지 표현하고 N층 부터는 3칸 연속되는 계단을 밝을 수 없다는 조건을 생각함.
# 1.dp[i]=dp[i-2]+arr[i]->i칸을 밝기 전의 칸이 i-2이므로 3칸 연속 밝을 일이 없음.
# 2.dp[i]=dp[i-1]+arr[i]->i칸 이전에 i-1칸을 밟았으므로, 3칸 연속일 가능성이 존재함.
# 그래서 2번 점화식을 한칸 전의 dp가 아닌, 3칸 전의 dp로 이동시킨 뒤에 마지막 칸은 셀프로 더해줘
# 2번 점화식을 dp[i]=dp[i-3]+arr[i-1]+arr[i] 변경시킴.
# N층의 점화식은 결과적으로 1과 2중 큰값이 되므로 dp[i]=max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])가 됨.