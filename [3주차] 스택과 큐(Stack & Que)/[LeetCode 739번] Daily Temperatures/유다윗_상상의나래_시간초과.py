
# T = temperatures
# result = []
# for i in range(len(T)): # 온도 순회
#     days = 1
#     for j in range(i+1, len(T)): # 위에서 선택된 온도의 다음 온도부터 하나씩 순회
#         if T[j] > T[i]: # j번째 온도가 i번째 온도보다 더 높을 경우
#             result.append(days)
#             break
#         else:
#             days += 1
#     else: # break가 안 걸린 경우, 즉 더 높은 온도가 없을 경우
#         result.append(0)
# return result

##################################
######### 시간 초과 발생 ##########
##################################


########################################################
# 위에서 통과 못한 케이스는 통과했으나 여전히 시간초과 #
########################################################

# 최종 결과를 담을 리스트
result = [0] * len(temperatures)
# 바로 처리되지 않은 온도의 인덱스를 넣어둘 리스트
unsolved = []
solved = 0
for t in range(len(temperatures)-1):
    today = temperatures[t]
    tomorrow = temperatures[t+1]

    temp = 0
    for u in unsolved[solved: ]:
        if u[0] < tomorrow:
            result[u[1]] = t+1-u[1]
            temp += 1
        else:
            # 더 이상 tomorrow보다 낮은 온도가 없을 경우 break
            break
    solved += temp


print(result)
    
    

        



