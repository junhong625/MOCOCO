class Solution(object):
    def countOfAtoms(self, formula):
        count = {}
        group = []
        result = ""
        for i in range(len(formula)):
            if not formula[i].isdigit(): # 문자열일 경우
                if formula[i].upper() == formula[i]: # 대문자일 경우
                    group.append([str(formula[i]),1])
                else: # 소문자일 경우
                    group[-1][0] += str(formula[i])
            else: # 숫자일 경우
                c = int(formula[i])
                if formula[i-1].isdigit(): # 이미 계산했던 숫자일 경우
                    continue
                
                if i+1 < len(formula) and formula[i+1].isdigit(): # 다음 문자가 숫자인지 확인
                    c = int(formula[i]+formula[i+1])

                if group[-1][0] != ')': # 닫는 괄호가 아닐 경우
                    group[-1][1] *= c
                else: # 닫는 괄호일 경우
                    idx = 1
                    group.pop(-1) # 닫는 괄호 제거
                    while group[-idx][0] != '(': # 여는 괄호가 나올때 까지
                        group[-idx][1] *= c 
                        idx += 1
                    group.pop(-idx)
                    
        cnt = 0
        for i in range(len(group)): # group에 남아있는 괄호를 제거
            if group[i-cnt][0] in '()':
                group.pop(i-cnt)
                cnt += 1
        
        for atom in group: # 카운팅 솔트 변형 버전
            if atom[0] in count:
                count[atom[0]] += atom[1]
            else:
                count[atom[0]] = atom[1]
        
        for key in sorted(count): # 사전순으로 result에 문자열로 저장
            if count[key] == 1:
                result += key
            else:
                result += key+str(count[key])
                
        return result
                