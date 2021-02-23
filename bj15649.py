n, m = map(int, input().split())

number_list=[1+ i for i in range(n)] # 숫자 리스트
check_number=[False] * n # 중복숫자 체크
array=[] # 출력할 수열

def DFS(x):
    if x == m: # 수열 m개를 충족할 경우 출력
            print(*array)
            return
    for i in range(n):
        if check_number[i]: # 중복될 경우 패스
            continue

        array.append(number_list[i]) # 수열 추가
        check_number[i]=True # 사용한 수 체크

        DFS(x+1) # + 1번째 수열을 위해 재귀함수 호출

        array.pop() # 수열 마지막 자리 삭제
        check_number[i]=False # 사용한 수 초기화
DFS(0)

# 문제를 풀기 위해서는 Backtracking에 대한 이해가 필요함
#
# Backtracking(되추척)이란
# 비선형으로 구성된 자료 구조를 깊이 우선으로 탐색할 때,
# 더 이상 나아갈 수 없는 상황에서 그 이전 단계로 복귀하는 과정을 말함.
# 여러 개의 solution을 가진 문제에서 모든 solution을 탐색하는 완전탐색 전략임.
# 대표적인 예로는 재귀 호출 or 스택을 통한 DFS가 있음.
# 원리
# 1.어떤 노드의 유망성을 점검 후,
# 2.유망하지 않으면 배제 시킴=가지치기
# 3.해당 노드이 부모노드로 되돌아간 후 다른 자손노드를 검색함= 시간 단축
# 조건이 만족하는 모든 경우의 수를 찾는 것.

# 위 문제도 조건을 만족하기 직전 상태로 되돌아가 다음 경우의 수를 찾는 방식인 DFS와
# 재귀적으로 함수를 호출하고 이후 제일 바닥에 있는 함수부터 차례차례 종료되면서 다음 수열을 완성하는 방식으로 함.