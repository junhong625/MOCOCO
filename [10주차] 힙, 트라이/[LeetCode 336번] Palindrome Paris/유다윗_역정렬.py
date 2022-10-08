# 105에서 시간초과

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        palindromes = []

        for idx, w in enumerate(words):
            for idx2, w2 in enumerate(words[idx+1:], idx+1):
                word_all = w + w2
                if word_all == word_all[::-1]:
                    palindromes.append([idx, idx2])
                word_all = w2 + w
                if word_all == word_all[::-1]:
                    palindromes.append([idx2, idx])
        return palindromes