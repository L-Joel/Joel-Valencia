peso_por_costal_cemento = 40
peso_por_costal_yeso = 30
peso_total = 0

costales_cemento = int(input("Ingrese el numero de costales de cemento "))

costales_yeso = int(input("Ingrese el numero de costales de yeso "))

peso_total += ((costales_cemento*peso_por_costal_cemento)+(costales_yeso*peso_por_costal_yeso))

print("La cantidad solicitada de costales de cemento es ",costales_cemento)

print("La cantidad solicitada de costales de yeso es ",costales_yeso)

print("El total de costales es de ",costales_cemento+costales_yeso)

print("El peso total es de ",peso_total ,"Kg")

condicion_traslado = peso_total > (3254/2) and peso_total < 3254

print("Se puede realizar el envio?: ",condicion_traslado)