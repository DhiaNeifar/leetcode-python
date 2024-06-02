def removeKdigits(num, k):
    stack = []
    for char in num:
        if not stack and k:
            stack.append(char)
        while char < stack[-1] and k:
            k -= 1
            stack.pop()
            stack.append(char)
    first_index = 0
    for char in stack:
        if char == '0':
            first_index += 1
    return ''.join(stack[first_index:])


if __name__ == '__main__':
    num_ = '1432219'
    k_ = 3
    print(removeKdigits(num_, k_))
