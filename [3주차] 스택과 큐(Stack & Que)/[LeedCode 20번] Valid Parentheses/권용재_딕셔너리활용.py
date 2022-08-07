class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        brackets = {'(':')', '{':'}','[':']'}      #딕셔너리에 Key값을 여는 괄호로, Value 값을 닫는 괄호로 설정
        stack = []                                 #Stack 을 사용할 빈 리스트 생성
  
        for i in s:
            if i in brackets:                      #string 값을 순회하여 Key 값이 있을 경우 스택 list에 추가
                stack.append(i)
                
            elif len(stack) == 0:                  #input 으로 닫는 괄호가 들어올 처음으로 경우 False 처리 (닫는 괄호의 경우 value 값으로 설정이 되어있기 때문에 위의 if문에서 stack에 추가되지 않는다.)
                return False                       #혹은 아무 입력값이 없는 경우나 이상한 문자열이 들어와도 False 처리 가능. (Dictionary만 참조하여 stack에 추가하고 있기 때문에)
            
            elif brackets[stack.pop()] != i:       # 인덱싱을 할 때도 stack.pop을 사용하면 자연스레  stack에서 마지막 push가 사라짐.
                return False                       # 잎에서 '(' 가 들어오고 뒤에 '}' 이게 들어오면 닫히는 괄호가 for 문을 돌면 여기서  False
                                                   # 한마디로 아무리 페어가 맞아도 처음 닫히기 시작하는 곳 부터 페어가 맞지 않으면 False가 나와야함.
            
        return len(stack) == 0                     # pop이 모두 완료가 되었다면 stack은 빈 리스트 일 것이기 때문에  True가 나와야함 
    