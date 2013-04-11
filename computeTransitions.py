 
def buildMatrix(size):
  matrix = []
  for i in range(size):
    row = []
    for j in range(size):
      row.append(i*size+j)
    matrix.append(row)
  return matrix

def ijFromIndex(size, index):
  return [index/size,index%size]

def distance(iStart,jStart,iEnd,jEnd):
  return abs(iEnd-iStart)+abs(jEnd-jStart)

def destinations(size,iStart,jStart,length,exact=True):
  destinations=[]
  for i in range(size):
    for j in range(size):
      if exact:
	if distance(iStart,jStart,i,j)==length:
	  destinations.append([i,j])
      elif distance(iStart,jStart,i,j)<=length:
	  destinations.append([i,j])
  return destinations

def destinationsIndexes(size,iStart,jStart,length,exact=True):
  data=[]
  matrix=buildMatrix(size)
  for d in destinations(size,iStart,jStart,length,exact):
    data.append(matrix[d[0]][d[1]])
  return data

size = 4
matrix = buildMatrix(size)
for i in range(size*size):
  buff = "{"
  for j in range(1,7):
    ij = ijFromIndex(size,i)
    end = ""
    if not j==6: end=", "
    buff += str(j)+":"+str(destinationsIndexes(size,ij[0],ij[1],j,True))+end
  buff += "}"
  if not i == size*size-1:
    buff += ','
  print buff
