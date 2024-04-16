numeros_ingresados = []

# Mensaje inicial
print("Ingresa números y presiona '0' para finalizar.")

while True:  # Comenzamos un bucle infinito
    try:
        numero = int(input("Ingresa un número: "))  # Solicitamos al usuario que ingrese un número
        if numero > 0:
            numeros_ingresados.append(numero)  # Agregamos el número a la lista
        elif numero ==0:
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")  # Manejamos el error si no se ingresa un número

# Filtramos y mostramos solo los números positivos
numeros_positivos = [num for num in numeros_ingresados if num > 0]
print("suma de Números positivos ingresados:", sum(numeros_positivos))