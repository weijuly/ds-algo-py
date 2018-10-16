def sort_stack(stack):
    if len(stack) <= 1:
        return stack
    tstack = []
    while stack:
        tstack.append(stack.pop())
        if stack and tstack[-1] < stack[-1]:
            elem = stack.pop()
            while tstack and tstack[-1] < elem:
                stack.append(tstack.pop())
            stack.append(elem)
            while tstack:
                stack.append(tstack.pop())
    while tstack:
        stack.append(tstack.pop())
    return stack


def sort_stack2(stack):
    if len(stack) <= 1:
        return stack
    tstack = []
    while stack:
        elem = stack.pop()
        while tstack and tstack[-1] > elem:
            stack.append(tstack.pop())
        tstack.append(elem)
    return tstack


def sort_insert_r(stack, v):
    if not stack:
        return [v]
    if v > stack[-1]:
        return stack + [v]
    top = stack.pop()
    stack = sort_insert_r(stack, v)
    stack.append(top)
    return stack + [top]


def sort_stack_r(stack):
    if len(stack) <= 1:
        return stack
    top = stack.pop()
    return sort_insert_r(sort_stack_r(stack), top)
