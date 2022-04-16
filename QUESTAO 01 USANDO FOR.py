palavra = []
palavras = input("Digite um nome: ")
palavra.append(palavras)
for i in palavra:
  print(f'\nNa palavra {i.upper()} temos vogais ', end = "")
  for letra in i:
    if letra.lower() in "aeiouáàâãéêíóôõuú":
      print(letra, end = "")