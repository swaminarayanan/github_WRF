
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
# Define the shapefile for India
orissa_shapefile = Reader(r'/home/lab/Desktop/Narayanswamy/hail_work/orissa_shape/Orissa.shp')
orissa_geometries = list(orissa_shapefile.geometries())
orissa_polygon = unary_union(orissa_geometries)
orissa_feature = ShapelyFeature(orissa_geometries, ccrs.PlateCarree(), facecolor='none', edgecolor='black')
# Define a function to check if a point is inside India
def is_inside_orissa(lat, lon, orissa_polygon):
    point = Point(lon, lat)
    return orissa_polygon.contains(point)

india_shapefile = Reader(r'/home/lab/Desktop/Narayanswamy/hail_work/jarkh_shp/Jharkhand.shp')
india_geometries = list(india_shapefile.geometries())
india_polygon = unary_union(india_geometries)
india_feature = ShapelyFeature(india_geometries, ccrs.PlateCarree(), facecolor='none', edgecolor='black')
# Define a function to check if a point is inside India
def is_inside_india(lat, lon, india_polygon):
    point = Point(lon, lat)
    return india_polygon.contains(point)
# Load the dataset
ds11 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20190421.nc')
ds22 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20200303.nc')
# Select the region of interest and calculate non-cumulative data
ds1 = ds11['precipitation'].sum(dim='time').sel(lat=slice(15, 25), lon=slice(80, 90))#.squeeze()#.values
ds2 = ds22['precipitation'].sum(dim='time').sel(lat=slice(21, 26), lon=slice(83, 88))#.squeeze()#.values
#############
lons1 = ds1['lon']
lats1 = ds1['lat']
lons2 = ds2['lon']
lats2 = ds2['lat']
mask1 = np.zeros((len(lats1), len(lons1)), dtype=int)

for i in range(len(lats1)):
    for j in range(len(lons1)):
        if is_inside_orissa(lats1[i], lons1[j], orissa_polygon):
            mask1[i, j] = 1
        else:
            mask1[i, j] = 0 
##############
mask = np.zeros((len(lats2), len(lons2)), dtype=int)

for i in range(len(lats2)):
    for j in range(len(lons2)):
        if is_inside_india(lats2[i], lons2[j], india_polygon):
            mask[i, j] = 1
        else:
            mask[i, j] = 0 
# # # # Replace values less than 1 with np.nan
ds1 = ds1.where(mask1 == 1)
ds2 = ds2.where(mask == 1)
ds1 = np.where(ds1 < 0.1, np.nan, ds1)
ds2 = np.where(ds2 < 0.1, np.nan, ds2)
# Define the position and radius of the circle
lev1 = np.arange(0, 90.1, 5)
lev2 = np.arange(0, 50.1, 5)
# Create the plot with Cartopy
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1], hspace=0.061, wspace=0.12)
ax1 = fig.add_subplot(gs[0, 0], projection=ccrs.PlateCarree())
ax1.add_feature(orissa_feature)
pcm1 = ax1.contourf(lons1, lats1, ds1, transform=ccrs.PlateCarree(), levels = lev1, cmap='Blues', extend ='both')
ax1.set_xticks(np.arange(81, 88.1, 1))
ax1.set_yticks(np.arange(17, 23.1, 1))
ax1.set_xlim([81, 88])
ax1.set_ylim([17, 23])
# Modify the X-tick labels to show longitude with "E"
ax1.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(81, 88.1, 1)], fontsize=10, fontweight='bold', rotation=0)
# Modify the Y-tick labels to show latitude with "N"
ax1.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(17, 23.1, 1)], fontsize=10, fontweight='bold', rotation=46)
ax1.tick_params(axis='both', length=4, width=1.2)
# Second subplot: ax2
ax2 = fig.add_subplot(gs[0, 1], projection=ccrs.PlateCarree())
ax2.add_feature(india_feature)
pcm2 = ax2.contourf(lons2, lats2, ds2, transform=ccrs.PlateCarree(), levels = lev2, cmap='Blues', extend ='both')
ax2.set_xticks(np.arange(83, 89.1, 1))
ax2.set_yticks(np.arange(21, 26.1, 1))
ax2.set_xlim([83, 88])
ax2.set_ylim([21, 26])
ax2.tick_params(axis='both', length=4, width=1.2)
# Modify the X-tick labels to show longitude with "E"
ax2.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(83, 89.1, 1)], fontsize=10, fontweight='bold', rotation=0)
ax2.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 26.1, 1)], fontsize=10, fontweight='bold', rotation=46)
ax1.set_title('(a)', fontsize=11, fontweight='bold')
ax2.set_title('(b)', fontsize=11, fontweight='bold')
# Add colorbars for both plots
cbar1 = plt.colorbar(pcm1, ax=[ax1], orientation='horizontal', shrink=0.5)
cbar1.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
cbar1.ax.tick_params(labelsize=7)  # Adjust tick label size
cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# Adjust the position and size of the second colorbar (cbar2)
cbar1.ax.set_position([0.15, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
cbar1.ax.tick_params(length=2.5, width=1.2)
cbar2 = plt.colorbar(pcm2, ax=[ax2], orientation='horizontal', shrink=0.5)
cbar2.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
cbar2.ax.tick_params(labelsize=7)  # Adjust tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# Adjust the position and size of the second colorbar (cbar2)
cbar2.ax.set_position([0.56, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
cbar2.ax.tick_params(length=2.5, width=1.2)
ax1.set_ylabel('lat')
# Update plot parameters for font size, boldness, and tick sizes
plt.rcParams.update({
    "font.weight": "bold",          # Set the default font weight to bold
    "axes.labelweight": "bold",     # Axis label font weight
    'xtick.labelsize': 10,          # X-axis tick label size
    'ytick.labelsize': 10,          # Y-axis tick label size
    "axes.linewidth": 1,            # Line width for the axes
    "patch.linewidth": 1,           # Line width for patches (e.g., circles, rectangles)
    'xtick.major.size': 8,         # Major tick size for X-axis
    'ytick.major.size': 8,         # Major tick size for Y-axis
    'xtick.major.width': 2,         # Major tick width for X-axis
    'ytick.major.width': 2,         # Major tick width for Y-axis
    'axes.titlesize': 16,           # Font size for subplot (ax1, ax2) titles
    'axes.titleweight': 'bold',     # Font weight for subplot titles
    'figure.titlesize': 16,         # Font size for the overall figure title (suptitle)
    'figure.titleweight': 'bold',   # Font weight for the overall figure title
})
plt.show()



