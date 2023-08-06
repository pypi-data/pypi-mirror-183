# lptransportsolver (C) Stanislav Chubar. 2022-2023 All rights reserved
# def solve(a:list, b:list, prise:list) -> None:
#     sum_a = sum(a)
#     sum_b = sum(b)
#     if sum_a == sum_b:
#         print("Problem is close type.")
#
#     elif sum_a > sum_b:
#         print("Problem is open type. Profit.")
#     else:
#         print("Problem is open type. Debit.")


# from pulp import *
# import time
# start = time.time()
# x1 = pulp.LpVariable("x1", lowBound=0)
# x2 = pulp.LpVariable("x2", lowBound=0)
# x3 = pulp.LpVariable("x3", lowBound=0)
# x4 = pulp.LpVariable("x4", lowBound=0)
# x5 = pulp.LpVariable("x5", lowBound=0)
# x6 = pulp.LpVariable("x6", lowBound=0)
# x7 = pulp.LpVariable("x7", lowBound=0)
# x8 = pulp.LpVariable("x8", lowBound=0)
# x9 = pulp.LpVariable("x9", lowBound=0)
# problem = pulp.LpProblem('0',pulp.LpMaximize)
# problem += -7*x1 - 3*x2 - 6* x3 - 4*x4 - 8*x5 -2* x6-1*x7- 5*x8-9* x9, "Функция цели"
# problem +=x1 + x2 +x3<= 74,"1"
# problem +=x4 + x5 +x6 <= 40, "2"
# problem +=x7 + x8+ x9 <= 36, "3"
# problem +=x1+ x4+ x7 == 20, "4"
# problem +=x2+x5+ x8 == 45, "5"
# problem +=x3 + x6+x9 == 30, "6"
# problem.solve()
# print ("Результат:")
# for variable in problem.variables():
#     print (variable.name, "=", variable.varValue)
# print ("Стоимость доставки:")
# print (abs(value(problem.objective)))
# stop = time.time()
# print ("Время :")
# print(stop - start)

from scipy import optimize
from scipy.optimize import linprog
import time

start = time.time()
c = [7, 3, 6, 4, 8, 2, 1, 5, 9]
A_ub = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1]]
b_ub = [74, 40, 36]
A_eq = [[1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1]]
b_eq = [20, 45, 30]
print(linprog(c, A_ub, b_ub, A_eq, b_eq))
stop = time.time()
print("Время :")
print(stop - start)
scipy.optimize