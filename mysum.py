import sys #Импорт библиотеки взаимодействия с системой

def get_nums(): #Запрос и сумма чисел с проверкой
	args = sys.argv #Запрос аргументов
	args.pop(0) #Удалить первый аргумент(Название файла)
	num_sum = 0 #Задаём начальную сумму
	
	for num in args: #Парсинг аргументов
		try:#Пробуем преобразовать строку в число
			num_sum += int(num) #Если это число, то добавляем его к общей сумме
		except Exception: #Если не число
			print("Элемент "+num+" не число!") #Сообщение о том, что элемент не является числом
	return num_sum #После оканчания парсинга отдаём число

if len (sys.argv) > 1: #Если есть аргументы
	nums = get_nums() #Запрашиваем сумму аргументов
	print("Сумма: "+str(nums)) # Выводим сумму
else:#Если нет аргументов
	print("Аргументов нет")
