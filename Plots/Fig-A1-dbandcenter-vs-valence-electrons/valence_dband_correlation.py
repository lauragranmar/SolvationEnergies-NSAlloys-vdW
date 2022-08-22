__author__ = 'Laura'
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import os.path
from matplotlib import colors
matplotlib.rcParams['axes.linewidth'] = 2.5

dband_outerelectrons_data='dband_outerelectrons_data.txt'
dband_lineatoms='dband_lineatoms_data.txt'

data = np.genfromtxt(dband_outerelectrons_data, dtype=float, skip_header=1, usecols=(1,2),
                        names=['ve','dbc_wrt_Pt'])

data2= np.genfromtxt(dband_lineatoms, dtype=float, skip_header=1, usecols=(0, 2, 4, 6),
                        names=['ve','3d','4d','5d'])
#make a figure
fig = plt.figure(figsize=(8,8), linewidth=5)
ax1 = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.19, left=0.14, right=0.99, top=0.99)

#legned_labels
label_3d=r'3d'
label_4d=r'4d'
label_5d=r'5d'

#ax1.plot(data['ve'], data['dbc_wrt_Pt'], linestyle='None',
             #marker='s', color='red', markeredgewidth=1.5, markeredgecolor="firebrick", markersize= 8, )
ax1.plot(data2['ve'],data2['3d'], linestyle='None', marker='s', markersize= 12, markeredgecolor="black", markeredgewidth=1.5, label= label_3d)
ax1.plot(data2['ve'],data2['4d'], linestyle='None', marker='s', markersize= 12, markeredgecolor="black", markeredgewidth=1.5, label= label_4d)
ax1.plot(data2['ve'],data2['5d'], linestyle='None', marker='s', markersize= 12, markeredgecolor="black", markeredgewidth=1.5, label= label_5d)
ax1.legend(loc='best',frameon=False, ncol=3, columnspacing=5, fontsize=15, markerscale= 0.8)


ax1.tick_params(axis='both', which='major', direction= 'in', width= 1.5, size=8)
ax1.set_xlim(8.5, 11.5)
ax1.set_ylim(-0.45, 0.4)
ax1.set_xticks([9,10,11], minor=False)




for tick in ax1.xaxis.get_ticklabels():
    tick.set_fontsize(15)
    tick.set_fontname('Arial')
    tick.set_color('black')
    tick.set_weight('bold')


for tick in ax1.yaxis.get_ticklabels():
    tick.set_fontsize(15)
    tick.set_fontname('Arial')
    tick.set_color('black')
    tick.set_weight('bold')



fig = plt.figure(num =1, frameon=True,facecolor="white", dpi= 600)
fig.text( 0.03,0.6,r'$\mathit{d}$-band center wrt Pt-Pt / eV',ha='center',va='center',rotation='vertical', size= 18)
fig.add_axes(linewidth=8.0)
fig.text( 0.55,0.12,r'valence electrons',ha='center',va='center', size=18 )

#fig.text( 0.5, 0.975 ,r'subsurface element',ha='center',va='center', size=18)


ax1.legend(loc='upper center',frameon=False, bbox_to_anchor=(0.5, -0.15), ncol=3, columnspacing=5, fontsize=15, markerscale= 0.9)
#matplotlib.rc('legend', columnspacing=1, fontsize='large', markerscale=4)




#Annotations for the metals.


bbox_args = dict(boxstyle="square", fc="w", edgecolor= 'white')

#ax1.annotate(r'$6H_2O_{\ (l)}$', xy=( 0.84, -0.71), color=color_O, size='large', weight='normal')

size_ann = 18
color_3d ='blue'
color_4d = 'orange'
color_5d = 'green'
Rh = ax1.annotate(r'Rh', xy=(9.15, -0.2), xycoords="data", annotation_clip=False,
                   va="center", ha="center", bbox= bbox_args, size=size_ann)

Co = ax1.annotate(r'Co', xy=(9.15, -0.3), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)

Ir = ax1.annotate(r'Ir', xy=(9.15, -0.4), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)

Pd = ax1.annotate(r'Pd',xy=(10.15, 0.18), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)

Pt = ax1.annotate(r'Pt',xy=(10.15, 0.0), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)
Ni = ax1.annotate(r'Ni',xy=(10.15, -0.17), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)
Ag = ax1.annotate(r'Ag',xy=(11.15, 0.32), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)
Au = ax1.annotate(r'Au',xy=(11.15, 0.24), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)

Cu = ax1.annotate(r'Cu',xy=(11.15, 0.12), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)


"""
title2=['dbc_valenceElectrons_3.7.2019']
fig.savefig(title2[0]+'.svg', format='svg', dpi=1200)
fig.savefig(title2[0]+'2'+'.png', format='png', dpi=600)
"""
title2=['FigA1-dbandcenter-vs-valenceElectrons']
fig.savefig(title2[0]+'2'+'.png', format='png', dpi=600)

plt.draw()
plt.show()

