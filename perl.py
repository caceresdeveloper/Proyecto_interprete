import subprocess

# Código Perl que deseas ejecutar (puedes guardar tu código Perl en un archivo o usar una cadena)
codigo_perl = """
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
"""

# Guarda el código Perl en un archivo temporal (opcional)
with open("codigo_perl.pl", "w") as archivo_perl:
    archivo_perl.write(codigo_perl)

# Ejecuta el código Perl utilizando el comando "perl" en la línea de comandos
proceso = subprocess.Popen(["perl", "-e", codigo_perl], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
salida, errores = proceso.communicate()

# Imprime la salida y los errores (si los hay)
print("Salida:")
print(salida)

print("Errores:")
print(errores)




