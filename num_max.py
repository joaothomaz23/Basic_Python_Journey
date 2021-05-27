print("Este programa lê três numeros e dia qual deles é o maior: ")

num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))
num3 = int(input("Entre com o terceiro numero: "))

num_max = max(num1, num2, num3)
num_min = min(num1, num2, num3)
print("O maior numero e: ",num_max)
print("O menor numero e: ",num_min)
