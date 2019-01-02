import numpy as np

A = np.array(list(map(float, input().split())))

print(str(np.floor(A)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'),
      str(np.ceil(A)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'),
      str(np.rint(A)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'),
      sep = "\n")
