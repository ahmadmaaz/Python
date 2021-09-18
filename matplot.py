import matplotlib.pyplot as plt
import numpy as np

y=np.random.uniform(0.0,10.0,500)
x=np.array([0,"PERCENTAGE"])
plt.hist(y,10,color='red')
plt.title('Random array')
plt.show()