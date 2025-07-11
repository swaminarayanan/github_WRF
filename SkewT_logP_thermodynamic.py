import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from shapely.geometry import Point
from shapely.ops import unary_union
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
from netCDF4 import Dataset as netcdf
from scipy.stats import ttest_1samp
import pandas as pd
from matplotlib.patches import Circle
from metpy.plots import SkewT
from metpy.units import units
from metpy.calc import parcel_profile
from metpy.units import units

ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
# # ds1 = ds1.sel(lat=slice(22.926, 23.084), lon=slice(84.958, 85.121))#.isel(time=20)
# ds1 = ds1.sel(lat=21.49, lon=86.9, method='nearest')  # Single point
# ds2 = ds2.sel(lat=slice(21.5, 24), lon=slice(84, 86.6))#.isel(time=16)
ds1 = ds1.sel(lon=slice(86.87,86.95),lat=slice(21.44,21.53)).mean(dim=['lon', 'lat'])
ds2 = ds2.sel(lon=slice(85.21,85.41),lat=slice(23.26,23.46)).mean(dim=['lon', 'lat'])
pressure = ds1['pressure'].isel(time=16).squeeze()  # Assuming 'qice' exists in the dataset
wspd = ds1['wspd'].isel(time=16).squeeze()   # Assuming 'qice' exists in the dataset
wdir = ds1['wdir'].isel(time=16).squeeze()   # Assuming 'qice' exists in the dataset
dew_point = ds1['td'].isel(time=16).squeeze()   # Assuming 'qice' exists in the dataset
temperature = ds1['tc'].isel(time=16).squeeze()  # Assuming 'qice' exists in the dataset

    # pressure = ds1['pressure'].mean(dim=['lat', 'lon']).isel(time=20).squeeze()  # Assuming 'qice' exists in the dataset
    # wspd = ds1['wspd'].mean(dim=['lat', 'lon']).isel(time=20).squeeze()   # Assuming 'qice' exists in the dataset
    # wdir = ds1['wdir'].mean(dim=['lat', 'lon']).isel(time=20).squeeze()   # Assuming 'qice' exists in the dataset
    # dew_point = ds1['td'].mean(dim=['lat', 'lon']).isel(time=20).squeeze()   # Assuming 'qice' exists in the dataset
    # temperature = ds1['tc'].mean(dim=['lat', 'lon']).isel(time=20).squeeze()  # Assuming 'qice' exists in the dataset
# Mask missing pressure values and corresponding data
valid_mask = ~np.isnan(pressure)  # Mask to identify valid pressure values

pressure = pressure[valid_mask] * units.hPa
temperature = temperature[valid_mask] * units.degC
dew_point = dew_point[valid_mask] * units.degC
wspd = wspd[valid_mask] * units.knots
wdir = wdir[valid_mask] * units.degrees

# Create the Skew-T plot
fig = plt.figure(figsize=(10, 8))
skew = SkewT(fig)

# Plot the temperatureerature and dewpoint
skew.plot(pressure, temperature, 'r', label='temperature')
skew.plot(pressure, dew_point, 'g', label='Dewpoint')

# Add wind barbs
# Plot wind barbs
skew.plot_barbs(pressure, wspd * np.cos(np.deg2rad(wdir)), wspd * np.sin(np.deg2rad(wdir)))

# Calculate the parcel profile
parcel_profile = parcel_profile(pressure, temperature[0], dew_point[0])
skew.plot(pressure, parcel_profile.values-273.16, 'k', linestyle='--', label='Parcel Profile')
# Add labels, grid, and legend
plt.title('Skew-T Log-P Diagram')
plt.legend(loc='best')
plt.grid(True)

# Add enhancements like dry adiabats, moist adiabats, and mixing lines
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()
# skew.tick_params(axis='both', length=4, width=1.2)

# Show the plot
plt.show()



