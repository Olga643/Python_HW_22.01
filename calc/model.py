# my_list = ''

def change_equation(my_list: str) -> list:
  # global my_list
  my_list = my_list.replace(' ', '').\
  replace('+', ' + ').replace('-', ' - ').\
  replace('*', ' * ').replace('/', ' / ')
  print(my_list)
  if my_list.startswith(' - '):
    my_list = '-' + my_list[3:]
  my_list = my_list.split()
  return my_list


def calculation(example: list) -> float:
  global my_list
  operation = {
        '+': lambda x, y: float(x) + float(y),
        '-': lambda x, y: float(x) - float(y),
        '*': lambda x, y: float(x) * float(y),
        '/': lambda x, y: float(x) / float(y),}
  
  for sign in ['*', '/', '-', '+']:
        while sign in example:
            i = example.index(sign)
            example[i] = operation[sign](example[i - 1], example[i + 1])
            example.pop(i - 1)
            example.pop(i)
  
  return example[0]

