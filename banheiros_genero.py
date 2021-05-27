print("Você esta diante de um banheiro!!")
aux = 0

while aux == 0:
 genero = str(input("Qual e o seu genero? F para Feminino ou M para Masculino: "))
if genero == "F":
 print("Entre no banheiro da Esquerda!")
 aux = 1
elif genero == "M":
 print("Entre no banheiro da Direita!")
 aux = 1
else:
 aux = 0 
