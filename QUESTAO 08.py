variavel = "1234567890"
cres,desc=True,False
i = 0
while i!=-1:
  j=0
  print("")
  while j<=i: 
    if j<=len(variavel):
      print(variavel[j],end="")
      j+=1
  if cres==True:
    i+=1
    if i==len(variavel):
      cres,desc=False,True
      i-=1
  if desc==True:
    i-=1