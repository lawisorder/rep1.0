# На вход программе подается натуральное число в десятичной системе счисления.
# Программапереводит его в двоичную, восьмеричную и шестнадцатеричную системы счисления.
# При написании пронграммы учтены нюансы работы и вывода на экран PeCharm.


def f(x):
    return bin(x)[2:], oct(x)[2:], hex(x)[2:].upper()

n = int(input())
print(*f(n), sep='\n')