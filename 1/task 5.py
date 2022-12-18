# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#  https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
# AB = √(xb - xa)2 + (yb - ya)2

xA = int(input("Input X point A: "))
yA = int(input("Input Y point A: "))
xB = int(input("Input X point B: "))
yB = int(input("Input Y point B: "))


AB = (((xB - xA) ** 2) + ((yB - yA) ** 2)) ** 0.5

print(round(AB, 3))