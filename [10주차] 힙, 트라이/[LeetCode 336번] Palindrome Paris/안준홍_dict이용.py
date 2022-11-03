class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        new_words = {val:idx for idx, val in enumerate(words)}
        for word in new_words:
            for i in range(len(word)):
                target = word[:i][::-1]
                target2 = word[-i:][::-1]
                if word != target:
                    new_word = word + target
                    if new_word == new_word[::-1] and target in new_words:
                        if target == '':
                            result.append([new_words[target], new_words[word]])
                        result.append([new_words[word], new_words[target]])
                if word != target2:
                    new_word = target2 + word
                    if new_word == new_word[::-1] and target2 in new_words:
                        if target2 == '':
                            result.append([new_words[word], new_words[target2]])
                        result.append([new_words[target2], new_words[word]])
        return result