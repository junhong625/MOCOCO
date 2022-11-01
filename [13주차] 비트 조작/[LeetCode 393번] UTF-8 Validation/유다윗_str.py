# 393. UTF-8 Validation
# 143ms / 14.2mb

# flow
# 1. data의 첫 번째 원소로 몇 바이트 문자인지 확인
# 2. 바이트에 따른 sequence가 유효한지 판별 

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check_bytes(element):
            if element[0] == '0':                       # 1 byte
                return 0
            elif element[:3] == '110':                  # 2 bytes
                return 1
            elif element[:4] == '1110':                 # 3 bytes
                return 2
            elif element[:5] == '11110':                # 4 bytes
                return 3
            else:                                       # 유효하지 않은 값
                return False
        

        while data:
            element = bin(data.pop(0))[2:].zfill(8)     # 2진수
            check_nums = check_bytes(element)
            if type(check_nums) != int:                 # False를 리턴 받으면 False로 종료
                return False
            
            while check_nums > 0:                       # sequence가 유효한지 체크
                if not data:                            # 체크해야 할 sequence가 있음에도 더 이상 data에 원소가 없을 경우
                    return False
                sequence = bin(data.pop(0))[2:].zfill(8)

                if sequence[:2] != '10':                # sequnce는 반드시 10으로 시작해야 함
                    return False
                check_nums -= 1
        return True                                     # data의 모든 원소 체크가 완료된 경우