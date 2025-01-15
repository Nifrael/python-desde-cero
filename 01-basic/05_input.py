###
# 05 - Entrées des utilisateurs - Version simplifiée
# La fonction input() permet d'obtenir des données de l'utilisateur à travers de la console.
###

# print("Salut, comment tu t'appelles ?")
# nom = input()

# print(f"Hola {nom}, enchanté!")

nom = input("Hola, comment tu t'appelles ?\n")
print(f"Hola {nom}, enchanté!")

age = input("Quel âge as-tu?\n")
age = int(age)
print(f"Tu as {age} ans!")

print("Obtenir des valeurs multiples en même temps")
country, city = input("Dans quel pays et ville es-tu né?\n").split()

print(f"Tu vis en {country}, à {city}")
