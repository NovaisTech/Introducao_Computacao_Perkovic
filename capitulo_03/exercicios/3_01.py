#Problema Prático 3.1

# Implemente um programa que solicita a temperatura 
# atual em graus Fahrenheit do usuário e exibe a
# temperatura em graus Celsius usando a fórmula

# celsius = 5/9(fahrenheit - 32)

tempFahrenheit = eval(input("Digite a temperatura em Fahrenheit: "))

print(f"A temperatura de {tempFahrenheit} em Fahrenheit convertida pra Celsius é igual a:")
tempCelsius = (5 / 9 * (tempFahrenheit - 32))
print(f"{tempCelsius:.1f}°C")