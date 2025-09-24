length = int(input("Введите длину прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))
if length < 0 or width < 0:
    print("Вы ввели отрицательное число")
else:
    area = length * width
    perim = (length + width) * 2
    print("Площадь прямоугольника равна:", area, "\nПериметр равен:", perim)
