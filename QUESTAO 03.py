sequencia = input("Digite uma palavra ou sequência de número: ").upper()
i = 0
j = 0
while i < len(sequencia):
  if sequencia[i] != sequencia[len(sequencia)-i-1]:
    j +=1
  i+=1
if j == 0:
  print("É um palíndromo!")   
else:
  print("Não é um palíndromo!")