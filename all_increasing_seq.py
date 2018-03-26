def list()

D = [10, 9, 2, 5, 3]
L = [[] for in range(len(D))] # created a list of lists of length d L = [[],[],[],[],[]]

for i in range(len(D)):
  for j in range(0,i):
    if D[i] > D[j]:
      L[i] = list(L[j])
    L[i].append(D[i])
