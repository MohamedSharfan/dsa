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

    def is_match(self,ch1, ch2):
        match_dict = {
            ")" : "(",
            "]": "[",
            "}": "{"
        }
        return match_dict[ch1] == ch2

    def is_balanced(self, s):
        stack = Stack()
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.push(ch)
            if ch == ")" or ch == "]" or ch == "}":
                if stack.size() == 0:
                    return False
                if not stack.is_match(ch, stack.pop()):
                    return False
        return stack.size() == 0


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_balanced("({a+b})"))
    print(stack.is_balanced("))((a+b}{"))
    print(stack.is_balanced("((a+b))"))
    print(stack.is_balanced("((a+g))"))
    print(stack.is_balanced("))"))
    print(stack.is_balanced("[a+b]*(x+2y)*{gg+kk}"))