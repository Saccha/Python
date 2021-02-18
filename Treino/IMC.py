peso = float(input("digite o peso: ")) 
altura = float(input("digite a altura: ")) 
imc = peso / altura ** 2

if (imc < 20): 
  imc = peso / altura ** 2 
  print("Abaixo do peso")

elif (imc <= 25): 
  imc = peso / altura ** 2 
  print("Normal")

else: 
  imc = peso / altura ** 2 
  print("Obesidade Mórbida")
