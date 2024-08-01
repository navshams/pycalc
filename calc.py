def compute(expression):
    # 2 + 32
    values = expression.split(' ')
    # -> 2,+,32
    num0 = int(values[0]) #2
    operator = values[1]  #+
    num1 = int(values[2]) #34
    if operator == '+':
        return num0 + num1
    else:
        print('unknown operator!')
        return 0