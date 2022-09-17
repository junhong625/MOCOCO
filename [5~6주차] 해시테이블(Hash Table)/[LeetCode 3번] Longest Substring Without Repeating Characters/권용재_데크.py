from collections import deque

s = 'abcabcbb'

dq = deque()
count = 0
for i in range(len(s)):
    if s[i] in dq:
        while True:
            if s[i] == dq.popleft():
                dq.append(s[i])
                break
    else:
        dq.append(s[i])
    
    if len(dq) > count:
        count = len(dq)

