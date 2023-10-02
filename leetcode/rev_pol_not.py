def evaluate(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            x, y = stack.pop(), stack.pop()
            stack.append(y + x)
        elif token == '-':
            x, y = stack.pop(), stack.pop()
            stack.append(y - x)
        elif token == '*':
            x, y = stack.pop(), stack.pop()
            stack.append(y * x)
        elif token == '/':
            x, y = stack.pop(), stack.pop()
            stack.append(int(y / x))
        else:
            stack.append(int(token))
    print(stack[0])
    return stack[0]


evaluate(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
