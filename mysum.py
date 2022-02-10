import sys #Импорт библиотеки взаимодействия с системой

def get_first(): #Проверка первого числа
	try:
		return int(sys.argv[1]) #Попробовать преобразовать текст в число
	except Exception:#Если не получилось
		print("Первое число должно состоять из цифр!")#Предупреждение
def get_second():#Аналогично первому
	try:
		return int(sys.argv[2]) 
	except Exception:
		print("Второе число должно состоять из цифр!")

if len (sys.argv) > 1:#Если есть аргументы
	first_num = get_first() #Запрос первого числа
	second_num = get_second() #Запрос второго числа
	print("Сумма: "+str(first_num+second_num)) #Сумма чисел, с преобразованием в str(Python такое требует)
else:#Если нет аргументов
	print("Аргументов нет")
