### Phrases ocnditionnelles
# if elsif else
###

import os
os.system("clear")

print('\n Mon message conditionnel')

age = 18

if age >= 18:
    print('Tu es majeur')
    print("Félicitations!")

age = 15

if age >= 18:
    print('Tu es majeur')
    print("Félicitations!")

print('\n Mon message else')

age = 15

if age >= 18:
    print('Tu es majeur')
else:
    print("Tu es mineur!")

print('\n Mon message elif')

note = 7

if note >= 9: # Si la note est 9 ou plus, le code s'arrête à la première condition remplie et ne jouera pas la condition note >= 7
    print('Fantastique!')
elif note >= 7:
    print('Pas mal!')
else:
    print("Nul!")

print('\n Conditions multiples')
age = 16
permis = True

if age >= 18 and permis:
    print("Tu peux conduire")
else:
    print("APPELEZ LA POLICE!!!")

## Un village de l'île Marguerite

if age >= 18 or permis:
    print("Tu peux conduire sur l'île")
else:
    print("Paie la police et elle te laissera conduire")

## if not comme le ! en JS

c_le_weekend = False
if not c_le_weekend:
    print("Et non, pas encore...")


print('\n Nester des conditions')
age = 20
avoir_argent = True

if age >= 18:
    if avoir_argent:
        print("Tu peux aller en discothèque")
    else:
        print("Tu restes à la maison.")
else:
    print("Tu ne peux pas entrer à la discothèque")


# Refacto (à prendre du cours)
