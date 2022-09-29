sityva = input("Sityva ? : ")
sia = dict()

for aso in sityva:
    if aso in sia:
        sia[aso] += 1
    else:
        sia[aso] = 1
print(sia)

