###
# 03 - casting de types
# Transformer un type de valeur en un autre type
###

print("Conversion d'une string")
print(type("100"))

# Python ne réalise pas une transormation de type de données automatiquement : typage très fort
# On doit nous-même spécifier que l'on veut le transformer

# print("100" + 2) # ceci donne une erreur : TypeError

print(int("100") + 2)
print("100" + str(2))

print(type(float("3.1416")))
print(int(3.1416))

print(bool(3)) ## True
print(bool(0)) ## False
print(bool(-1)) ## True

print((bool(""))) ## False

# print(int("Hola mundo")) ## ValueError
