# stack: first in last out []
"""
push(value)
pop()
peek()
is_empty()
"""


class MyStack():
    # use list
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)  # why this one doesn't have return value

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    my_stack = MyStack()
    for i in range(50):
        my_stack.push(i)

    while not my_stack.is_empty():
        print(my_stack.pop(), end=' ')
    print()
