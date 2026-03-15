print("╔════════════════════════════════╗")
print("   CALCULADORA DE FIN DE EVENTO")
print("╚════════════════════════════════╝")

print("\nIngrese la hora en formato de 24 horas\n")

horas = int(input("Hora de inicio (0-23): "))
minutos = int(input("Minuto de inicio (0-59): "))
evento = int(input("Duración del evento (minutos): "))

# cálculo del tiempo final
minutos = minutos + evento
horas = horas + minutos // 60
minutos = minutos % 60
horas = horas % 24

print("\nEl evento termina a las:")
print(horas, ":", minutos, sep='')

print("\n¡Gracias por usar el programa!")