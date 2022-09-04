class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def calcul(li):
            if li == []:
                return 1
            else:
                result = 1
                for i in li:
                    result *= i
                return result
            
            
        stack = []
        science = list(formula)
        count = collections.defaultdict(int)
        
        while science:
            back = science.pop()
            if back.isdigit():
                front = science.pop()
                # 숫자가 연속으로 여러개 나올 경우 숫자를 뽑아내도록 반복
                if front.isdigit():
                    while front.isdigit():
                        back = front + back
                        front = science.pop()
                # 앞의 문자들에 따라 동작 다르게
                # ) 면 stack에 숫자 쌓아두기
                if front == ")":
                    stack.append(int(back))
                # 대문자면 원소로 저장
                elif front.isupper():
                    count[front] += int(back) * calcul(stack)
                # 소문자면 원소 이름 다 출력하고 붙여줌
                elif front.islower():
                    new = science.pop()
                    while new.islower():
                        front = new + front
                        new = science.pop()
                    front = new + front
                    count[front] += int(back) * calcul(stack)
            else:
                # 그 외의 조건은 원소 개수 단위가 1 이거나 여는 괄호이다
                # 여는 괄호면 닫는괄호의 숫자 하나 삭제
                if back == "(":
                    if stack:
                        stack.pop()
                # 나머진 단어들 단위로 정리
                elif back.isupper():
                    count[back] += 1 * calcul(stack)
                elif back.islower():
                    front = science.pop()
                    while front.islower():
                        back = front + back
                        front = science.pop()
                    back = front + back
                    count[back] += 1 * calcul(stack)
            # print(stack)
        
        
        result = ''
        for key, value in sorted(count.items()):
            if value == 1:
                result += key
            else:
                result += key + str(value)
        return result