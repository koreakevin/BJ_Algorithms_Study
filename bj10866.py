from collections import deque
import sys

n = int(sys.stdin.readline())

dq = deque()

def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0

def size():
    return len(dq)

for i in range(n):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push_front':
        dq.appendleft(cmd[1])

    elif cmd[0] == 'push_back':
        dq.append(cmd[1])

    elif cmd[0] == 'pop_front':
        if empty() == 1:
            print("-1")
        else:
            tmp = dq.popleft()
            print(tmp)

    elif cmd[0] == 'pop_back':
        if empty() == 1:
            print("-1")
        else:
            tmp = dq.pop()
            print(tmp)

    elif cmd[0] == 'front':
        if empty() == 1:
            print("-1")
        else:
            print(dq[0])

    elif cmd[0] == 'back':
        if empty() == 1:
            print("-1")
        else:
            print(dq[len(dq)-1])

    elif cmd[0] == 'size':
        print(size())

    elif cmd[0] == 'empty':
        print(empty())


# deque 모듈 사용함

# deque 모듈이란?
# double-ended queue 의 줄임말로, 앞과 뒤에서 즉, 양방향에서 데이터를 처리할 수 있는 queue형 자료구조를 의미한다.

# queue(큐)는 자료의 선입선출,FIFO(First-In-First_Out)을 보장하는 자료구조이다.

# 데이터 추가/append,appendleft
# 리스트의 명령어와 같이 append를 이용해서 데이터를 하나씩 추가할 수 있다. appendleft의 경우 왼쪽에서 데이터를 추가할 수 있다.

# 데이터 추가(확장)/extend, extendleft
# 기본 deque에 iterable데이터를 합치는 명령어이다. 기본적으로 오른쪽 방향으로 합치고, extendleft의 경우은 왼쪽에 데이터를 붙인다.

# 데이터 반환/Pop,Popleft
# pop의 경우는 데이터를 하나씩 반환하고, 기존 큐에서 삭제하는 명령어이다. popleft의 경우는 왼쪽 방향에서 데이터를 반환하고 삭제하는 명령어이다.

# 데이터 삭제/remove,clear
# remove의 경우 인자로 넣은 데이터를 deque에서 삭제하는 명령어이다. clear의 경우는 deque안의 모든 맴버를 삭제한다.

# 데이터 값 위치 바꾸기/reverse, rotate
# reverse의 경우 데이터를 뒤집어 버린다. 그냥 데이터를 통째로 뒤집어 버린다. 그리고 rotate 명령어는 가장 오른쪽 데이터를 pop해서 appendleft한다.
# 이런식으로 데이터를 하나씩 순회하게 한다. 만약 인자로 들어간 숫만큼 회전을 하게 된다.