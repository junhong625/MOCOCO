# 17_Letter Combinations of a Phone Number

from itertools import product


                                                        ## 1. 숫자-알파벳 딕셔너리 생성 ##
letters_dict = {
    '2' : ['a', 'b', 'c'],
    '3' : ['d', 'e', 'f'],
    '4' : ['g', 'h', 'i'],
    '5' : ['j', 'k', 'l'],
    '6' : ['m', 'n', 'o'],
    '7' : ['p', 'q', 'r', 's'],
    '8' : ['t', 'u', 'v'],
    '9' : ['w', 'x', 'y', 'z']
}


                                                        ## 2. 조합 구하는 함수 정의 ##
def combination(target):
    result = [] 
    combination_list = list(product(*target))           # 모든 조합 구하기
    for c in combination_list:
        result.append(''.join(c))                       # 각 케이스들을 문자열로 바꾸기
    return result


def letterCombinations(digits: str):
    if digits == '':                                    # digits이 빈문자열일 경우 바로 빈 리스트 리턴
        return []

                                                        ## 3. input 받고 target 인자 만들기 ##
    target = []
    for d in digits:
        target.append(letters_dict[d])                  # 각 digits에 해당하는 문자 리스트 target에 넣기
    
                                                        ## 4. 조합 출력 ##
    return combination(target)


if __name__ == '__main__':                              # test
    digits = '23'
    print(letterCombinations(digits))