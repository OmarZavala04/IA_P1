import time

print("💣 ¡BOMBA ACTIVADA!")
print("Cuenta regresiva iniciada...\n")

for n in range(10, 0, -1):
    print("⏳", n)
    time.sleep(1)

print("\n💥 ¡BOOM!")
print("La bomba explotó.")