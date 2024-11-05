def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Pedir al usuario que ingrese la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en Celsius: "))

# Convertir la temperatura a Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

# Mostrar el resultado
#la "f" sirve para insertar valores en donde haya llaves ({})
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
