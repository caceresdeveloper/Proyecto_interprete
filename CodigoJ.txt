println("Cada segundo simula un minuto de viaje")

function calcular_costo_viaje(tiempo)
    tarifa_base = 5000  # Tarifa base en pesos
    tarifa_por_tiempo = 100  # Tarifa por tiempo en minutos
    
    costo_total = tarifa_base + tarifa_por_tiempo * tiempo
    return costo_total
end

tiempo = rand(1:10)
println(tiempo)

tiempo_inicial = now()

for i in 1:tiempo
    println("Viaje en proceso")
    sleep(1)  # Pausa durante 1 segundo
end

tiempo_final = now()

if tiempo > 0
    if tiempo <= 30
        costo = calcular_costo_viaje(0)
    else
        costo = calcular_costo_viaje(tiempo - 30)
    end

    println("El costo del viaje es: \$$("%.2f" % costo)")
else
    println("Error: Dato Invalido")
end
