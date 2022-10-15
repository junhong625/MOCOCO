class Solution(object):
    def merge(self, intervals):
        inte = sorted(intervals, key=lambda x: x[0])
        print(inte)
        # 앞에서부터 작은 친구들 순으로 병합을 진행
        merged = []
        for i in inte:
            if merged and merged[-1][1] >= i[0]:
                if merged[-1][1] < i[1]:
                    merged[-1][1] = i[1]
            else:
                merged.append(i)
        return merged
                    