# Dates of input
day1 = int(input("Contagiados día 1: "))
day2 = int(input("Contagiados día 2: "))
day3 = int(input("Contagiados día 3: "))
day4 = int(input("Contagiados día 4: "))
day5 = int(input("Contagiados día 5: "))
day6 = int(input("Contagiados dia 6: "))

# Algorithm
porcentaje1 = int((100 * (day2 - day1) / day2))
porcentaje2 = int((100 * (day3 - day2) / day3))
porcentaje3 = int((100 * (day4 - day3) / day4))
porcentaje4 = int((100 * (day5 - day4) / day5))
porcentaje5 = int((100 * (day6 - day5) / day6))
prom = int((porcentaje1 + porcentaje2 + porcentaje3 + porcentaje4 + porcentaje5) / 5)

# Print output data
print(f'Porcentaje de Contagio 1 : {porcentaje1}')
print(f'Porcentaje de Contagio 3 : {porcentaje2}')
print(f'Porcentaje de Contagio 4 : {porcentaje3}')
print(f'Porcentaje de Contagio 5 : {porcentaje4}')
print(f'Porcentaje de Contagio 5 : {porcentaje5}')
print(f'Promedio de porcentaje: {prom}')
# End of algorithm
