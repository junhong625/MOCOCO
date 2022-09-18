def canFinish(numCourses, prerequisites):
    # 노드 수
    n = numCourses
    # 그래프
    graph = [[] for _ in range(n)]
    need_to_be_clear = [0] * n

    # 2번째 인자를 이수해야 1번째 수업을 들을 수 있으므로 
    for nxt, start in prerequisites:
        graph[start].append(nxt)
        need_to_be_clear[nxt] += 1

    # 수강할 수 있는 수업 목록을 스택으로
    can_take = []
    for nxt in range(n):
        # 다음 수업을 듣기 위해서 들어야 할 수업이 없다면 수강할 수 있는 목록에 추가
        if need_to_be_clear[nxt] == 0:
            can_take.append(nxt) 
    while can_take:
        start = can_take.pop()
        for nxt in graph[start]:
            # 선수과목 한개 삭제해줌
            need_to_be_clear[nxt] -= 1
            # 선수 과목에서 삭제해줬는데 0이 되면 이제 들을 수 있는 수업이니까 수강 할 수 있는 목록에 append
            if need_to_be_clear[nxt] == 0:
                can_take.append(nxt)
    # return need_to_be_clear
    # 아직 수강 못하는 과목이 남아있다면 False
    for i in need_to_be_clear:
        if i > 0:
            return False
    else:
        return True

numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

print(canFinish(numCourses, prerequisites))