import pytest
from stack import Stack
from check_brackets import check_brackets


def test_empty_stack():
    my_stack = Stack()
    assert my_stack.is_empty(), "Ожидали наличие пустого стека"

def test_push_stack():
    my_stack = Stack()
    tst_str = "1"
    my_stack.push(tst_str)
    assert not my_stack.is_empty(), "Ожидали не пустой стек"
    assert my_stack.peek() == tst_str, f'Ожидали наличие элемента {tst_str}'

def test_pop_stack():
    my_stack = Stack()
    tst_str = "123"
    my_stack.push(tst_str)
    assert my_stack.pop() == tst_str, f'Ожидали наличие элемента {tst_str}'
    assert my_stack.is_empty()

def test_peek_stack():
    my_stack = Stack()
    tst_str = "test"
    my_stack.push(tst_str)
    assert my_stack.peek() == tst_str

def test_push_pop_stack():
    my_stack = Stack()
    tst_str = "Hello, world"
    for l in tst_str:
        my_stack.push(l)
    output: str = ''
    while not my_stack.is_empty():
        output += my_stack.pop()
    assert tst_str == output[::-1]


@pytest.mark.parametrize('input, expected',
    (
            ('(((([{}]))))', 'Сбалансированно'),
            ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
            ('{{[()]}}', 'Сбалансированно'),
            ('}{}', 'Не сбалансированно'),
            ('{{[(])]}}', 'Не сбалансированно'),
            ('[[{())}]', 'Не сбалансированно'),
    )
)
def test_symmetric_bracket_string(input, expected):
    assert check_brackets(input) == expected