from funciones import multiplicar

# 1) Solicita dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# 2) Multiplica usando la función encapsulada e imprime el resultado
resultado = multiplicar(num1, num2)
print("El resultado de la multiplicación es:", resultado)
