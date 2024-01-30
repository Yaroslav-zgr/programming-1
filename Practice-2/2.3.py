def check_brackets(s): # Определение функции check_brackets, которая принимает строку s в качестве аргумента.
    stack = [] 
    longest_correct = '' 
    current_correct = '' 
    for bracket in s: # Цикл по каждому символу в строке s.
        if bracket in '([{':
            stack.append(bracket)
            current_correct += bracket
        else:
            if len(stack) == 0:
                current_correct = ''
                continue
            if bracket == ')' and stack[-1] == '(' or \
               bracket == ']' and stack[-1] == '[' or \
               bracket == '}' and stack[-1] == '{':
                stack.pop()
                current_correct += bracket
                if len(current_correct) > len(longest_correct):
                    longest_correct = current_correct
            else: 
                stack = []
                current_correct = ''
    if len(stack) == 0 and len(current_correct) == len(s):
        return True
    elif longest_correct == '':
        return False
    else:
        return longest_correct

# Пример использования:
print(check_brackets('()[]{}'))  # Выводит: True
print(check_brackets('(]'))  # Выводит: False
print(check_brackets(')()())'))  # Выводит: ()()
print(check_brackets('{[()]{[()]}}'))  # Выводит: True
print(check_brackets('{[(]){[()]}}'))  # Выводит: {[()]}