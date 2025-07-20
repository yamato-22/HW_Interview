from typing import NoReturn, Any


class Stack:
    def __init__(self):
        self.stack_of_elem = []

    def __str__(self):
        return ",".join(self.stack_of_elem)

    def is_empty(self) -> bool:
        """ проверка стека на пустоту. Метод возвращает True или False """

        if len(self.stack_of_elem) > 0:
            return False
        return True

    def push(self, element: Any) -> NoReturn:
        """Метод добавляет новый элемент на вершину стека.
        Метод ничего не возвращает."""

        self.stack_of_elem.append(element)

    def pop(self) -> Any:
        """Метод удаляет верхний элемент стека. Стек изменяется.
        Метод возвращает верхний элемент стека"""
        if len(self.stack_of_elem) > 0:
            return self.stack_of_elem.pop(-1)
        else:
            return None

    def peek(self) -> Any:
        """Метод возвращает верхний элемент стека, но не удаляет его.
        Стек не меняется."""
        if len(self.stack_of_elem) > 0:
            return self.stack_of_elem[-1]
        else:
            return None

