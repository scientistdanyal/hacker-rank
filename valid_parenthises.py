def isValid(inp):
    pairs = dict(['()','[]','{}'])

    stack = []

    for i in inp:
        if i in '({[':
            stack.append(i)

        elif len(stack) == 0 or i != pairs[stack.pop()]:
            return False


    return len(stack) == 0        



if __name__== "__main__":

    inp = '()[]{}'
    print(isValid(inp))

