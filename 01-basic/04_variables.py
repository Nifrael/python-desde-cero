###
# 04 - Variables
# Transformer un type de valeur en un autre type
###

# Assigner une variable

my_name = "Julien"
print(my_name)

age = 31
print(age)

age = 39
print(age)

# Le type de données se détermine pendant le temps d'éxécution
# Pas de besoin de les déclarer explicitement

name = "Julien"
print(type(name))

name = 31
print(type(name))

## Typage très fort : pas de conversion automatique des types de données

#print(10 + "2") donnera une erreur

# f-string
print(f"Hola {my_name}, tengo {age} años")

# Convention de nommage de variables
# nommage_de_variable = "ok" #snake_case
# nommage = "ok"
# MonNommageDeVariable = "ko"
# monnommagedevariable = "ko"
# nommage_de_variable_123 = "ok"

# # UPPER_CASE : par convention, ne pas réassigner cette variable
# Contrairement à d'autres langages, on peut quand réassigner une valeur à cette constante.

is_user_logged_in: bool = True ## Annotation de type
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)
