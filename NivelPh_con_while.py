print("-" * 30)
ph_level = int(input("Ingrese el nivel de ph: "))

def nivelph(ph_level):
    while ph_level > 14 or ph_level < 0:
        print("Ese dato no es valido, Ingrese de nuevo la cantidad correcta")
        print("-" * 30)
        ph_level = int(input("Digite de nuevo el nivel de pH: "))
    if ph_level < 7 and ph_level >= 0:
        return "Es un ácido"
    elif ph_level == 7:
        return "Es un ácido neutro"
    elif ph_level > 7 or ph_level <= 14:
        return "Es un ácido base"
print(nivelph(ph_level))