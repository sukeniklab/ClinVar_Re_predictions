# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:38:18 2024

@author: ssukenik
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from mpl_toolkits.axes_grid1 import Divider, Size

mpl.rcParams['axes.linewidth'] = 3
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 3
mpl.rcParams['xtick.major.width'] = 3
mpl.rcParams['font.size'] = 20

#%%
compact = pd.read_csv('gProfiler_hsapiens_11-7-2024_compact.csv',
                      comment='#',)
for source in ['GO:MF']:#,'GO:CC']:
    sliced = compact[(compact['source']==source)&(compact['term_size']>100)&(compact['FC']>1.1)&(compact['term_name'].str.len()<35)]
    fig = plt.figure(figsize=[5,5])
    h = [Size.Fixed(0), Size.Fixed(2)]
    v = [Size.Fixed(0), Size.Fixed(len(sliced)*.4)]
    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
    ax = fig.add_axes(divider.get_position(),axes_locator=divider.new_locator(nx=1, ny=1))
    ax.hlines(np.arange(len(sliced)),np.zeros(len(sliced)),np.ones(len(sliced))*4.5,
              color='k',linestyle='--',zorder=0)
    g = sns.scatterplot(x='FC',y='term_name',data=sliced,hue='negative_log10_of_adjusted_p_value',
               size='term_size',sizes=(150,800),palette='Reds',
               legend='brief',edgecolor='k',
               hue_norm=(3,11),ax=ax)
    g.legend(bbox_to_anchor=(1.2,1))
    ax.set_xlim(1,2)
    plt.savefig('GO_MF.svg')
#%% 
for source in ['GO:BP']:
    sliced = compact[(compact['source']==source)&(compact['term_size']>500)&(compact['FC']>1.4)&(compact['term_name'].str.len()<35)]
    fig = plt.figure(figsize=[5,5])
    h = [Size.Fixed(0), Size.Fixed(2)]
    v = [Size.Fixed(0), Size.Fixed(len(sliced)*.4)]
    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
    ax = fig.add_axes(divider.get_position(),axes_locator=divider.new_locator(nx=1, ny=1))
    ax.hlines(np.arange(len(sliced)),np.zeros(len(sliced)),np.ones(len(sliced))*4.5,
              color='k',linestyle='--',zorder=0)
    g = sns.scatterplot(x='FC',y='term_name',data=sliced,hue='negative_log10_of_adjusted_p_value',
               size='term_size',sizes=(150,800),palette='Reds',
               legend='brief',edgecolor='k',
               hue_norm=(-7,30),ax=ax)
    g.legend(bbox_to_anchor=(1.2,1))
    plt.savefig(source+'.svg')