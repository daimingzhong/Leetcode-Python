def prefixToPostfix(prefixes):
    result = []
    for item in prefixes:
        current = []
        n = len(item)
        for i in range(n - 1, -1, -1):
            if item[i].isdigit():
                current.append(item[i])
            else:
                left = current.pop()
                right = current.pop()
                current.append(left + right + item[i])
        result.append(current.pop())
    return result

a = []
a.append("+1*23")
print(prefixToPostfix(a))
