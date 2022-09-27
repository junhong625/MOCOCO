# 310. Minimum Height Trees

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
        
        
        
        def preorder(n, h, visited):
            nonlocal min_height
            nonlocal result
            
            visited[n] = 1
            print(root, n, visited, h)
            
            if 0 in visited:
                while ch_dict[n]:
                    v = ch_dict[n].pop(0)
                    preorder(v, h+1, visited)
                else:
                    visited[n] = 0

            else:
                if h:
                    if min_height > h:
                        min_height = h
                        result = [root]
                    elif min_height == h:
                        result.append(root)
                
            

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
                
                preorder(root, 0, [0] * n)

        return result
