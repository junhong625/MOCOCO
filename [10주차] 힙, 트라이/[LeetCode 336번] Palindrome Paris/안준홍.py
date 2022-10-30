class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        
        def dfs(idx=0):
            if idx == len(words):
                return
            
            for i in range(idx+1, len(words)):
                if not words[idx]:
                    if words[i] == words[i][::-1]:
                        nonlocal result
                        result.extend([[idx, i], [i, idx]])    
                elif not words[i]:
                    if words[idx] == words[idx][::-1]:
                        result.extend([[idx, i], [i, idx]])
                else:                
                    if words[idx][0] == words[i][-1]:
                        new_word = words[idx] + words[i]
                        if new_word == new_word[::-1]:
                            result.append([idx, i])
                    if words[i][0] == words[idx][-1]:
                        new_word = words[i] + words[idx]
                        if new_word == new_word[::-1]:
                            result.append([i, idx])
            dfs(idx+1)
        dfs()
        return result