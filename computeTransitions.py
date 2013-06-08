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

if __name__=='__main__':
  print(str([destinations(position,maxDepth=6,size=4) for position in range(16)]))
    
