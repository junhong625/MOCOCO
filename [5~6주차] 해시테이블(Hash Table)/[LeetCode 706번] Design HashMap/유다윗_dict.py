class MyHashMap:

    def __init__(self):
        self.hash = {}                                                      # 딕셔너리 생성

    def put(self, key: int, value: int) -> None:
        self.hash.update({                                                  # key가 이미 존재하면 덮어씀
            key : value
        })

    def get(self, key: int) -> int:
        return self.hash.get(key) if self.hash.get(key) != None else -1     # get 메서드가 None을 반환하면 -1, 아니면 value 리턴
        

    def remove(self, key: int) -> None:
        try:                                                                # 존재하지 않는 key가 입력되었을 때 아무런 작업하지 않음
            self.hash.pop(key)
        except:
            pass