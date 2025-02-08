# Función para calcular el Índice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Funciónes de errores
def pedir_cadena(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            print("Error: Este campo no puede estar vacío. Inténtalo nuevamente.")

def pedir_numero(mensaje, tipo=float):
    while True:
        entrada = input(mensaje).strip()
        try:
            return tipo(entrada)
        except ValueError:
            print(f"Error: Por favor, introduce un número válido ({'entero' if tipo == int else 'decimal'}).")


# Programa para definir el IMC
print("--- Registro de datos personales ---")
nombre = pedir_cadena("Ingresa tu nombre: ")
apellido_paterno = pedir_cadena("Ingresa tu apellido paterno: ")
apellido_materno = pedir_cadena("Ingresa tu apellido materno: ")
edad = pedir_numero("Ingresa tu edad: ", int)
peso = pedir_numero("Ingresa tu peso en kilogramos (kg): ", float)
altura = pedir_numero("Ingresa tu altura en metros (m): ", float)

if peso <= 0 or altura <= 0:
    print("\nError: El peso y la altura deben ser valores mayores a cero.")
else:
    imc = calcular_imc(peso, altura)

    print("\n--- Datos Personales y Resultados ---")
    print(f"Nombre Completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso:.2f} kg")
    print(f"Altura: {altura:.2f} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")

    if imc < 18.5:
        print("Estado: Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Estado: Peso normal")
    elif 25 <= imc < 29.9:
        print("Estado: Sobrepeso")
    else:
        print("Estado: Obesidad")
