import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")

  temp = np.reshape(list, (3,3))
  temp.mean(axis = 0)
  
  calculations = {
    'mean': [
      temp.mean(axis=0).tolist(),
      temp.mean(axis=1).tolist(),
      temp.flatten().mean()
    ],
    'variance' : [
      temp.var(axis=0).tolist(),
      temp.var(axis=1).tolist(),
      temp.flatten().var()
    ],
    'standard deviation' : [
      temp.std(axis=0).tolist(),
      temp.std(axis=1).tolist(),
      temp.flatten().std()
    ],
    'max' : [
      temp.max(axis=0).tolist(),
      temp.max(axis=1).tolist(),
      temp.flatten().max()
    ],
    'min' : [
      temp.min(axis=0).tolist(),
      temp.min(axis=1).tolist(),
      temp.flatten().min()
    ],
    'sum' : [
      temp.sum(axis=0).tolist(),
      temp.sum(axis=1).tolist(),
      temp.flatten().sum()
    ]
  }
  return calculations