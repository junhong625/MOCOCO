# 179. Largest Number
# 46ms / 13.9mb

# flow
# 1. input 리스트의 원소를 모두 문자열로 변경
# 2. 0~9를 key로 하는 딕셔너리 생성(value는 list)
# 3. input 리스트 각 원소들의 가장 큰 자릿수 값과 일치하는 딕셔너리 key의 리스트에 해당 원소 추가
# 4. 삽입 정렬로 딕셔너리 각 키의 리스트 정렬
# 5. 9~0 순으로 딕셔너리 key를 순회하며 각 원소들 붙여서 return

from collections import defaultdict
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def insert_sort(arr):                                   # 삽입 정렬
            sorted_nums = []                                    # 정렬 결과 리스트
            while arr:
                now_num = arr.pop(0)                            # 하나씩 꺼냄
                for i in range(len(sorted_nums)-1, -1, -1):     # 정렬 리스트 역순 순회
                    if len(sorted_nums[i]) == len(now_num):     # 정렬 리스트 원소와 now_num의 길이가 일치할 경우 바로 숫자 비교하여 정렬 리스트에 추가
                        if now_num <= sorted_nums[i]:
                            sorted_nums.insert(i+1, now_num)
                            break
                    else:                                       # 정렬 리스트 원소와 now_num의 길이가 일치하지 않을 경우
                        temp1 = sorted_nums[i] + now_num        
                        temp2 = now_num + sorted_nums[i]
                        if temp2 <= temp1:
                            sorted_nums.insert(i+1, now_num)
                            break
                else:                                           # sorted_nums가 비었거나, now_num이 가장 큰 경우
                    sorted_nums.insert(0, now_num)
            return sorted_nums


        nums_reverse_str = [str(i) for i in range(9, -1, -1)]
        nums_str = list(map(str, nums))                         # int -> str
        nums_dict = defaultdict(list)

        for n in nums_str:
            nums_dict[n[0]].append(n)

        result = ''
        for i in nums_reverse_str:
            if nums_dict[i]:
                result += ''.join(insert_sort(nums_dict[i]))    # values 정렬 후 result에 붙이기
        if not result.rstrip('0'):                              # result의 모든 character가 0일 경우 0 return
            return '0'
        return result