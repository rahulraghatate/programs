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
ages_freq_list['bar']= (ages_freq_list['age'] +1).astype(int)

#Creating List of Tuples for Histogram plot
subset = ages_freq_list[['count','age','bar']]
tuples = [tuple(x) for x in subset.values]

#Histogram Plot
from pygal.style import BlueStyle,LightStyle,DarkGreenBlueStyle
hist = pygal.Histogram(legend_at_bottom=True, human_readable=True,
                       title='first-quarter citations histogram',
                       x_title='Age',y_title='No. of Violators')
hist.add('Narrow bars',tuples)
hist.render_to_file('histogram.svg')

#As we can see we see some 116 year-old violators! 
#This is probably an error in the data, so we can remove these data points easily and plot the histogram again:

tuples = [i for i in tuples if i[1] < 100]

#Histogram Plot without outlier
from pygal.style import BlueStyle,LightStyle,DarkGreenBlueStyle
hist = pygal.Histogram(legend_at_bottom=True, human_readable=True,
                       title='first-quarter citations histogram',
                       x_title='Age',y_title='No. of Violators')
hist.add('No. of violators',tuples)
hist.render_to_file('histogram_no_outlier.svg')

ages_freq_list[['age']]=ages_freq_list[['age']].astype(int).astype(str)

#Bar_graph Plot
bar_graph = pygal.Bar(style=LightStyle,x_title='Age',y_title='No. of Violators',
                      legend_at_bottom=True, human_readable=True,
                      title='first-quarter citations bar_graph')

for index, row in ages_freq_list.iterrows():
    bar_graph.add(row["age"], row["count"])
bar_graph.render_to_file('bar_graph_categorized.svg') 

#Bar graph 
bar_chart =pygal.Bar(x_label_rotation=-90,style=LightStyle,
                     x_title='Age',y_title='No. of Violators',
                     legend_at_bottom=True, human_readable=True,
                     title='first-quarter citations bar_graph')
bar_chart.title = "first-quarter citations bar_chart"      
bar_chart.add("No.of violators", ages_freq_list["count"])   
bar_chart.x_labels =ages_uniq 
bar_chart.render_to_file('simple_bar_graph.svg')
