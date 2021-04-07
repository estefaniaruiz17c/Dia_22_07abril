# Diferencia de tiempo, timedelta()
print("Diferencia de tiempo, timedelta()")

from datetime import datetime, date, timedelta,time
# Creación del primer archivo de texto en replit, que contendrá los ejercicios de diferencia de tiempo del archivo 'date_time1.txt'
file_fech1time = open('fech_time1.txt', 'w')

# Primera frase del archivo nuevo
file_fech1time.write("Ejercicios de diferencia de tiempo del texto 'fech_time1.txt'\n")
file_fech1time.write("\n")

# Para acceder al archivo de texto de 'date_time1.txt' debemos abrir el texto en forma de lectura y utilizar el método read()
fech1timetext = open('date_time1.txt','r')
texto1 = fech1timetext.read()
# Es importante cerrar este archivo antes de proseguir con el código
fech1timetext.close()

# Ahora, con el método write, plasmaremos las fechas del archivo subido, en el archivo de texto creado desde acá, y ejecutaremos algunas funciones de fechas
file_fech1time.write("- Las fechas del primer texto de la 1 a la 4 en orden: \n")
# Forma de mostrar el texto tomado del archivo subido 'date_time1.txt'
file_fech1time.write(texto1)
file_fech1time.write("\n")

# Para acceder al archivo de texto de 'date_time1.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
fech1timetext = open('date_time1.txt','r')
texto1lista = fech1timetext.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
fech1timetext.close()

# De la manera como está escrito el archivo, cada fecha va acompaña de un '\n', esto debe eliminarse para que las fechas puedan entrar en el formato date. En este paso eliminaremos estos '\n' de cada fecha
print()
print(texto1lista)
print()
f1 = (texto1lista[1].rstrip('\n'))
f2 = (texto1lista[2].rstrip('\n'))
f3 = (texto1lista[3].rstrip('\n'))
f4 = (texto1lista[4].rstrip('\n'))

print(list(f3))
# Operaciones entre fechas
file_fech1time.write("\n")
file_fech1time.write("- Operaciones entre fechas, las dejaremos actualizadas: \n")
file_fech1time.write("\n")

# Sumaremos y restaremos semanas, días, horas, minutos, segundos
file_fech1time.write("- Sumaremos y restaremos semanas, días, horas, minutos, segundos: \n")

file_fech1time.write("\n")

# Definir fecha 1: usamos strptime para convertir el string al formato date
date1 = datetime.strptime(f1,'%d/%m/%Y %H:%M:%S')
file_fech1time.write("Fecha 1: ")
file_fech1time.write(str(date1))

file_fech1time.write("\n")

# Realizamos la suma de 2 semanas, 5 días, 3 horas, 20 minutos,  y 10 segundos; ponemos la respuesta en el archivo 'fech_time1.txt'
sumasdate1 = (date1 + timedelta(weeks=2, days=5, hours=3, minutes=20, seconds=10))
file_fech1time.write("Sumar 2 semanas, 5 días, 3 horas, 20 minutos,  y 10 segundos a la fecha 1: ")
file_fech1time.write(str(sumasdate1))
print(sumasdate1)

file_fech1time.write("\n")
file_fech1time.write("\n")

# Definir fecha 2: usamos strptime para convertir el string al formato date
date2 = datetime.strptime(f2,'%d/%m/%Y %H:%M:%S')
file_fech1time.write("Fecha 2: ")
file_fech1time.write(str(date2))

file_fech1time.write("\n")

# Realizamos la suma de 3.8 semanas, 8 días, 4.2 horas, -45 minutos,  y -2000 segundos; ponemos la respuesta en el archivo 'fech_time1.txt'
sumasdate2 = (date2 + timedelta(weeks=3.8, days=8, hours=4.2, minutes=-45, seconds=-2000))
file_fech1time.write("Sumar 3.8 semanas, 8 días, 4.2 horas, -45 minutos,  y -2000 segundos a la fecha 2: ")
file_fech1time.write(str(sumasdate2))
print(sumasdate2)

file_fech1time.write("\n")
file_fech1time.write("\n")

# Definir fecha 3: usamos strptime para convertir el string al formato date
date3 = datetime.strptime(f3,'%d/%m/%Y %H:%M:%S')
file_fech1time.write("Fecha 3: ")
file_fech1time.write(str(date3))

