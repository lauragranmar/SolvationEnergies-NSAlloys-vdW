__author__ = 'Laura'
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import os.path
from matplotlib import colors
matplotlib.rcParams.update({'errorbar.capsize':5})
matplotlib.rcParams['axes.linewidth'] = 2.5

# https://matplotlib.org/gallery/color/named_colors.html list of colors available when importing color maps



ohvac= 'GOH_vac_2ggas.txt'
oh_water='GOH_water_2ggas.txt'
gsol='solvation_energy_2groupsGGAs.txt'

ohvac_data = np.genfromtxt(ohvac, dtype=float, skip_header=1, usecols=(1, 2, 3, 4, 5),
                        names=['av1', 'av2','stdev1', 'stdev2','valence_electrons'])

ohwater_data = np.genfromtxt(oh_water, dtype=float, skip_header=1, usecols=(1, 2, 3, 4, 5),
                             names=['av1', 'av2','stdev1', 'stdev2','valence_electrons'])

solvation_energy = np.genfromtxt(gsol, dtype=float, skip_header=1, usecols=(1, 2, 3, 4, 5),
                                 names=['av1', 'av2','stdev1', 'stdev2','valence_electrons'])




#make a figure
fig = plt.figure(figsize=(7,7), linewidth=5)
ax1 = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.22)

label_ohvac1=r'$\Delta\mathsf{G}^{vac}_{OH}$-1'
label_ohvac2=r'$\Delta\mathsf{G}^{vac}_{OH}$-2'

label_ohwater1=r'$\Delta\mathsf{G}^{H_2O}_{OH}$-1'
label_ohwater2=r'$\Delta\mathsf{G}^{H_2O}_{OH}$-2'

label_gsol1\
    =r'$\Omega\mathsf{_{OH}}$-1'
label_gsol2=r'$\Omega\mathsf{_{OH}}$-2'

ax1.errorbar(ohvac_data['valence_electrons'], ohvac_data['av1'], ohvac_data['stdev1'], linestyle='None',
             marker='s', color='orange', markeredgewidth=1.5, markeredgecolor="k" , markersize= 8, label= label_ohvac1)

ax1.errorbar(ohvac_data['valence_electrons'], ohvac_data['av2'], ohvac_data['stdev2'], linestyle='None',
             marker='s', color='green', markeredgewidth=1.5, markeredgecolor="k" , markersize= 8, label= label_ohvac2)


ax1.errorbar(ohwater_data['valence_electrons'], ohwater_data['av1'], ohwater_data['stdev1'],linestyle='None',
             marker='^', color='orange', markeredgewidth=1.5, markeredgecolor="k", markersize= 8, label= label_ohwater1 )

ax1.errorbar(ohwater_data['valence_electrons'], ohwater_data['av2'], ohwater_data['stdev2'],linestyle='None',
             marker='^', color='green', markeredgewidth=1.5, markeredgecolor="k", markersize= 8, label= label_ohwater2 )


ax1.errorbar(solvation_energy['valence_electrons'], solvation_energy['av1'], solvation_energy['stdev1'], linestyle='None',
             marker='o', color='orange', markeredgewidth=1.5, markeredgecolor="k", markersize= 8, label= label_gsol1)

ax1.errorbar(solvation_energy['valence_electrons'], solvation_energy['av2'], solvation_energy['stdev2'], linestyle='None',
             marker='o', color='green', markeredgewidth=1.5, markeredgecolor="k", markersize= 8, label= label_gsol2)


ax1.tick_params(axis='both', which='major', direction= 'in', width= 1.5, size=8)
ax1.set_xlim(8.5, 11.5)
ax1.set_ylim(-0.8, 1.6, 0.5)
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



fig = plt.figure(num =1, frameon=True,facecolor="white", dpi= 300)
fig.text( 0.03,0.55,r'energy / eV',ha='center',va='center',rotation='vertical', size= 18)
fig.add_axes(linewidth=8.0)

fig.text( 0.5,0.14,r'valence electrons',ha='center',va='center', size=18 )
fig.text( 0.5, 0.975 ,r'subsurface element',ha='center',va='center', size=18)

plt.legend(loc='best', frameon=False)
ax1.legend(loc='upper center',frameon=False, bbox_to_anchor=(0.5, -0.15), ncol=3, columnspacing=5, fontsize=15, markerscale= 1)
#matplotlib.rc('legend', columnspacing=1, fontsize='large', markerscale=4)

#Annotations


bbox_args = dict(boxstyle="square", fc="w", edgecolor= 'white')

#ax1.annotate(r'$6H_2O_{\ (l)}$', xy=( 0.84, -0.71), color=color_O, size='large', weight='normal')

size_ann = 'large'
an1 = ax1.annotate(r'Co, Rh, Ir', xy=(9, 1.7), xycoords="data", annotation_clip=False,
                   va="center", ha="center", bbox= bbox_args, size=size_ann)

an2 = ax1.annotate(r'Ni, Pd, Pt', xy=(10.0, 1.7), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)

an3 = ax1.annotate(r'Cu, Ag, Au', xy=(11.0, 1.7), xycoords="data", annotation_clip=False,va="center", ha="center",
                  bbox= bbox_args, size=size_ann)

group1 = ax1.annotate(r'group 1', xy =(9.4, 1.2), xycoords="data", annotation_clip=False,
                      va="center", ha="center", bbox= bbox_args, size=15, color = 'orange')
group2 = ax1.annotate(r'group 2', xy =(9.4, 1.0), xycoords="data", annotation_clip=False,
                      va="center", ha="center", bbox= bbox_args, size=15, color= "green")


#an4 = ax1.annotate(r'$\Omega\mathsf{_{OH}}$',xy=(11.0, 0), xycoords="data", annotation_clip=False,va="center", ha="center",
                  #bbox= bbox_args)





"""title2=['energy_solvationvdW_3.7.2019']
fig.savefig(title2[0]+'2ggas.svg', format='svg', dpi=1200)
fig.savefig(title2[0]+'2ggas'+'.png', format='png', dpi=600)
"""
title2=['FreeEnergies-2GGAS']
fig.savefig(title2[0]+'2ggas'+'.png', format='png', dpi=600)

plt.show()



#TODO: increase size of legend



