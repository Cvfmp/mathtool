import sys
import math

MAX_VALUE = 10000 # ввел максимальное значение

if len(sys.argv) == 1 or sys.argv[1] == "--help": # проверил первый параметр запуска (его отсутствие либо help), если да, то далее справка.
    print("mathtool - решение уравнений вида A*x^2 + B*x + C = 0")
    print()
    print("Туториал:")
    print("  python mathtool.py                          вывод справки")
    print("  python mathtool.py --help                   вывод справки")
    print("  python mathtool.py solve                    ввод коэффициентов с клавиатуры")
    print("  python mathtool.py solve -a 1 -b -3 -c 2    решение с заданными коэффициентами")
    print()
    print("Коэффициенты A, B, C - целые числа, по модулю не больше 10000.")
    sys.exit(0)

if sys.argv[1] != "solve": # проверил, является ли первое слово solve'ом, если нет, код возврата 1 и ошибко.
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

if len(sys.argv) == 2: # Если длина списка 2 (то есть имя файла + solve, то прошу ввести коэффициенты самостоятельно)
    a_str = input("Введите A: ")
    b_str = input("Введите B: ")
    c_str = input("Введите C: ")

elif len(sys.argv) == 8: # если прошлое ложь, тогда длина должна быть 8 элементов, если так, то проверим, что там реально коэффициенты abc, а не gbl
    if sys.argv[2] != "-a" or sys.argv[4] != "-b" or sys.argv[6] != "-c":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)
    a_str = sys.argv[3] #записываем в переменные значения коэффициентов
    b_str = sys.argv[5]
    c_str = sys.argv[7]

else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    sys.exit(1)

try: # пробуем перевести в интовый тип все переменные (инпут их делает текстовыми), если все окей, то дальше, либо ошибку
    A = int(a_str)
    B = int(b_str)
    C = int(c_str)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

if abs(A) > MAX_VALUE or abs(B) > MAX_VALUE or abs(C) > MAX_VALUE: # проверяем на удовлетворение условию
    print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)

if A == 0 and B == 0:
    print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
    sys.exit(1)

elif A == 0:
    print("Уравнение линейное")
    x = -C / B
    print(f"x = {x:.3f}")

else:
    print("Уравнение квадротное")
    D = B * B - 4 * A * C
    print(f"D = {D}")

    if D > 0:
        x1 = (-B + math.sqrt(D)) / (2 * A)
        x2 = (-B - math.sqrt(D)) / (2 * A)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif D == 0:
        x = -B / (2 * A)
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")

sys.exit(0)
