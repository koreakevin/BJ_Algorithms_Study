n = int(input()) # 만들 리스트 크기 입력
dp = [1, 1, 1] # dp라는 리스트에 f(1) = f(2) = f(3) = 1이기 때문에 0~2까지 [1, 1, 1]을 넣음
for i in range(3, n): # 3부터 n까지의 합
    dp.append(dp[i-3]+dp[i-1]) #점화식 f(n) = f(n-1) + f(n-3)넣음
print(dp[n-1]) # 0부터 리스트가 나오기 때문에 n-1을 해 값 출력

# 피보나치 수열은 상당히 단순한 단조 증가 수열로 0번째 항은 0, 1번째 항은 1, 그 외 항은 전번, 전전번 항의 합으로 표현한다.
# 피보나치 수열은 재귀함수의 활용이나 동적 계획법을 많이 사용한다.
# 재귀함수는
# 피보나치 수열의 재귀함수 파이썬 코드
# def fibo(n):
#     return fibo(n-1) + fibo(n-2) if n >= 2 else n
#
# for n in range(1, 11):
#     print(n, fibo(n))

# 피보나치 수열의 동적 계획법 파이썬 코드
# n을 10이라고 하자.
# cache = [0 for _ in range(10+1)]
# cache[1] = 1
#
# for i in range(2, 10+1):
#     cache[i] = cache[i-1] + cache[i-2]
#
#     print(cache[10])
# 위 코드는 동적 계획법을 변형해 만들었다.
