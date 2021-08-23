while True:
    try:
        number1, operation, number2 = [
                i for i in
                input(
                    'Введите через пробел число операнд (+, -, *, /), число: '
                    ).split()
                ]
    except ValueError:
        print('Неправильный ввод.')
        continue
    number1 = int(number1)
    number2 = int(number2)

    if operation == '0':
        break
    elif operation == '+':
        print(f'{number1} {operation} {number2} = {number1 + number2}')
    elif operation == '-':
        print(f'{number1} {operation} {number2} = {number1 - number2}')
    elif operation == '*':
        print(f'{number1} {operation} {number2} = {number1 * number2}')
    elif operation == '/':
        try:
            print(f'{number1} {operation} {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')
