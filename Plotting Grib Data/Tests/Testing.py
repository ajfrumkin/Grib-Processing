# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Load necessary libraries
import pygrib
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#Read the GRIB File
grbs = pygrib.open("C:/Users/frumkina/Desktop/Python/Grib Files/T2m_End_of_2019.grib")



grb = grbs.message(1)
lats,lons = grb.latlons()
t2m=(grb.values-273.15) * (9/5) + 32
print(t2m)
fig, ax = plt.subplots(figsize=(10,8))
# m = Basemap(width=12000000, height=9000000, projection='lcc', resolution='h', lat_1=45., lat_2=55, lat_0=40, lon_0=-97.)
m = Basemap(width=6000000, height=3500000, projection='lcc', resolution='h', lat_0=40, lon_0=-97.)
x,y = m(lons,lats)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
cs = m.contourf(x,y,t2m,np.linspace(0,110,40),cmap=plt.cm.jet)
cb = m.colorbar()
t = plt.title('2m Temperature @ ' + str(grb.validDate))
plt.savefig("Test_Image_2m_Temperature.png")
