import math

print('Алгоритм метода Хука-Дживса')
print('\nУравнение - F(x) = x1^4 + x1^2x2 - 6x1^2 - 1,2*x1x2 + x2^2')
d = 2
e = 0.1
h = 0.2
start_point_symplex = [1, 2]
checker = 1
print('\nКоэффициент уменьшения шага d = ', d)
print('Метод Хука-Дживса с точностью e = ', e)
print('Шаг по координатным направлениям h = ', h)
print('Начальная базисная точка x0 = ', start_point_symplex)

official_list_x1_x2 = []                                                       # главный список значений координат всех х1             
official_list2_x1_x2 = []
official_list_x1_x2 = start_point_symplex  
offical_list_value_function = []


def value_points_x1_x2(off_list1 = [], list2 = []):       # функция для нахождения значений координат х1, х2
    list2 = off_list1
    value1 = off_list1[0] + h
    value2 = off_list1[1]
    off_list1 = [value1, value2]
    return list2, off_list1

official_list2_x1_x2, official_list_x1_x2 = value_points_x1_x2(official_list_x1_x2, official_list2_x1_x2)
print('\nЗначение иксов при первой итерации: ', official_list_x1_x2)

def Value_Function(num1, num2, off_list3):                                          # Вычисление целевой функции в вершинах
    result1 = num1**4
    result2 = num1**2 * num2
    result3 = 6 * num1**2
    result4 = 1.2 * num1 * num2
    result5 = num2**2
    end_result = round((result1 + result2 - result3 - result4 + result5), 3)
    off_list3.append(end_result)
    return end_result

Value_Fx0 = Value_Function(official_list2_x1_x2[0], official_list2_x1_x2[1], offical_list_value_function)           # значения функции f(x0), f(x1)
Value_Fx1 = Value_Function(official_list_x1_x2[0], official_list_x1_x2[1], offical_list_value_function)

print('\nЗначение функции F(x0) = ', Value_Fx0)
print('Значение функции F(x1) = ', Value_Fx1)

def Function_Fp(x1 = [], x0 = []):
    result1 = list(map(lambda x, y: x - y, x1, x0))
    result2 = [0.5 * x for x in result1]
    result3 = list(map(lambda x, y: x + y, x1, result2))
    x0 = x1
    x1 = result3[:]
    return x1, x0

official_list_x1_x2, official_list2_x1_x2 = Function_Fp(official_list_x1_x2, official_list2_x1_x2)
print('\nНахождение новых координат точек X_p = ', official_list_x1_x2)


Value_Fx_p = Value_Function(official_list_x1_x2[0], official_list_x1_x2[1], offical_list_value_function)
print('Значение функции в точке F(xp) = ', Value_Fx_p)
Fx_p = Value_Fx_p

while Fx_p <= offical_list_value_function[2]:
    official_list2_x1_x2, official_list_x1_x2 = value_points_x1_x2(official_list_x1_x2, official_list2_x1_x2)
    value_Fx_n = Value_Function(official_list_x1_x2[0], official_list_x1_x2[1], offical_list_value_function)
    official_list_x1_x2, official_list2_x1_x2 = Function_Fp(official_list_x1_x2, official_list2_x1_x2)
    Value_Fx_pn = Value_Function(official_list_x1_x2[0], official_list_x1_x2[1], offical_list_value_function)
    Fx_p = Value_Fx_pn
    checker += 1
    print('\nНомер итерации = ', checker)
    print('Итерация, в которой Fx_p удовлетворяют условию: ', Fx_p)
