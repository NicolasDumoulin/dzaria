 
def buildMatrix(size):
  return [[i*size+j for j in range(size)] for i in range(size)]

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

def computeTransitions():
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
    print(buff)

import numpy as np
def destinations(position=2,maxDepth=2,size=4) :
  """
  Returns an array of destinations represented by an array containing the position of the
  destination and the path to reach it
  """
  depth=0
  destinations = []
  starts = [[position,[]]]
  while depth<maxDepth:
    nextStarts=[]
    for pos,path in starts:
      path+=[pos]
      shift=[]
      if pos>=size:
        shift.append(-size)
      if pos%size>0:
        shift.append(-1)
      if pos%size<size-1:
        shift.append(1)
      if pos<size*(size-1):
        shift.append(size)
      neighbours=pos+np.array(shift)
      for dest in neighbours:
        # avoiding moves that reach the start
        if dest!=position:
          # avoiding to return on previous position
          if len(path)<2 or dest!=path[-2]:
            # avoiding long moves that reaches a direct neighbour: these moves are useless
            if len(path)<3 or abs(path[-3]-dest) not in [1,4]:
              destinations.append([dest,path[:]])
              nextStarts.append([dest,path[:]])
    starts = nextStarts
    depth += 1
  return destinations
    
