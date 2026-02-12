import numpy as np
 >>> import matplotlib.pyplot as plt
 >>> data = np.random.randn(1000)
 >>> values, base = np.histogram(data, bins=40)
 >>> cumulative = np.cumsum(values)
 >>> plt.plot(base[:-1], cumulative, c='blue')
 >>> plt.show(
     