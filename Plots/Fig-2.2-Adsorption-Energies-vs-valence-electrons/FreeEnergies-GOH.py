
# %%
__author__ = 'Laura'
import matplotlib as mpl
#mpl.use('Agg') # silent mode
#mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import os.path
from matplotlib import colors
mpl.rcParams.update({'errorbar.capsize':100})
#mpl.rcParams.update({'figure.autolayout': True})
mpl.rcParams['xtick.labelsize'] = 200 #95
mpl.rcParams['ytick.labelsize'] = 200
mpl.rcParams['ytick.major.pad'] = 40
mpl.rcParams['xtick.major.pad'] = 40
mpl.rc('lines', markeredgewidth=10, markersize=200, lw=20)
mpl.rc('axes', linewidth=30)
mpl.rc('legend', fontsize=300)

# https://matplotlib.org/gallery/color/named_colors.html list of colors available when importing color maps



ohvac='GOH_vacuum.txt'
oh_water='GOH-H2O.txt'
gsol='solvation_energy'


ohvac_data = np.genfromtxt(ohvac, dtype=float, skip_header=1, usecols=(1, 2, 3),
                           names=['average', 'stdev', 'valence_electrons'])

ohwater_data = np.genfromtxt(oh_water, dtype=float, skip_header=1, usecols=(1, 2, 3),
                             names=['average', 'stdev', 'valence_electrons'])

solvation_energy = np.genfromtxt(gsol, dtype=float, skip_header=1, usecols=(1, 2, 3),
                                 names=['average', 'stdev', 'valence_electrons'])




#make a figure
fig = plt.figure(figsize=(100,100),frameon=False, dpi=10)
ax1 = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.20)

label_ohvac=r'$\Delta\mathsf{G}^{vac}_{OH}$'
label_ohwater=r'$\Delta\mathsf{G}^{H_2O}_{OH}$'
label_gsol=r'$\Omega\mathsf{_{OH}}$'

ax1.errorbar(ohvac_data['valence_electrons'], ohvac_data['average'], ohvac_data['stdev'], linestyle='None',
             marker='s', color='red',markeredgecolor="firebrick" , label= label_ohvac)

ax1.errorbar(ohwater_data['valence_electrons'], ohwater_data['average'], ohwater_data['stdev'],linestyle='None',
             marker='^', color='cyan', markeredgecolor="deepskyblue", label= label_ohwater )

ax1.errorbar(solvation_energy['valence_electrons'], solvation_energy['average'], solvation_energy['stdev'], linestyle='None',
             marker='o', color='springgreen', markeredgecolor="limegreen", label= label_gsol)


ax1.tick_params(axis='both', which='major', direction = 'in', width= 20, size= 60)
ax1.set_xlim(8.5, 11.5)
ax1.set_ylim(-0.8, 1.6, 0.1)
ax1.set_xticks([9,10,11], minor=False)






for tick in ax1.xaxis.get_ticklabels():
    #tick.set_fontsize('medium')
    tick.set_fontname('Arial')
    tick.set_color('black')
    tick.set_weight('bold')


for tick in ax1.yaxis.get_ticklabels():
    #tick.set_fontsize('medium')
    tick.set_fontname('Arial')
    tick.set_color('black')
    tick.set_weight('bold')



fig = plt.figure(num =1, frameon=False)
fig.text( 0.04,0.5,r'energy / eV',ha='center',va='center',rotation='vertical',size=300)
fig.add_axes(linewidth=8.0)

fig.text( 0.5,0.12,r'valence electrons',ha='center',va='center', size=300 )
fig.text( 0.5, 0.975,r'subsurface element',ha='center',va='center', size=300)

#plt.legend(loc='best', frameon=False, ncol=3)
ax1.legend(loc='upper center',frameon=False, bbox_to_anchor=(0.5, -0.1),ncol=3)

#Annotations


bbox_args = dict(boxstyle="square", fc="none", edgecolor= 'none')

#ax1.annotate(r'$6H_2O_{\ (l)}$', xy=( 0.84, -0.71), color=color_O, size='large', weight='normal')


an1 = ax1.annotate(r'Co, Rh, Ir', xy=(9, 1.7), xycoords="data", annotation_clip=False,
                   va="center", ha="center", bbox= bbox_args,size=300)

an2 = ax1.annotate(r'Ni, Pd, Pt', xy=(10.0, 1.7), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=300)

an3 = ax1.annotate(r'Cu, Ag, Au', xy=(11.0, 1.7), xycoords="data", annotation_clip=False,va="center",   ha="center", bbox= bbox_args, size=300)

#an4 = ax1.annotate(r'$\Omega\mathsf{_{OH}}$',xy=(11.0, 0), xycoords="data", annotation_clip=False,va="center", ha="center",
                  #bbox= bbox_args)





#plt.savefig('NEWSolvation_vdWFig.png', dpi =10, format='png', transparent=True, style='presentation')



#plt.savefig('Fig2.2-Solvation_vdWFig.png', dpi =10, format='png', transparent=True, #style='presentation')


plt.draw() #remove for interactive run
plt.show()



