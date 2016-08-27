# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    count = 0
    iterator = 0
    pos = []
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(next)
            first = Bracket(next, i)
            pos.append(first.position + 1)

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                count = i+1
                break
            top = Bracket(opening_brackets_stack.pop(), i)
            a = pos.pop()
            if top.Match(next):
                continue
            else:
                count = top.position + 1
                break

        iterator += 1

    if (len(opening_brackets_stack) == 0) & (iterator > 1) & (count == 0):
        print('Success')
    elif count != 0:
        print(count)
    else:
        print(pos[-1])

    # Printing answer, write your code here
