cpf = input("Digite o CPF: ")
while int(cpf)<10000000000 or int(cpf)>99999999999:
  print("digite um cpf com 11 digitos")
  cpf = int(input("Digite o CPF: "))
i,j,v1,v2=0,11,0,0
while i<len(cpf)-1:
  if i<len(cpf)-2:
      v1+=int(cpf[i])*(j-1)
  v2+=int(cpf[i])*j
  j-=1
  i+=1
v1,v2=(v1*10)%11,(v2*10)%11
if v1==10:
  v1=0
if v2==10:
  v2=0
if v1==int(cpf[9]) and v2==int(cpf[10]):
  print(f"Digito verificador é {v1}{v2}, o CPF é válido")
else:
  print("CPF inválido")