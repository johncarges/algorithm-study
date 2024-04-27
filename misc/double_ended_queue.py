from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')


print(stack.pop()) # c
# a, b
print(stack.pop()) # b
# a

stack.appendleft('d')
print(stack.pop())

