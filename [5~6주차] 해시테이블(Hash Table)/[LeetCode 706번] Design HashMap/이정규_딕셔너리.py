class MyHashMap(object):

    def __init__(self):
        self.Hash = ['0']                   # 0번째 값은 안쓸거니까 걍 만듦

    def put(self, key, value):
        while len(self.Hash) - 1 < key:     # 주어진 키값이 현재 Hash 길이보다 짧으면
            self.Hash.append('')            # 일단 그 값 될때까지 빈 문자열 추가
        
        self.Hash[key] = str(value)         # 밸류 문자로 할당
        

    def get(self, key):
                                            # 인덱스 에러 방지 및 해당 문자열에 값이 있으면
        if len(self.Hash) - 1 >= key and self.Hash[key]:
            return self.Hash[key]           # 리떤~
        else :
            return -1
        

    def remove(self, key):
                                            # 위에거랑 같은 거임
        if len(self.Hash) - 1 >= key and self.Hash[key]:
            self.Hash[key] = ''
        else :
            return -1                       # 791ms, 24.5mb