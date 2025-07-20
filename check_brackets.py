from stack import Stack

def check_brackets(brackets: str) -> str:
    match = {'(': ')', '[': ']', '{': '}'}
    my_stack = Stack()
    for i in brackets:
        if i in ['(', '[', '{']:
            my_stack.push(i)
        elif my_stack.is_empty() or match[my_stack.pop()] != i:
            return 'Не сбалансированно'

    return 'Сбалансированно' if my_stack.is_empty() else 'Не сбалансированно'
