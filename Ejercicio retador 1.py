print("Informacion sobre el estado de sinaloa")

#Datos
superficie = " 57 mil 365 Km^2."
ubicacion = " Al noroeste del pais."
clima = " Calido, Subhumedo, Seco y Semiseco"
temp_media_anual = float(25.45) 
precip_anual_promedio = float(790.1)
poblacion_mujeres = 1532128
poblacion_hombres = 1494815
municipios_con_mas_habitantes = "Culiacan y Mazatlan"
porcentaje_habitantes_culiacan = float(33.15)
porcentaje_habitantes_mazatlan = float(16.57)

# Variable adicional 1 (poblacion total)
poblacion_total = poblacion_hombres + poblacion_mujeres

#Variable adicional 2 (% total Mazatlan-Culiacan)
porcentaje_poblacion_culiacan_mazatlan = porcentaje_habitantes_culiacan + porcentaje_habitantes_mazatlan

# Variable adicoinal 3 (Temp. media anual y climas)
temp_y_climas = clima, temp_media_anual

# Secuencia de datos a mostrar
print("Tiene una superficie de ",superficie)

print("Se localiza ", ubicacion)

print("El clima es por lo general ", clima,"Con una temperatura media anual de ",temp_media_anual,"°C")

print("y una precipitacion anual promedio de ",precip_anual_promedio,"mm")

print("Ademas cuenta con una poblacion de ",poblacion_mujeres ,"mujeres ","Y ",poblacion_hombres ,"hombres")

print("y una poblacion total de ", poblacion_total ,"habitantes")

print("siendo ",municipios_con_mas_habitantes ,"los municipios con mas habitantes con ",porcentaje_habitantes_culiacan,"%" ,"y",porcentaje_habitantes_mazatlan,"%" ,"respectivamente")

print("y un porcentaje total entre los dos municipios de ",porcentaje_poblacion_culiacan_mazatlan ,"%")

print("siendo un estado con climas y temperatura media anual de ",temp_y_climas ,"°C" , "a lo largo de toda su extension territorial")
