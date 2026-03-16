print("╔══════════════════════════════════╗")
print("  VERIFICADOR DE DURACIÓN DEL AÑO")
print("╚══════════════════════════════════╝")

anio = int(input("\nIntroduce un año: "))

if anio < 1582:
    print("Este año no pertenece al calendario Gregoriano.")
else:
    if anio % 4 != 0:
        print("El año tiene 365 días.")
    elif anio % 100 != 0:
        print("El año tiene 366 días.")
    elif anio % 400 != 0:
        print("El año tiene 365 días.")
    else:
        print("El año tiene 366 días.")

print("\nConsulta terminada.")