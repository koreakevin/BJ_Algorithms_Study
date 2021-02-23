class Stack:
    def __init__(self):
        self.list=[]

    def push(self, num):
        self.list.append(num)

    def pop(self):
        if self.size()==0:
            return -1
        return self.list.pop()

    def size(self):
        return len(self.list)

    def empty(self):
        return  1 if len(self.list)== 0 else 0

    def top(self):
        return self.list[-1] if self.size() != 0 else -1

num = int(input()) # 몇개의 숫자를 받을건지
stack = Stack() # 문제를 풀기위해 사용한 stack
inputs = [] # 입력을 저장하기 위한 list
outputs = [] # 출력을 저장하기 위한 list
idx = 0

# 입력을 받아 inputs 리스트에 저장
for i in  range(num):
    inputs.append(int(input()))

# for loop를 돌며 각 loop의 시작에서 push를 하며 시작
for i in range(num):
    stack.push(i+1)
    outputs.append("+")

    # idx가 전체 숫자의 개수보다 큰 경우가 이 문제를 풀지 못하는 경우
    # 그러한 경우 발생시 while에서 pop을 하지 않기 때문에 stack에 숫자가 남게 됨
    while idx < num and stack.top()==inputs[idx]:
        stack.pop()
        outputs.append("-")
        idx += 1
# 숫자가 남은 경우 이 문제를 풀지 못하는 경우 "NO"를 출력
if not stack.empty():
    print("NO")
else:
    for str in outputs:
        print(str)

# Stack(스택)이란
# 스택이란 가장 마지막에 넣은 자료가 가장 먼저 나오는 특징(LIFO: last in first out)을 가진 자료구조임.= 후입선출

# 스택의 연산
# pop(): 스택에서 가장 위에 있는 항목을 제거.
# push(item): item 하나를 스택의 가장 윗 부분에 추가.
# peek(): 스택의 가장 위에 있는 항목을 반환.
# isEmpty(): 스택이 비어 있을 때에 true를 반환.
