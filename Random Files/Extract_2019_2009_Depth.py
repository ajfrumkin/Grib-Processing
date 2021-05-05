# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Load necessary libraries
import pygrib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import numpy as np
#import pandas as pd

#Read the GRIB File
grbs = pygrib.open('snow_2019_2009_era5land.grib')
#grb = grbs.message(70128)
#print(grb)
grb = grbs.select(name='Snow depth')
#print(type(grbs))
print(grb[-1])
print(grb[-1].validDate)

#Just playing around with calculations on the data
#aveT = grb.values
#print(aveT.min())
#print(aveT.max())
#print(aveT.shape)


#playing around with calculations on the lats/lons
#grb = grbs.select(name='Snow depth')[0]
#lats, lons = grb.latlons()
#print(lats.shape)
#print(lats.max())
#print(lats.min())
#print(lons.shape)
#print(lons.max())
#print(lons.min())
#print(lats)
#print(lons)


#Grabbing one particular value from aparticular timestep
# grb = grbs.message(1)
# print(grb.validDate) #this prints the message with the variable and timestamp
# data,lats,lons = grb.data()
# lats_round = np.around(lats,decimals=1)
# lons_round = np.around(lons,decimals=1)
# print(data) #this prints the data can be 0-2 
# print(lats)
# print(lons)
# print(type(data)) #Prints the data type
# print(data.shape)
# data2 = grb.data()
# data3 = grb.data()[0]
# data4 = round(data3[4,1]*100,1)
# latitude = round(lats[4,1],1)
# longitude = round(lons[4,1],1)
#a = np.array([[1, 2, 3], [4, 5, 6]])
#newArray = np.append(a, [[50, 60, 70]], axis = 0)
#print(newArray)

#now we will try to loop through multiple steps
Data_File = open("2019_2009_Center_London.txt","w")
list = [("Date,","Time,","Snow_Depth")]
for count in range(1,94202,1):
    print(count)
    grb = grbs.message(count)
    date_time = grb.validDate.strftime("%m/%d/%Y,%H:%M:%S,")
    data,lats,lons = grb.data()
#    print(type(data))
    list.append((date_time,float(data[4,4]*100),"\n"))
    Data_File.write(date_time + str(round(float(data[4,4]*100),1)) + "\n")

Data_File.close()

# #print(list)
# array1 = np.array(list)



#count=1
#grb = grbs.message(count)
#data, lats, lons = grb.data(lat1=45.25, lat2=45.25, lon1=7.5, lon2=7.5)
#print(data)





