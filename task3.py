"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from cProfile import run
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


x = 22366844

print(f"{revers_1(x)}, Выполнено за {timeit(number=10000):.10f}")
print(f"{revers_2(x)}, Выполнено за {timeit(number=10000):.10f}")
print(f"{revers_3(x)}, Выполнено за {timeit(number=10000):.10f}")

"""Вариант решения"""


def revers_4(enter_num):
    n_list = list(str(enter_num))
    n_list.reverse()
    revers_num = "".join(n_list)

    return revers_num


print(f"{revers_4(x)}, Выполнено за {timeit(number=10000):.10f}")

run('revers_1(x)')
run('revers_2(x)')
run('revers_3(x)')
run('revers_4(x)')

"""Функции revers_3 и revers_4 почти одинаковы по времени исполнения, так как они использует функционал списков.
В первом случае используя срез, во втором используя метод .reverse. 
С другой стороны revers_3 требует меньше строчек кода"""
