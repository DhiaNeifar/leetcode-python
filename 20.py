def main(s):
    stack = []
    for char in s:
        if char in ['{', '(', '[']:
            stack.append(char)
        else:
            if (stack and
                    ((char == '}' and stack[-1] == '{')
                     or (char == ']' and stack[-1] == '[')
                     or (char == ')' and stack[-1] == '('))):
                stack.pop()
            else:
                return False

    if len(stack):
        return False
    return True


if __name__ == '__main__':
    _s = '(()'
    main(_s)
