def summa_3(a, b, c):
    return a + b + c


def schet_bukv(line):
    schet = 0
    for char in line:
        if char.isalpha():
            schet += 1
    return schet


def calсulate_fibonacci(first_number, iterationsCount):
    result = [first_number, 1]
    while not len(result) == iterationsCount:
        last_number = len(result) - 1
        next_number = result[last_number] + result[last_number - 1]
        result.append(next_number)
    return result

def calсulate_fibonacci_super(first_number, iterationsCount):
    result = [first_number, 1]
    while not len(result) == iterationsCount:
        last_number = len(result) - 1 + 10
        next_number = result[last_number] + result[last_number - 1]

    return result

def binary(num: str, base: int):
    result = 0

    reversed_number = num[::-1]

    current_degree = 0
    for symbol in reversed_number:
        number = int(symbol)

        next_number = number * base ** current_degree
        result += next_number

        current_degree += 1

    return result

    # 101 (10) = (1 * 10 ** 0) + (1 * 10 ** 2) = 101
    # 210

    # 1) получили число и основание в строке \/
    # 2) перевернуть число \/
    # 3) цикл прохода по каждому символу\/
    # 4) превращаем символ в число\/
    #      4*)
    # 5) определяете степень множителя\/
    # 6) высчитываете следующее значение\/
    # 7) прибавть к общему результату \/
    # 8) конец цикла \/
    # 9) возвращаете общий результат \/


file_data = ['sum 10 10 5', 'chars df12312312tdfyt', 'mult 10 10 12', 'chars jkgbjh', 'chars', 'fibonacсi 1 7',
             'decimal  afaw 7']
input_file = file_data  # = open("file_data", 'r')
for line in input_file:  # input_file:
    try:
        parametrs = line.split()
        command = parametrs[0]
        if command == 'sum':
            summ = summa_3(int(parametrs[1]), int(parametrs[2]), int(parametrs[3]))
            print(f'Сумма: {summ}')
        elif command == 'chars':
            if len(parametrs) < 2:
                raise Exception(f'Command {parametrs[0]} no parametr')
            char_count = schet_bukv(parametrs[1])
            print(f'Кол-во букв: {char_count}')
        elif command == 'fibonacсi':
            fibonacci = calсulate_fibonacci(int(parametrs[1]), int(parametrs[2]))
            print(f'Fibonacci: {fibonacci}')
        elif command == 'fibonacсi_super':
            fibonacci = calсulate_fibonacci_super(int(parametrs[1]), int(parametrs[2]))
            print(f'Fibonacci: {fibonacci}')
        else:
            raise Exception(f'Command {parametrs[0]} not found')
    except Exception as e:
        print(f'#ERROR: In {line} : {e}')
