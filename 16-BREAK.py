print("""
+==================================+
|        PORTAL MISTERIOSO         |
|   Solo una palabra puede abrirlo |
+==================================+
""")

while True:
    palabra = input("Di la palabra secreta: ")
    
    if palabra.lower() == "sesamo":
        print("✨ El portal se abre lentamente...")
        print("Has escapado con éxito.")
        break
    else:
        print("🔒 El portal sigue cerrado. Intenta otra vez.")