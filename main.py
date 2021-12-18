import math
import sys

print("Введите коэффициенты для уравнения")
print("ax^4 + bx^2 + c = 0:")

a = 0
b = 0
c = 0
count = 0

count = float(input("введите 1, если программа запускается в CMD, иначе 2 = "))


def Number():
    global a, b, c, count
    if count == 1:
        count += 1
        try:
            a = sys.argv[1]
            b = sys.argv[2]
            c = sys.argv[3]
        except:
            print("Введены неверные данные")
            Number()
    else:
        a = input("a = ")
        b = input("b = ")
        c = input("c = ")
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        Number()


if (a and b and c) == 0:
    Number()

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
print("Корни ур-я:")
if discr > 0:
    t1 = (-b + math.sqrt(discr)) / (2 * a)
    t2 = (-b - math.sqrt(discr)) / (2 * a)
    if t1 > 0:
        x = math.sqrt(t1)
        print("x = %.2f \nx = %.2f" % (x, -x))
    if t1 == 0:
        print("x = %.2f", t1)
    if t1 < 0:
        print("x = нет корня \nx = нет корня")
    if t2 > 0:
        x = math.sqrt(t2)
        print("x = %.2f \nx = %.2f" % (x, -x))
    if t2 == 0:
        print("x = %.2f", t2)
    if t2 < 0:
        print("x = нет корня \nx = нет корня")
elif discr == 0:
    x = -b / (2 * a)
    if x > 0:
        x = math.sqrt(x)
        print("x1 = %.2f \nx2 = %.2f" % (x, -x))
    if x == 0:
        print("x2 = %.2f", x)
    if x < 0:
        print("x1 = нет корня \nx2 = нет корня")

else:
    print("Корней нет")
