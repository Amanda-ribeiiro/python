time = float(input("Por favor, entre com o número de segundos que deseja converter:"))
day = time // (24 * 3600)
time = time % (24*3600)
hour = time // 3600
time %= 3600

min = time // 60
time %=60
seconds = time
print ("%d dias, %d horas, %d minutos e %d segundos." %(day, hour, min, seconds))
