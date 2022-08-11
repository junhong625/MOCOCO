class MyQueue(object):

    def __init__(self):
        self.self_que_push = []    # 넣을 때 쓸 놈
        self.self_que_pop = []     # 뺄 때 쓸 놈

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.self_que_push.append(x) # 넣을 때 쓸 놈에다가

    def pop(self):
        """
        :rtype: int
        """
        while self.self_que_push :
            self.self_que_pop.append(self.self_que_push.pop()) 
            # 넣을때 쓸 놈에서 뺄 때 쓸 놈으로 pop해서 옮기기
            # 그러면 위상이 뒤집힌다

        self_pop =  self.self_que_pop.pop() # stack[-1]값 pop
        
        while self.self_que_pop :
            self.self_que_push.append(self.self_que_pop.pop())
            # 다음 명령이 무엇일지 모르므로 초기화
        
        return self_pop # 출력
        

    def peek(self): # self.pop() 이랑 똑같은데 pop안하고 값만 할당
        """
        :rtype: int
        """
        while self.self_que_push :
            self.self_que_pop.append(self.self_que_push.pop())
        
        self_peek = self.self_que_pop[-1]
        
        while self.self_que_pop :
            self.self_que_push.append(self.q_pop.pop())
            
        return self_peek

        

    def empty(self):
        """
        :rtype: bool
        """
        
        return not self.self_que_push and not self.self_que_pop


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
