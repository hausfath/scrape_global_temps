import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import os

#Add your local path here for loading the csv
os.chdir('/Users/your_local_path_here')

#Name of CSV file containing the data (one column only)
temp_data = 'global_temps.csv'

savename = 'global_temps_line'

temps = np.genfromtxt(temp_data, delimiter=",")[1:]
temps_normed = ((temps - temps.min(0)) / temps.ptp(0)) * (len(temps) - 1)
elements = len(temps)

x_lbls = np.arange(elements)
y_vals = temps_normed / (len(temps) - 1)
y_vals2 = np.full(elements, 1)
bar_wd  = 1

my_cmap = plt.cm.RdBu_r #choose colormap to use for bars
norm = Normalize(vmin=0, vmax=elements - 1)

def colorval(num):
    return my_cmap(norm(num))

fig=plt.figure(figsize=(6,3))
plt.axis('off')
plt.axis('tight')

#Plot warming stripes. Change y_vals2 to y_vals to plot stripes under the line only.
plt.bar(x_lbls, y_vals2, color = list(map(colorval, temps_normed)), width=1.0)

#Plot temperature timeseries. Comment out to only plot stripes
plt.plot(x_lbls, y_vals - 0.002, color='black', linewidth=2)

plt.xticks( x_lbls + bar_wd, x_lbls)
plt.ylim(0, 1)
fig.subplots_adjust(bottom = 0)
fig.subplots_adjust(top = 1)
fig.subplots_adjust(right = 1.005)
fig.subplots_adjust(left = 0)
fig.savefig(savename+'.png', dpi=300)
