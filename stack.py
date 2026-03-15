    from collections import deque
    class Stack:
        def __init__(self):
            self.container = deque()
        def push(self, item: object) -> None:
            self.container.append(item)
        def pop(self):
            return self.container.pop()
        def peek(self):
            return self.container[-1]
        def isEmpty(self):
            return len(self.container) == 0
        def size(self):
            return  len(self.container)


    def reversee(self, item):
        reversed_item = ""
        for i in item:
            self.push(i)
        while not self.isEmpty():
            top = self.pop()
            reversed_item += top
        return reversed_item

class Main:
    def __init__(self):
        self.stack = Stack()
        result = self.stack.reversee("We will conquer COVID-19")
        print(result)

Main()




