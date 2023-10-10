n = int(input())

horas = n // 3600
segundos_restantes = n - (horas * 3600)

minutos = segundos_restantes // 60

segundos = n - (minutos * 60) - (horas * 3600)

print(f'{horas}:{minutos}:{segundos}')