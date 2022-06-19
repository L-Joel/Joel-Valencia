municipios = []
habitantes = []

agregar = input("Ingrese un municipio ")
municipios.append(agregar)

agregar = int(input("Ingrese el numero de habitantes "))
habitantes.append(agregar)

agregar = input("Agrege otro municipio ")
municipios.append(agregar)

agregar = int(input("Ingrese el numero de habitantes "))
habitantes.append(agregar)

agregar = input("Agregue otro municipio ")
municipios.append(agregar)

agregar = int(input("Ingrese el numero de habitantes "))
habitantes.append(agregar)

total_habitantes = habitantes[0]+habitantes[1]+habitantes[2]

promedio_habitantes = float((habitantes[0]+habitantes[1]+habitantes[2])/3)

print("El total de habitantes es: ",total_habitantes)
print("El promedio de habitantes es: ",promedio_habitantes)