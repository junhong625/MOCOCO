# 310. Minimum Height Trees

from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 가장 많이 언급된 노드를 출발 노드로 지정
        # 딕셔너리 만들기: key:n, value:빈도
        # edges 순회하며 언급이 더 많이 된 노드를 출발로 놓기
        # 루트를 바꿔가며 최소 높이를 가진 루트를 찾아내기(최소 높이보다 큰 높이가 나오면 break)

        def preorder(n):
            nonlocal ch
            if n != -1:
                if ch[n][0] == -1:
                    return 0
                max_h = 0
                while ch[n]:
                    h = preorder(ch[n][0])
                    ch[n].pop(0)
                    if h > max_h:
                        max_h = h
                return max_h+1
            else:
                return -1
                
        node_dict = defaultdict(int)
        for edge in edges:
            for e in edge:
                node_dict[e] += 1
        node_dict = dict(sorted(node_dict.items(), key=lambda x:x[1], reverse=True))
        
        for idx, (i, j) in enumerate(edges):
            if node_dict[i] < node_dict[j]:
                edges[idx] = [j, i]
        
        min_height = n
        node_keys = list(node_dict.keys())
        result = []
        for root in node_keys:
            ch = [[-1] for _ in range(n)]

            for i, j in edges:
                if ch[i][0] == -1:
                    ch[i][0] = j
                else:
                    ch[i].append(j)
            # print(root, ch)
            max_height = preorder(root)
            print(root, max_height)
            if max_height > min_height:
                break
            print(root, max_height)
            min_height = max_height
            result.append(root)
        return result