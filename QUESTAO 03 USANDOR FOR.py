sequencia = str(input("Digite uma palavra ou sequência de número: ")).upper()
j = " "
for i in range(len(sequencia) -1, -1, -1):
  j += sequencia[i]
if j == sequencia:
    print("Temos um palíndromo!")
else:
    print("Não é um palíndromo!")