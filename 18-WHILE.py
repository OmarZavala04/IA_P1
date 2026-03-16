print("=== CONSTRUCTOR DE PIRÁMIDES ===")

bloques = int(input("Número de bloques disponibles: "))

h = 0
bloques_nec = 1

while bloques >= bloques_nec:
    bloques = bloques - bloques_nec
    h = h + 1
    bloques_nec = bloques_nec + 1

print("\nResultados:")
print("Altura máxima de la pirámide:", h)
print("Bloques que sobraron:", bloques)