class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.max_len = k
        self.fp = 0 # front pointer
        self.rp = 0 # rear pointer
        

    def enQueue(self, value: int) -> bool:
        # rear포인터 위치에 값을 추가하고 rear포인터를 다음으로 넘기는 작업 수행해야 함
        if self.q[self.rp] == None:
            self.q[self.rp] = value
            self.rp = (self.rp + 1) % self.max_len
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        # front포인터 위치의 값을 삭제하고 front포인터를 다음으로 넘기는 작업 수행해야 함
        if self.q[self.fp] != None:
            self.q[self.fp] = None
            self.fp = (self.fp + 1) % self.max_len
            return True
        else:
            False

    def Front(self) -> int:
        if self.q[self.fp] != None:
            return self.q[self.fp]
        else:
            return -1

    def Rear(self) -> int:
        if self.q[(self.rp-1)%self.max_len] != None:
            return self.q[(self.rp-1)%self.max_len]
        else:
            return -1

    def isEmpty(self) -> bool:
        if (self.fp == self.rp) and (self.q[self.fp] == None):
            return True
        else:
            return False

    # def isFull(self) -> bool:
    #     if (self.fp == self.rp) and (self.q[self.fp] != None):
    #         return True
    #     else:
    #         return False

    def isFull(self) -> bool:
        if self.isEmpty() == True:
            return False
        else:
            return False