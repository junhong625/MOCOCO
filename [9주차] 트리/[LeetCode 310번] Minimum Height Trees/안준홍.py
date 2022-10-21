class Solution:
    def findMinHeightTrees(self, n, edges):
        if not edges: # 비어있을 경우 
            return [0]
        
        adjList = {}
        for s, e in edges:   # 인접 리스트 생성
            if s not in adjList:
                adjList[s] = [e]
            else:
                adjList[s].append(e)
            if e not in adjList:
                adjList[e] = [s]
            else:
                adjList[e].append(s)

        result = set()      # MHT가 들어갈 변수
        while True:         # 반복문
            result = list(result) 
            for i in range(len(result)): # result의 길이만큼 반복
                a, b = result.pop(0)     # a, b에 result 첫번째 값 추출하여 할당
                if adjList:              # 인접 리스트가 있을 경우 노드 제거하고 더 이상 인접 리스트가 없는 노드 삭제
                    adjList[b].remove(a) 
                    if not adjList[b]:
                        del adjList[b]
                    adjList[a].remove(b)
                    if not adjList[a]:
                        del adjList[a]
                result.append(b)         # 제거된 노드들 중 기준 노드 result 추가
                
            result = set(result)         # set으로 변경하여 중복 제거
                
            if not adjList:              # 인접 리스트가 없을 경우 중지
                break
            result = set()               # 중지되지 않았다면 result 초기화
            
            for i in adjList:            # 인접리스트를 순회하여 인접한 노드의 개수가 1인 노드번호 추가
                if len(adjList[i]) == 1:
                    result.add((i, adjList[i][0]))
        return result