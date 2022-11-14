class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        # 크기 큰 순서대로, 앞의 갯수는 작은 순 대로
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        # insert method는 특정 인덱스에 해당 원소를 넣게 해 준다
        # 따라서 작은 친구가 존재할 경우, 해당 위치에 넣어주기만 하면 된다
        # 앞서 큰 친구들이 다 배치되었기 때문에 작은 친구는 해당 인덱스에 바로 위치하기만 하면 되기 때문
        return result

        # 아래는 시간 복잡도가 20배가 넘는, O(n^2) 상태
        # 
    
#         queue = [[-1,-1]]*len(people)
#         people.sort()
        
#         for i,j in people: 
            
#             greater_ele = 0
#             place_pos = 0
                        
#             while greater_ele<j:
#                 if queue[ place_pos ][0] >= i or queue[ place_pos ][0] == -1:
#                     place_pos += 1
#                     greater_ele += 1
#                 else:
#                     place_pos += 1
            
#             while queue[place_pos][0] != -1:
#                 place_pos+=1
            
#             queue[ place_pos ] = [i,j]
        
#         return queue
