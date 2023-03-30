import pandas as pd 
import plotly.figure_factory as ff 
import csv 


#Calculating mean with open


#Creating a distribution plot 
dataFrames = pd.read_csv("data_1.csv")
figure = ff.create_distplot([dataFrames["Avg Rating"].tolist()], ["Avg Rating"], show_hist = True) 
figure.show()