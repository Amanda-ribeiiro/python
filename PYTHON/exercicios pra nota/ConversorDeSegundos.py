segundos_str = input("Por favor, entre com o numero de segundos que deseja converter: ")

total_segs = int(segundos_str)
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
horas = total_segs // 3600
segs_restantes_final = segs_restantes % 60
dias = horas // (24 * 3600)

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")