print("╔══════════════════════════════════╗")
print("     CALCULADORA DE COMISIONES")
print("╚══════════════════════════════════╝")

ventas = float(input("\nIntroduce el total de ventas del año: "))

if ventas < 85528:
    comision = ventas * 0.18 - 556.02
else:
    comision = (ventas - 85528) * 0.32 + 14839.02

if comision < 0:
    comision = 0

comision = round(comision, 0)

print("\n------------------------------")
print("Ventas totales:", ventas, "MXN")
print("Comisión ganada:", comision, "pesos")
print("------------------------------")
print("¡Buen trabajo en tus ventas!")