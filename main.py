n=8
T=[[0 for i in range(n+1)] for j in range(n+1)]
T[1][3],T[3][1]=1,1
T[1][2],T[2][1]=1,1
T[2][4],T[4][2]=1,1
T[4][3],T[3][4]=1,1
T[2][5],T[5][2]=1,1
T[7][5],T[5][7]=1,1
T[7][8],T[8][7]=1,1
T[6][8],T[8][6]=1,1
T[5][6],T[6][5]=1,1

parents=[-1]*(n+1)
visited=[0]*(n+1)
# parents=[-1, -2, 1, -1, 2, -1, -1, -1, -1]

def findParent(node):
  val=1
  while(1):
    val=parents[node]
    if(val>0):
      node=val
    else:
      break
  return [node,val]
# print(findParent(4))

def makeUnion(u,v,parents):
  parent1,weight1=findParent(u)
  parent2,weight2=findParent(v)
  # print( parent1,weight1,'---',parent2,weight2)
  if(parent1==parent2):
    print("Cycle found",u,v)
  else:
    if(weight1<=weight2):
      parents[parent2]=parent1
      parents[parent1]+=weight2
      for el in range(len(parents)):
        if parents[el]==parent2:
          parents[el]=parent1
      # print('u1',u,'v1',v,parents)
    else:
      parents[parent1]=parent2
      parents[parent2]+=weight1
      for el in range(len(parents)):
        if parents[el]==parent1:
          parents[el]=parent2
      # print('u',u,'v',v,parents)


def selectEdge(visited,parents):
  for row in range(1,n+1):
    for nei in range(1,n+1):
      if(not visited[nei] and T[row][nei]):
        makeUnion(row,nei,parents)
    
    visited[row]=1

selectEdge(visited,parents)
print(parents)




