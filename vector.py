a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
 
  
def kartezyen(a,b):
  matris=[]
  gecici=[]
  x=0
  for i in a:
    for j in b:
      for k in range(len(j)):
        gecici.append(i[x])
        gecici.append(j[k])
        matris.append(gecici)
        gecici=[]
      x=x+1
    x=0
  print(matris)

def carp(liste, sayi):
  vektor=[]
  gecici=[]
  for i in liste:
    for j in range(len(i)):
      gecici.append((i[j]*sayi))
    vektor.append(gecici)
    gecici=[]
  return vektor

def dis_carpim2(a,b):
  matris=[]
  gecici=[]
  for i in range(len(a)):
    for j in range(len(a[0])):
      gecici.append(carp(b,a[i][j]))
    matris.append(gecici)
    gecici = []
  print(matris)

def ic_carp(a,b):
  result=[]
  toplam=0
  # iterate through rows of X
  for i in range(len(a)):
    # iterate through columns of Y
      for j in range(len(b[0])):
        # iterate through rows of Y
        for k in range(len(b)):
            toplam += a[i][k] * b[k][j]
        result.append(toplam)
        toplam=0
            
ic_carp(a,b) 
dis_carpim2(a,b)
kartezyen(a,b)