def quadrante(x,y):
  if x>0 and y>0:
    return "no primeiro quadrante"
  elif x<0 and y>0:
    return "no segundo quadrante"
  elif x<0 and y<0:
    return "no terceiro quadrante"
  elif x>0 and y<0:
    return "no quarto quadrante"
  elif x==0 and y>0:
    return "entre o primeiro e segundo quadrante"
  elif x==0 and y<0:
    return "entre o terceiro e quarto quadrante"
  elif x>0 and y==0:
    return "entre o primeiro e quarto quadrante"
  elif x<0 and y==0:
    return "entre o segundo e terceiro quadrante"
  elif x==0 and y==0:
    return "na origem"

xi=int(input("Digite a coordenada X inicial do robô: "))
yi=int(input("Digite a coordenada Y inicial do robô: "))
xf,yf=xi,yi
comando=input("Digite uma combinação de movimentos para o robô Executar: Movimentos Validos U D R L O N E W: ")
comando=comando.lower()
validos=["u","d","r","l","o","n","e","w"]
i=0
movinvalidos=0
tamanhocomando=len(comando)
while True:
  if i==len(comando)-1:
    break
  if comando[i] not in validos:
   
    comando = comando.replace(comando[i], '')
    movinvalidos+=1
    i=0
  else:
    i+=1

i=0
while i<len(comando):
  if comando[i]=="u":
    yf+=1
  elif comando[i]=="d":
    yf-=1
  elif comando[i]=="r":
    xf+=1
  elif comando[i]=="l":
    xf-=1
  elif comando[i]=="o":
    xf-=1
    yf+=1
  elif comando[i]=="n":
    xf+=1
    yf+=1
  elif comando[i]=="e":
    xf+=1
    yf-=1
  elif comando[i]=="w":
    xf-=1
    yf-=1
  i+=1
print(f"A posição inicial do robô era X={xi} Y={yi}")
print(f"A posição final do robô é X={xf} Y={yf}")
print(f"O robô executou {len(comando)} comandos válidos, nos quais foram {comando}")
print(f"O robô tinha sua coordenada inicial {quadrante(xi,yi)}")
print(f"O robô tem a coordenada final {quadrante(xf,yf)}")