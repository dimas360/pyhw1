#  Напишите программу, которая по заданному номеру четверти, 
#  показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input("Введите номер четверти:  "))

if   a == 1: print(" Первая четверть : x от 0  до + ∞, y от  0 до + ∞") 
elif a == 2: print(" Вторая четверть: x от 0 до  - ∞, y от 0  до + ∞ ")  
elif a == 3: print(" Третья четверть: x от 0 до  - ∞, y от 0  до - ∞ ")
elif a == 4: print(" Четвёртая четверть: x от 0 до  + ∞, y от 0  до - ∞ ")
else:        print("Ошибка ввода") 