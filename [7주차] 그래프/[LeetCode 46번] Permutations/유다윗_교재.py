# 46. Permutations
# 3시간 동안 푼 것 같은데 못 풀어서 그냥 교재 풀이를 썼습니다.

def permute(nums):
    result = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            result.append(prev_elements[:])
        
        # 순열 생성
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result


if __name__ == '__main__':
    print(permute([1,2,3]))


## 아래는 실패작 ##

# # 1. 인접행렬 구하는 함수 정의 ##
# def make_adj(n):
#     adj_matrix = [[1] * n for _ in range(n)]
#     for i in range(n):
#         adj_matrix[i][i] = 0
#     return adj_matrix

# def visited(v, adj_matrix):
#     for i in adj_matrix:
#         i[v] = 0
#     return adj_matrix

# def visited_return(v, adj_matrix):
#     for i in adj_matrix:
#         if i != v:
#             i[v] = 1
#     return adj_matrix


# ## 2. dfs 함수 정의 ##
# def dfs(n, adj_matrix):                             # n: nums의 개수
#     result = []
#     for i in range(n):                  # 인덱스 순회
#         s = []
#         pivot = [[0] * n for _ in range(n)]
#         pivot_idx = -1
#         root = []

#         root.append(i)
#         pivot_idx += 1
#         pivot[i][pivot_idx] = 1
#         adj_matrix = visited(i, adj_matrix)
#         v = i

#         while True:
#             for idx, j in enumerate(adj_matrix[v]):           # 인덱스 i에 해당하는 인접행렬의 행 순회
#                 if j == 1 and pivot[v][idx] != 1:
#                     pivot_idx += 1
#                     pivot[idx][pivot_idx] = 1

#                     s.append(v)
#                     v = j
#                     root.append(v)
#                     adj_matrix = visited(v, adj_matrix)
#                     break
#             else:                               # 더 이상 방문 가능한 정점이 없을 경우,
#                 if len(root) == n:
#                     result.append(root)             # 지금까지의 루트 result에 추가
                
#                 if s:
#                     if pivot_idx < n-1:
#                         for k in range(n):
#                             pivot[k][pivot_idx+1] = 0
#                     pivot_idx -= 1
#                     print(pivot_idx)
#                     if pivot_idx == -1:
#                         break

#                     adj_matrix = visited_return(v, adj_matrix)
#                     v = s.pop()
#                     root.pop()
#                     print(v, s, root, adj_matrix, pivot)
#                     break
                    
#                 else:
#                     break

#     return result


# def permute(nums):
#     adj_matrix = make_adj(len(nums))
#     permutaion = dfs(len(nums), adj_matrix)
#     return

# if __name__ == '__main__':
#     print(permute([0,1]))

