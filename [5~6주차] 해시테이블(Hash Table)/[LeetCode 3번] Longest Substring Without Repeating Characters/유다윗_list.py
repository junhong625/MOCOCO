def lengthOfLongestSubstring(s: str) -> int:
    if s == '':                                                 # s가 빈 문자열일 경우 바로 0 리턴
        return 0

    container = []                                              # 2차원 리스트: [ [문자열의 원소, 똑같은 원소가 최초로 나오는 인덱스, 해당 원소에서 가능한 최대 길이] ]

    s_num = len(s)
    for idx, char in enumerate(s):                              # 문자열 순회
        for idx2, next_char in enumerate(s[idx+1:], idx+1):     # 원소의 다음 원소부터 순회
            if next_char == char:                               # 똑같은 원소를 발견할 경우,
                container.append([char, idx2, idx2-idx])        # container에 추가
                break
        else:                                                   # 문자열에 똑같은 원소가 없을 경우
            container.append([char, s_num, s_num-idx])

    max_len = 1                                                 # max_len 초기화
    for idx, i in enumerate(container):                         # container 순회
        if i[2] > max_len:                                      # 현재 char부터 가능한 최대 길이가 max_len보다 클 경우,
            moving_idx = idx+1                                  # 문자열을 순회를 위한 idx
            max_possible = i[2]                                 # 현재 시점에서 가능한 가장 긴 길이를 넣을 변수
            end_point = i[1]                                    # 현재 시점에서 순회가 끝나는 지점을 넣을 변수
            while True:
                if moving_idx == end_point:                     # 순회가 끝나는 지점에 도달한 경우,
                    if moving_idx-idx > max_len:                # 현재 길이가 max_len보다 더 길 경우 업데이트
                        max_len = moving_idx-idx
                    break

                if container[moving_idx][1] < end_point:        # moving_idx 원소의 '똑같은 원소가 최초로 나오는 인덱스'가 end_point 이전에 있을 경우,
                    end_point = container[moving_idx][1]        # end_point을 moving_idx 원소의 '똑같은 원소가 최초로 나오는 인덱스'로 수정
                    max_possible = end_point - idx              # max_possible을 위에서 갱신된 end_point에서 idx를 뺀 값으로 수정
                    if max_len > max_possible:                  # 현재 시점에서 최대 길이를 달성할 수 없을 경우,
                        if moving_idx-idx+1 > max_len:          # 현재 길이가 max_len보다 더 길 경우 업데이트
                            max_len = moving_idx-idx+1
                        break
                    
                moving_idx += 1
                

    return max_len

if __name__ == '__main__':
    print(lengthOfLongestSubstring("cdd"))