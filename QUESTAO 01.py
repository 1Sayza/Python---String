i=0
vogais=["a","e","i","o","u","ã","õ","á","é","í","ó","ú","à","è","ì","ò","ù","â","ê","î","ô","û"]
Qtvogais=0
palavra=input("Digite uma palavra: ")
while True:
    j = 0
    while j != len(vogais):
      if palavra[i]==vogais[j]:
        Qtvogais+=1
        print(palavra[i])
      j+=1
    i+=1
    if i == len(palavra):
      break