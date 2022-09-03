import copy
class MyStack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)
    
    def top(self):
        # 리스트의 마지막 원소 출력
        return self.s[-1]
    
    def pop(self):
        # 리스트의 마지막 원소 삭제 및 출력
        return self.s.pop()
    
    def empty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

class MyQueue(MyStack):
    def __init__(self):
        super().__init__()

    def peek(self):
        top = 0
        # t=0 -> top을 얻는 과정
        # t=1 -> 스택을 다시 돌려놓는 과정
        for t in range(2): 
            temp = []
            for i in range(len(self.s)): # 스택 원소 수만큼 순회
                temp.append(super().pop()) # 스택의 마지막 원소 빼서 temp에 넣기
            self.s = copy.deepcopy(temp) # temp를 deepcopy
            if t == 0:
                top = self.top()
        return top
    
    def pop(self):
        popped = 0
        # t=0 -> top을 얻는 과정
        # t=1 -> 스택을 다시 돌려놓는 과정(단, 마지막 원소는 제외된 상태)
        for t in range(2):
            temp = []
            for i in range(len(self.s)):
                temp.append(super().pop())
            self.s = copy.deepcopy(temp)
            if t == 0:
                popped = super().pop()
        return popped

# a = MyQueue()
# a.push(1)
# a.push(2)
# a.push(3)
# print(a.pop())
# print(a.peek())
# print(a.s)
# print(a.pop())
# print(a.s)


import copy
s = ")()())"
s_list = list(s)
max_len = 0
temp_max_len = 0
idx = 0
count_list = [0] * len(s_list)

while idx < len(s_list)-1:
    stack = []
    if s_list[idx] == '(':
        stack.append(s_list[idx])
        start = copy.deepcopy(idx)

        while idx < len(s_list) -1:
            idx += 1
            if s_list[idx] == '(':
                stack.append(s_list[idx])
                continue
            else: # s_list[idx] == ')'
                if not stack:
                    break

                else:
                    stack.pop()
                    temp_max_len += 2
                    count_list[idx] = 2
        if not stack == False: # 모든 '('가 처리되지 못했을 경우
            target_idx = count_list[start:].index(0)
            unvalid_count = 0
            for c in count_list[target_idx:idx]:
                unvalid_count += c
            temp_max_len -= unvalid_count
        if (max_len < temp_max_len):
            max_len, temp_max_len = temp_max_len, 0
    else:
        idx += 1

print(max_len)