minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
simbolos=["@","#","$","&"]
numeros=["0","1","2","3","4","5","6","7","8","9"]
maiusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

while True:
  i=0
  qtmaiusculas=0
  qtnumeros=0
  qtsimbolos=0
  repnumeros=False
  repsimbolos=False
  senha=input("Digite sua senha entre 10 e 15 caracteres, sem acentos ou espaços, no minimo 1 letra maiuscula, entre 1 e 3 numeros e no minimo 1 caractere especial sendo eles @#$&")
  while i<len(senha):
    if(len(senha)<10):
      print("Senha muito curta")
      break
    elif (len(senha)>15):
      print("Senha muito longa")
      break
    elif senha[i] not in minusculas and senha[i] not in maiusculas and senha[i] not in numeros and senha[i] not in simbolos:
      print(f"Senha contem caractere inválido {senha[i]}")
      break
    elif senha[i] in maiusculas:
      qtmaiusculas+=1
    elif senha[i] in numeros:
      if qtnumeros==0:
        xn=senha[i]
      if qtnumeros>0 and senha[i]==xn:
        repnumeros=True
      qtnumeros+=1
    elif senha[i] in simbolos:
      if qtsimbolos==0:
        yn=senha[i]
      if qtsimbolos>0 and senha[i]==yn:
        repsimbolos=True
      qtsimbolos+=1
    i+=1
  if qtmaiusculas>0 and qtnumeros<4 and qtnumeros>0 and qtsimbolos>0:
    print("Sua senha foi aceita.")
    break
  else:
    print("Senha invalida")

if len(senha)<15 and qtmaiusculas==1 and qtnumeros==2 and qtsimbolos==1:
  print("O nivel da sua senha é fraca")
elif len(senha)==15 and qtmaiusculas==3 and qtnumeros==3 and qtsimbolos==3 and repnumeros==False and repsimbolos==False:
  print("O nivel da sua senha é forte")
else:
  print("O nivel da sua senha é media")