file_fech1time.write("\n")

# Realizamos la resta de -2 semanas, 3 días, -5 horas, -13 minutos,  y -500 segundos; ponemos la respuesta en el archivo 'fech_time1.txt'
restardate3 = (date3 - timedelta(weeks=-2, days=3, hours=-5, minutes=-13, seconds=-500))
file_fech1time.write("Restar -2 semanas, 3 días, -5 horas, -13 minutos,  y -500 segundos a la fecha 3: ")
file_fech1time.write(str(restardate3))
print(restardate3)

file_fech1time.write("\n")
file_fech1time.write("\n")

# Definir fecha 4: usamos strptime para convertir el string al formato date
date4 = datetime.strptime(f4,'%d/%m/%Y %H:%M:%S')
file_fech1time.write("Fecha 4: ")
file_fech1time.write(str(date4))

file_fech1time.write("\n")

# Realizamos la resta de 6 semanas, 15 días, -7 horas, -100 minutos,  y 300 segundos; ponemos la respuesta en el archivo 'fech_time1.txt'
restardate4 = (date4 - timedelta(weeks=6, days=15, hours=-7, minutes=-100, seconds=300))
file_fech1time.write("Restar 6 semanas, 15 días, -7 horas, -100 minutos,  y 300 segundos a la fecha 4: ")
file_fech1time.write(str(restardate4))
print(restardate4)

file_fech1time.write("\n")
file_fech1time.write("\n")

# Compararemos fechas actualizadas
file_fech1time.write("- Compararemos fechas actualizadas: \n")

file_fech1time.write("\n")

# Compararemos la fecha 1 y 3 ambas actualizadas
compara1 = sumasdate1>restardate3
file_fech1time.write("La fecha 3 es mayor que la fecha 1?: ")
file_fech1time.write(str(compara1))
file_fech1time.write("\n")

file_fech1time.write("\n")

# Compararemos la fecha 2 y 4 ambas actualizadas
compara2 = sumasdate2<restardate4
file_fech1time.write("La fecha 2 es menor que la fecha 4?: ")
file_fech1time.write(str(compara2))
file_fech1time.write("\n")

file_fech1time.write("\n")
# Resta de 2 fechas actualizadas
file_fech1time.write("- Resta de 2 fechas no actualizadas y actualizadas: \n")
file_fech1time.write("\n")

# Restar fechas 3 y 4 no actualizadas
restno = date3-date4
file_fech1time.write("Resta de las fechas 3 y 4 no actualizadas: ")
file_fech1time.write(str(restno))
file_fech1time.write("\n")

file_fech1time.write("\n")

# Restar fechas 3 y 4 actualizadas
restsi = restardate3-restardate4
file_fech1time.write("Resta de las fechas 3 y 4 actualizadas: ")
file_fech1time.write(str(restsi))
file_fech1time.write("\n")

file_fech1time.write("\n")

# Uso de timedelta.total_seconds()
file_fech1time.write("- timedelta.total_seconds() \n")

file_fech1time.write("\n")
# timedelta.total_seconds(): Retorna el número total de segundos contenidos en la duración
twoyears = timedelta(days=7300)
total = twoyears.total_seconds()
file_fech1time.write("El total de segundos que hay en 20 años es: ")
file_fech1time.write(str(total))

# Cerraremos el archivo creado desde replit 'fech_time1.txt'
file_fech1time.close()

print("--------"*8)


# Crear y abrir el archivo 'fech_time2.txt'
file_fech2time = open('fech_time2.tx', 'w')

# Primera frase del archivo nuevo
file_fech2time.write("Ejercicios de diferencia de tiempo del texto 'fech_time2.tx'\n")
file_fech2time.write("\n")

# Para acceder al archivo de texto de 'date_time2.txt' debemos abrir el texto en forma de lectura y utilizar el método read()
fech2timetext = open('date_time2.txt','r')
texto2 = fech2timetext.read()
# Es importante cerrar este archivo antes de proseguir con el código
fech2timetext.close()

# Ahora, con el método write, plasmaremos las fechas del archivo subido, en el archivo de texto creado desde acá, y ejecutaremos algunas funciones de fechas
file_fech2time.write("- Las fechas del segundo texto de la 1 a la 3 en orden: \n")
# Forma de mostrar el texto tomado del archivo subido 'date_time2.txt'
file_fech2time.write(texto2)
file_fech2time.write("\n")

