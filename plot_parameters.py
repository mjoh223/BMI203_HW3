import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set
import matplotlib.pyplot as plt
%matplotlib inline
import csv

with open("heatmap.txt") as tsvfile:
    reader = csv.reader(tsvfile, delimiter = ' ')
    t = list(reader)
t = list(map(int, t))

result = [ [list( map(float, i) ) for i in t] ]

cmap = sns.palplot(sns.color_palette("BuGn_r"))
ax = sns.heatmap(result[0],vmin=0.3, vmax=.45, center=.30,square=1, xticklabels=range(1,6), yticklabels=range(1,21),
cmap="BuGn_r")

fig = ax.get_figure()
fig.savefig("parameter_heatmap.png", dpi=300)
