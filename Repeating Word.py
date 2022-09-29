sityva = input("Asobgera Meordeba? : ")
ramdeni = ''
for aso in sityva:
    if aso == ' ':
        ramdeni += aso
print("Ki, Meordeba" if any(sityva.count(aso) > 1 for aso in sityva) else "Ara, Ar Meordeba")
