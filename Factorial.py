def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número entero positivo: "))

# Verificar que el número sea positivo
if numero < 0:
    print("El número debe ser entero y positivo.")
else:
    # Calcular el factorial
    resultado = factorial(numero)
    # Mostrar el resultado
    print(f"El factorial de {numero} es {resultado}.")
