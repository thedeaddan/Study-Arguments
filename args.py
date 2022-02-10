import sys

if len (sys.argv) > 1:
	print ("Привет, {}!".format (sys.argv[1] ) )
else:
	name = input("Введите своё имя: ")
	print("Привет, "+name+"!")