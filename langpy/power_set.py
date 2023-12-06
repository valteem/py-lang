# https://simonhessner.de/calculate-power-set-set-of-all-subsets-in-python-without-recursion/

def get_subsets(fullset):
  listrep = list(fullset)

  subsets = []
  for i in range(2**len(listrep)):
    subset = []
    for k in range(len(listrep)):            
      if i & 1<<k:
        subset.append(listrep[k])
    subsets.append(subset)        

  return subsets

fullset = [1, 2, 3]
s = get_subsets(fullset)
print(s)