# Para acceder al archivo de texto de 'date_time2.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
fech2timetext = open('date_time2.txt','r')
texto2lista = fech2timetext.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
fech2timetext.close() 

print((texto2lista))
print()

# De la manera como está escrito el archivo, cada fecha va acompaña de un '\n', esto debe eliminarse para que las fechas puedan entrar en el formato date. En este paso eliminaremos estos '\n' de cada fecha
day1 = (texto2lista[1].rstrip('\n'))
day2 = (texto2lista[2].rstrip('\n'))
day3 = (texto2lista[3].rstrip('\n'))

print()

# De esta manera, cada fecha queda en modo string, pero para las funciones que usaremos ahora, se requiere que los números de la fecha sean de tipo int, para eso haremos la conversión de manera individual para cada número que está separado por comas

# Cambiar cada número de string a int para la fecha 1 del texto 2, day1 
day1_year= int(day1[1:5])
print(day1_year)
day1_month= int(day1[6:8])
print(day1_month)
day1_day= int(day1[9:11])
print(day1_day)


# Cambiar cada número de string a int para la fecha 2 del texto 2, day2
day2_year= int(day2[1:5])
print(day2_year)
day2_month= int(day2[6:8])
print(day2_month)
day2_day= int(day2[9:11])
print(day2_day)
day2_hour = int(day2[12:14])

# Cambiar cada número de string a int para la fecha 3 del texto 2, day3 
day3_year= int(day3[1:5])
print(day3_year)
day3_month= int(day3[6:8])
print(day3_month)
day3_day= int(day3[9:11])
print(day3_day)
day3_hour = int(day3[12:14])


# Empezaremos con los ejercicios
file_fech2time.write("\n- Ejercicios: \n")

# timedelta() y modificar valores de la fecha, este método solo puede usarse en date(), pues al intentar usar time() sale el error de que no se pueden operar
file_fech2time.write("\n- Usando timedelta(): \n")

# A la fecha 1, vamos a aumentar los días y semanas
fech1 = date(day1_year,day1_month,day1_day)
fech1_actuali = fech1 + timedelta(days=3,weeks=2)
file_fech2time.write("\nLa fecha 1: \n")
file_fech2time.write(str(fech1))
file_fech2time.write("\nLa fecha 1 aumentando 2 semanas y 3 días: \n")
file_fech2time.write(str(fech1_actuali))
print(fech1)
print(fech1_actuali)

file_fech2time.write("\n")
# A la fecha 2, vamos a aumentando los días negativos y semanas también
fech2 = date(day2_year,day2_month,day2_day)
fech2_actuali = fech2 + timedelta(days=-7,weeks=-4)
file_fech2time.write("\nLa fecha 2: \n")
file_fech2time.write(str(fech2))
file_fech2time.write("\nLa fecha 2 aumentando -4 semanas y -7 días: \n")
file_fech2time.write(str(fech2_actuali))
print(fech2)
print(fech2_actuali)

file_fech2time.write("\n")
# A la fecha 3, vamos a dismuyendo los días  y semanas también
fech3 = date(day3_year,day3_month,day3_day)
fech3_actuali = fech3 - timedelta(days=4,weeks=3)
file_fech2time.write("\nLa fecha 3: \n")
file_fech2time.write(str(fech3))
file_fech2time.write("\nLa fecha 3 disminuyendo 3 semanas y 4 días: \n")
file_fech2time.write(str(fech3_actuali))
print(fech3)
print(fech3_actuali)

file_fech2time.write("\n")
file_fech2time.write("\n")

# Algunas funcionalidades extra de timedelta()
file_fech2time.write("- Otras funcionalidades de timedelta(): \n")

file_fech2time.write("\n")
# timedelta.max: El objeto más positivo de la timedelta
maxi = timedelta.max
print(maxi)
file_fech2time.write("- timedelta.max, El objeto más positivo de timedelta(): \n")
file_fech2time.write(str(maxi))

file_fech2time.write("\n")
file_fech2time.write("\n")

# timedelta.min: El objeto más negativo de la timedelta
mini = timedelta.min
print(mini)
file_fech2time.write("- timedelta.min, El objeto más negativo de timedelta(): \n")
file_fech2time.write(str(mini))

# Cerraremos el archivo creado desde replit 'fech_time2.txt'
file_fech2time.close()