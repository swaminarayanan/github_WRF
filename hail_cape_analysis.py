#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:59:11 2024

@author: lab
"""
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from metpy.units import units
import metpy.calc as mpcalc
import matplotlib as mpl
ds = xr.open_dataset(r'/media/lab/My Passport/hail/ranchi_202003034.nc')
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/gfs/20190315/temperature.nc')

ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/ranchi_202003033.nc')# # Print all variables in the dataset

dss = ds2['gh']#.isel(isobaricInhPa=100.0, time=1, method='nearest').values
dsx1 = dss.sel(latitude=slice(25, 21), longitude=slice(83, 87), isobaricInhPa=500).isel(time=2).squeeze()#.isel(time=2).values#, isobaricInhPa=2)
dsx1 = dss.sel(latitude=slice(25, 21), longitude=slice(83, 87)).isel(time=0).squeeze()#.isel(time=2).values#, isobaricInhPa=2)

x = dsx1.values
dsx1 = dss.sel(latitude=slice(25, 21), longitude=slice(83, 87), isobaricInhPa=100).squeeze()

# print("Variables in the dataset:")
# print(ds1.data_vars)

# # Count the number of variables
# num_variables = len(ds1.data_vars)
# print(f"\nNumber of variables: {num_variables}")
# x = ds1['isobaricInhPa'].values



ds1 = ds1.isel(time=2)


ds1 = ds1.isel(isobaricInhPa=1000, time=2)



ds1 = ds1.sel(isobaricInhPa=1000, method='nearest')
