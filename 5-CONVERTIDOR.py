kilometros = 12.25
millas = 7.38

print("=== CONVERSOR DE DISTANCIAS ===\n")

# conversiones
millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

# resultados principales
print(millas, "millas son equivalentes a", round(millas_a_kilometros, 2), "kilómetros")
print(kilometros, "kilómetros son equivalentes a", round(kilometros_a_millas, 2), "millas")

print("\n--- RESUMEN ---")

# diferencia entre valores convertidos
diferencia = abs(millas_a_kilometros - kilometros)

print("Kilómetros originales:", kilometros)
print("Millas originales:", millas)
print("Diferencia entre kilómetros originales y convertidos:", round(diferencia, 2))

print("\n--- TABLA SIMPLE ---")
print("Tipo", "Valor", "Equivalente", sep=" | ")

print("Millas", millas, round(millas_a_kilometros, 2), sep=" | ")
print("Kilómetros", kilometros, round(kilometros_a_millas, 2), sep=" | ")