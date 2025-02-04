###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
# print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")
print("Julien", "Perpignan", sep="\n")

### Completa aquí

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
# print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
print(type(a))
b = 3.14159
print(type(b))
c = "Hola mundo"
print(type(c))
d = True
print(type(d))
e = None
print(type(e))

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

print(int("123456"))

### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
# print("Crea variables para tu nombre, edad y altura.")
# print("Usa f-strings para imprimir una presentación.")

nom = "Julien"
age = 31
taille = 1.86

print(f"Salut, je m'appelle {nom}, j'ai {age} et je mesure {taille}m.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
pi = 3.14
print("2. Redondea el número con round()")
rounded_pi = print(round(pi))
print("3. Haz la división entera entre el número que te salió y el número 2")
print(rounded_pi / pi)
print("4. El resultado debería ser 1")
