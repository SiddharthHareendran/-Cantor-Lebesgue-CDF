import numpy as np
import matplotlib.pyplot as plt
def cantor(x,left_bound=0,right_bound=1,level=1,v_offset=0):
    division = (right_bound-left_bound)/3
    if level>50: return 1/2**level + v_offset
    if x < left_bound + division:
        return cantor(x,left_bound,left_bound+division,level+1,v_offset)
    elif x < left_bound + 2*division:
        return 1/2**level + v_offset
    else:
        return cantor(x,left_bound+2*division,right_bound,level+1,
                     1/2**level + v_offset)

x = np.linspace(0,1,1000)
y = x.copy()
for i in range(len(y)):
    y[i] = cantor(y[i])
plt.plot(x,y)
plt.show()
1/2**100
