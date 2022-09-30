# 310. Minimum Height Trees

##### 포기. ###

from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def make_route(x_edges, root, new_edges):
            if x_edges:
                v = x_edges.pop(0)
                if v[0] == root:
                    new_edges.append(v)
                    make_route(x_edges, root, new_edges)
                elif v[1] == root:
                    new_edges.append([v[1], v[0]])
                    make_route(x_edges, root, new_edges)
                else:
                    new_edges.append(v)
                    make_route(x_edges, root, new_edges)
                    new_edges[-1] = [v[1], v[0]]
                    make_route(x_edges, root, new_edges)
            else:
                new_edges_all.append(new_edges[:])
        
        
        def postorder(node):
            visited[node] = 1
            print(ch_dict, root, node, visited, min_height)
            max_h = 0
            while ch_dict[node]:
                # print(ch_dict[node])
                v = ch_dict[node].pop(0)
                left = postorder(v)
                # print(left)
                if max_h < left:
                    max_h = left
            
            return max_h + 1


        nodes = [i for i in range(n)]# 모든 노드를 담은 리스트

        result = []
        min_height = n
        while nodes:
            root = nodes.pop(0)
            new_edges_all = []
            temp_e = edges[:]
            make_route(temp_e, root, [])
            
            for e in new_edges_all:
                ch_dict = defaultdict(list)
                for i in e:
                    ch_dict[i[0]].append(i[1])
                
                visited = [0] * n
                visited[root] = 1
                height = postorder(root)
                # print(root, min_height, height)
                
                if 0 not in visited and height and min_height > height:
                    min_height = height
                    result = [root]
                elif 0 not in visited and height and min_height == height:
                    result.append(root)

        return result
