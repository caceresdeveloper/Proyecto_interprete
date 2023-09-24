# Proyecto_interprete

# Codigo en ruby
puts "Cada segundo simula un minuto de viaje"

def calcular_costo_viaje(tiempo)
    tarifa_base = 5000  # Tarifa base en pesos
    tarifa_por_tiempo = 100  # Tarifa por tiempo en minutos
    
    costo_total = tarifa_base + tarifa_por_tiempo * tiempo
    return costo_total
end

tiempo = rand(1..10)
puts tiempo

tiempo_inicial = Time.now

tiempo.times do
    puts "Viaje en proceso"
    sleep(1)  # Pausa durante 1 segundo
end

tiempo_final = Time.now

if tiempo > 0
    if tiempo <= 30
        costo = calcular_costo_viaje(0)
    else
        costo = calcular_costo_viaje(tiempo - 30)
    end

    puts "El costo del viaje es: $#{'%.2f' % costo}"
else
    puts "Error: Dato Invalido"
end


# codigo en perl

use strict;
use warnings;

print "Cada segundo simula un minuto de viaje\n";

sub calcular_costo_viaje {
    my ($tiempo) = @_;
    my $tarifa_base = 5000;  # Tarifa base en pesos
    my $tarifa_por_tiempo = 100;  # Tarifa por tiempo en minutos

    my $costo_total = $tarifa_base + $tarifa_por_tiempo * $tiempo;
    return $costo_total;
}

my $tiempo = int(rand(10)) + 1;
print "$tiempo\n";

my $tiempo_inicial = time;

for (my $i = 0; $i < $tiempo; $i++) {
    print "Viaje en proceso\n";
    sleep(1);  # Pausa durante 1 segundo
}

my $tiempo_final = time;

if ($tiempo > 0) {
    my $costo;
    if ($tiempo <= 30) {
        $costo = calcular_costo_viaje(0);
    } else {
        $costo = calcular_costo_viaje($tiempo - 30);
    }

    printf "El costo del viaje es: \$%.2f\n", $costo;
} else {
    print "Error: Dato Inválido\n";
}

# codigo en julia 

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