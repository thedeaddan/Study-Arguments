import sys

if len (sys.argv) > 1: #Проверка на количество аргументов, название файла он тоже считает аргументом
	print ("Привет, {}!".format (sys.argv[1] ) ) #Вывод имени, если его ввели
else:#Если не ввели
	name = input("Введите своё имя: ")#Запрос имени
	print("Привет, "+name+"!")#Вывод введённого имени
