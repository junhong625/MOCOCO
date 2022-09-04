from collections import defaultdict 
'''
formula = "K4(ON(SO3)2)2"
formula = "Mg(OH)2"
'''

formula = "Mg(OH)2"
atoms = defaultdict(int)

stack = [1]
numbers = ''
somoonja = ''

reverse_formula = formula[::-1]

for element in reverse_formula:
    # 우리는 뒤에서부터 보기 떄문에 숫자 -> 괄호 -> 소문자 -> 대문자 순서로 본다
    # if number
    if element.isdigit():
        numbers = element + numbers
    # if 닫기
    elif element == ')':
        stack.append(stack[-1] * int(numbers or 1))
        numbers = ''
    # if 열기
    elif element == '(':
        stack.pop()
    # if so moon ja
    elif element.islower():
        somoonja = element + somoonja
    # if dae moon ja
    elif element.isupper():             # 대문자를 만났을 때 딕셔너리에 value 할당
        element = element + somoonja    # 대문자 + 소문자의 조합이 되어야함
        atoms[element] = atoms[element] + stack[-1]*int(numbers or 1)
        somoonja = ''
        numbers = ''

result = []

# 키로 sort해야함 문제 조건에 있음
for key, value in sorted(atoms.items()):
    if value == 1:
        value = ""
    result.append(key)
    result.append(str(value))

result_str = ''
for i in result:
    result_str += i

print(result_str)