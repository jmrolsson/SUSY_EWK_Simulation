#!/usr/bin/env python

import os
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
          'figure.figsize': (8, 6),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'}
pylab.rcParams.update(params)

# read in mass points
file_name = 'mass_grid.txt'
massgrid = []
if os.path.exists(file_name):
    with open(file_name) as f:
        for line in f:
            if (re.search('^#',line) or line==''): continue
            high_mass = -1
            for i,mass in enumerate(line.split()):
                fmass = float(mass)
                if i==0:
                    high_mass = fmass
                else:
                    massgrid.append([high_mass, fmass])
elif IOError:
    print 'Unable to open file: '+str(file_name)
    exit()

massgrid = np.array(massgrid)
print massgrid
x = massgrid[:,0]
y = massgrid[:,1]

# print x
# print y
print 'Number of point: {}'.format(len(x))

fig = plt.figure()
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
plt.plot(x, y, 'o', markersize = 8, clip_on=False)
plt.xlim([0,800])
plt.ylim([0,600])
plt.xlabel(ur'$m_{\tilde{\chi}^0_2,\tilde{\chi}^\pm_2}\,{\rm [GeV]}$')
plt.ylabel(ur'$m_{\tilde{\chi}^0_1}\,{\rm [GeV]}$')
fig.savefig('mass_grid.pdf', bbox_inches='tight')
