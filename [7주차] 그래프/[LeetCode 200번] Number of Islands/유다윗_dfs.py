# 200_Number_of_Islands
# LeetCode에 제출할 때에는 dfs 함수를 numIslands 함수 안에 넣어야 정상적으로 작동함


delta = [[0,1], [1,0], [0,-1], [-1,0]]                                                      # 동, 남, 서, 북

## 1. dfs 함수 정의 ##
def dfs(v: list):
    if not(0<=v[0]<len(grid)) or not(0<=v[1]<len(grid[0])) or grid[v[0]][v[1]] == '0':      # 종료 조건: 더 이상 육지가 아닌 경우,
        return                                                                          

    grid[v[0]][v[1]] = '0'                                                                  # 방문한 정점의 값 0으로 바꾸기
    
    dfs([v[0] + delta[0][0], v[1] + delta[0][1]])                                           # 동
    dfs([v[0] + delta[1][0], v[1] + delta[1][1]])                                           # 남
    dfs([v[0] + delta[2][0], v[1] + delta[2][1]])                                           # 서
    dfs([v[0] + delta[3][0], v[1] + delta[3][1]])                                           # 북


def numIslands(grid):
    islands = 0

    for row in range(len(grid)):                                                            # 행 순회
        for col in range(len(grid[0])):                                                     # 열 순회
            ## 2. 섬 카운트 ##
            if grid[row][col] == '1':                                                       # 육지이면, dfs 실행
                dfs([row, col])
                islands += 1                                                                # dfs 끝나면 섬의 수 +1
    
    return islands


if __name__ == '__main__':                                                                  # 테스트
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(grid)) # 1