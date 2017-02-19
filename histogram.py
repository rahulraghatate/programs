#Import Libraries and packages
from __future__ import division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygal
from datetime import datetime
data = pd.read_csv('btown-citations/2016-first-quarter-citations.csv')
#Data
data.head()
#Dropping records with NA values
data=data.dropna(how='any')
data.shape
ages = data['Cited Person Age']
ages_freq=ages.value_counts()
ages_freq_list = pd.DataFrame({'age':ages_freq.index, 'count':ages_freq.values})
ages_freq_list.sort_values(['age'],ascending=True,inplace=True)
ages_freq_list[['age']]=ages_freq_list[['age']].astype(int).astype(str)
ages_uniq=np.sort(np.unique(ages))
from pygal.style import LightStyle
#Method 1
bar_graph = pygal.Bar(style=LightStyle, width=1200, height=600,
                      legend_at_bottom=True, human_readable=True,
                      title='first-quarter citations')

for index, row in ages_freq_list.iterrows():
    bar_graph.add(row["age"], row["count"])
bar_graph.render_to_file('pygalplot1.svg') 

#Method 2
bar_chart =pygal.Bar(x_label_rotation=-90)
bar_chart.title = "first-quarter citations"      
bar_chart.add("frequency of same ages", ages_freq_list["count"])   
bar_chart.x_labels =ages_uniq 
bar_chart.render_to_file('pygalplot.svg')
