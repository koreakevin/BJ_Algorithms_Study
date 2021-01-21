n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)

# 모든 경우의 수를 다 참조하는 완전 탐색사용
# '무식하게 푼다(brute-force)'는 컴퓨터의 빠른 계산 능력을 이용해 가능한 경우의 수를 일일이 나열하면서 답을 찾는 방법을 의미.
# 이렇게 가능한 방법을 전부 만들어 보는 알고리즘을 뜻한다.
# Line 1: n,m을 입력받아 int로 변환
# Line 2: 카드에 쓰여 있는 수 들을 list화 하여 저장
# Line 3: 문제 조건에 적합한 수를 저장하여 반환하기 위한 변수 result 선언
# Line 4~10: 3개의 카드를 뽑아야 하며 이에 대한 모든 경우의 수를 살펴보기 위해 3중 for문 이용
# 첫번째 for문에서 0/ 두번째 for문에서 1/세번쨰 for문에서 2~n를 순회
# 모든 경우의 수를 확인하며 각각의 값을 더한뒤, 세 카드의 값이 m보다 클 경우 continue
# m보다 크지 않을 경우, 일단은 정답의 가능성이 존재하기 때문에 result변수에 저장
# 모든 경우를 반복하면 결국, result변수에는 m의 값 또는 m에 가장 가까운 값이 저장 됨
# Line 11: 출력