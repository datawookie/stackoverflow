import numpy as np
from foo import foo

a = np.array([[1,2,3,4], [5,6,7,8]], order='F')
print(foo(a))
