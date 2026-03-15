juan = 3
maria = 5
adrian = 6

print("Manzanas recolectadas por cada persona:")
print("Juan:", juan, "Maria:", maria, "Adrian:", adrian, sep=' ')

print("\nLista simple de cantidades:")
print(juan, maria, adrian, sep=', ')

# total
manzanas_total = juan + maria + adrian

# promedio
promedio = manzanas_total / 3

# quien tiene mas
mayor = max(juan, maria, adrian)

print("\nTotal de manzanas:", manzanas_total)
print("Promedio de manzanas:", promedio)
print("La mayor cantidad de manzanas es:", mayor)

print("\nResumen final ->", end=" ")
print("Juan:", juan, "| Maria:", maria, "| Adrian:", adrian)