def string_conversion(text: str) -> list:
    """
    Функция преобразует строку в список для дальнейшего расчета.
    :param text: пример для расчета.
    :return: список элементов строки
    """
    text_list = text.replace('+', ' + ').replace('-', ' + -').replace('*', ' * ') \
        .replace(' *  * ', ' ** ').replace('/', ' / ').replace('(', ' ( ') \
        .replace(')', ' ) ').replace(' (  + ', ' ( ').replace('+ - (', '+ -1 * (').split()

    if text_list[0] == '+':
        text_list.pop(0)
    print(text_list)
    return text_list




def calculate_simple(task_list: list) -> float:
    """
    Функция для расчета простых примеров, не содержащих выражений в скобках.
    :param task_list: преобразованный список элементов выражения для расчета.
    :return: результат расчета математического примера - вещественное число.
    """
    operations = {
        '+': lambda x, y: float(x) + float(y),
        '*': lambda x, y: float(x) * float(y),
        '/': lambda x, y: float(x) / float(y),
        '**': lambda x, y: float(x) ** float(y)
    }

    for sign in ['**', '/', '*', '+']:
        while sign in task_list:
            i = task_list.index(sign)
            task_list[i] = operations[sign](task_list[i - 1], task_list[i + 1])
            task_list.pop(i - 1)
            task_list.pop(i)

    return task_list[0]


def calculate_middle(task_list: list) -> float:
    """
    Функция для вычисления математических операций с одинарными скобками, например (8-6)-2*(2+2)
    :param task_list: список элементов математического примера.
    :return: результат вычисления.
    """
    while '(' in task_list:
        i = task_list.index('(')
        j = task_list.index(')')
        part_brackets = task_list[i + 1:j]
        task_list = task_list[:i] + [str(calculate_simple(part_brackets))] + task_list[j + 1:]
    return calculate_simple(task_list)


def calculate_hard(task_list: list):
    """
    Функция для вычисления математических операций с вложенными скобками, например
    36/3*(2+5-(3+4))-(2+6).
    :param task_list: список элементов математического выражения.
    :return: результат вычисления.
    """
    while ')' in task_list:
        i = task_list.index(')')
        j = len(task_list[:i]) - task_list[:i][::-1].index('(') - 1
        part_parentheses = calculate_simple(task_list[j + 1:i])
        task_list = task_list[:j] + [part_parentheses] + task_list[i + 1:]
    return calculate_simple(task_list)


task_1: str = '8-6-2*2+4'
task_2: str = '36/3*(2+5-(3+4))-(2+6)'

print(calculate_hard(string_conversion(task_1)))
print(calculate_hard(string_conversion(task_2)))