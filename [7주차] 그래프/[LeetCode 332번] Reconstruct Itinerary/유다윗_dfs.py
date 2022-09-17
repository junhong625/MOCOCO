# 332. Reconstruct Itinerary
# 질문1: dfs 재귀에서 route[:]가 아닌 route를 넣으면 route에 v가 계속 추가되거나 결과가 제대로 안 나오는 이유
# 질문2: result = route[:]가 안 되는 이유
# 질문3: result.append(route)가 되는 이유
# 질문4: dfs 함수를 find-함수 밖에 넣으면 문제가 생기는 이유


def findItinerary(tickets):
                                                            ## 1. 인접 리스트 만들기 ##
    adj_list = {}
    for t, f in tickets:
        try:                                                # 딕셔너리에 쌍(pair)이 이미 추가되어 있는 경우                        
            adj_list[t].append(f)
        except:                                             # 딕셔너리에 쌍(pair)을 새로 등록하는 경우
            adj_list[t] = []
            adj_list[t].append(f)

    ticket_nums = len(tickets)                              # tickets 개수

                                                            ## 2. 인접 리스트의 원소 리스트 정렬하기 ##
    for k in adj_list.keys():
        adj_list[k].sort()

                                                            ## 3. dfs ##
    def dfs(v, route):
        route.append(v)                                     # 방문 시 route에 추가
        if v not in adj_list.keys() or adj_list[v] == []:   # 더 이상 목적지가 없는 경우,
            if ticket_nums+1 == len(route):                 # 티켓을 모두 소진했으면,
                result.extend(route)                        # result에 route를 extend하고 종료
                return
        else:                                               # 아직 목적지가 남은 경우,
            for idx, i in enumerate(adj_list[v]):           # 목적지 순회
                adj_list[v].remove(i)                       # 목적지 제거
                dfs(i, route[:])                            # 재귀
                if result:                                  # 재귀 후 경로가 나온 상태라면 for문 break(최초 경로가 smallest lexical order이기 때문에 가능)
                    break
                adj_list[v].insert(idx, i)                  # 목적지 원상복귀

    result = []
    dfs('JFK', [])

    return result





## 이게 안 되는 이유(dfs의 인자로 route를 설정하지 않음)
## break가 안 걸림
## input: [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
## output: ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","ADL","EZE","AUA","AXA","TIA","ADL","EZE","TIA","ADL","EZE","TIA","AUA","AXA","EZE","AUA","AXA","EZE","TIA","ADL","EZE","TIA","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","EZE","AUA","AXA","EZE","ANU","JFK","AXA","TIA","ADL","EZE","TIA","ADL","EZE","ANU","JFK","AXA","EZE","EZE","ANU","JFK","AXA","EZE","TIA","ADL","EZE","AUA","AXA","TIA","ADL","EZE","TIA","ADL","EZE","TIA","AUA","AXA","EZE","AUA","AXA","EZE","TIA","ADL","EZE","TIA","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","EZE","AUA","AXA","EZE","ANU","JFK","AXA","TIA","ADL","EZE","TIA","ADL","EZE","ANU","JFK","AXA","EZE","ANU","JFK","AXA","EZE","ADL","EZE","TIA","ADL","EZE","AUA","AXA","TIA","ADL","EZE","EZE","TIA","ADL","EZE","AUA","AXA","TIA","ADL","EZE","TIA","ADL","EZE","ADL","EZE","EZE","ADL","EZE","AUA","AXA","TIA","ADL","EZE","ADL","EZE","EZE","ADL","EZE","TIA","ADL","EZE","ADL","EZE","TIA","AUA","AXA","EZE","TIA","AU...
def findItinerary(tickets):
    ## 1. 인접 리스트 만들기 ##
    adj_list = {}
    for t, f in tickets:
        try:
            adj_list[t].append(f)
        except:
            adj_list[t] = []
            adj_list[t].append(f)

    ticket_nums = len(tickets)

    ## 2. 인접 리스트의 원소 리스트 정렬하기 ##
    for k in adj_list.keys():
        adj_list[k].sort()


    ## 3. dfs ##
    def dfs(v):
        route.append(v)
        if v not in adj_list.keys() or adj_list[v] == []:
            if ticket_nums+1 == len(route):
                return
            else:
                route.pop()
        else:
            for idx, i in enumerate(adj_list[v]):
                adj_list[v].remove(i)
                dfs(i)
                if len(route) == ticket_nums+1:
                    break
                adj_list[v].insert(idx, i)

    route = []
    dfs('JFK')

    return route


if __name__ == '__main__':
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(findItinerary(tickets))

        # ## 3. dfs ##
    # stack = [''] * 300
    # top = -1
    # route_idx = -1
    # route = [[]] * 300

    # v = 'JFK'
    # while True:
    #     for arrival in list(adj_list[v]):
    #         if adj_list[arrival[0]] == []:
    #             if route_idx != ticket_nums:
    #                 continue
    #         if route_idx+1 in arrival[1]:
    #             continue
    #         top += 1
    #         stack[top] = v
    #         adj_list[v].remove(arrival)
    #         v = arrival[0]
    #         route_idx += 1
    #         route[route_idx] = arrival
    #         break

    #     else:
    #         if top != -1:
    #             temp = route[route_idx][:]
    #             temp[1].append(route_idx)
    #             adj_list[v].append(temp)
    #             adj_list[v].sort(key=sort_key)
    #             route_idx -= 1
    #             v = stack[top]
    #             top -= 1

    #         else:
    #             break
    # result = []
    # for r in route[:route_idx+1]:
    #     print(r)
    #     result.append(r[0])
    # return result