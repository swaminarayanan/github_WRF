#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:47:49 2024

@author: lab
"""
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
import pandas as pd

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Circle

# Load the dataset
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20190315.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20200303.nc')

# Select the region of interest and calculate non-cumulative data
non_cumulative_ds1 = ds1['qhail']#.isel(time=16).squeeze()
ds1 = non_cumulative_ds1.mean(dim=['lat', 'lon']) / 1*1.0e+08
# Replace values less than 1 with np.nan
non_ds1 = np.where(ds1 < 0.05, np.nan, ds1)

non_cumulative_ds2 = ds2['qhail']#.isel(time=16).squeeze()
ds2 = non_cumulative_ds2.mean(dim=['lat', 'lon']) / 1*1.0e+08
# Replace values less than 1 with np.nan
non_ds2 = np.where(ds2 < 0.05, np.nan, ds2)

# Define the position and radius of the circle
lat = 23.45    # Example latitude
lon = 85.4   # Example longitude
rad = 0.05          # Adjusted radius to be in degrees


# Extract longitude and latitude
lons2 = ds2['time'].values
lats2 = ds2['lev'].values
time = pd.to_datetime(ds2['time'].values)

# Define the position and radius of the circle
latitude = 23.1
longitude = 85.1
radius = 0.05
# lev1 = np.arange(0, 3, 0.5)
# lev2 = np.arange(0, 3, 0.5)

# Create the plot with Cartopy
fig = plt.figure(figsize=(18, 9))
gs = gridspec.GridSpec(1, 2)#, width_ratios=[4, 4], hspace=0.15, wspace=0.12)

ax1 = fig.add_subplot(gs[0, 0])
pcm1 = ax1.contourf(time, lats2, non_ds1.T, cmap='jet')
ax1.set_yticks(np.arange(100, 950.1, 100))
# ax2.set_xlim([])
ax1.set_ylim([100, 950.1])
ax1.invert_yaxis()

# # First subplot: ax1
# ax1 = fig.add_subplot(gs[0, 0], projection=ccrs.PlateCarree())
# pcm1 = ax1.contourf(lons1, lats1, non_cumulative_ds1, cmap='jet', levels=lev1, extend='both')
# ax1.set_xticks(np.arange(82, 88.61, 1))
# ax1.set_yticks(np.arange(21, 25.1, 1))
# ax1.set_xlim([82, 88.1])
# ax1.set_ylim([21, 25.1])

# # Modify the X-tick labels to show longitude with "E"
# ax1.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(82, 88.61, 1)], fontsize=10, fontweight='bold')

# Modify the Y-tick labels to show latitude with "N"
# ax1.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 25.1, 1)], fontsize=10, fontweight='bold')

# Second subplot: ax2
ax2 = fig.add_subplot(gs[0, 1])
pcm2 = ax2.contourf(time, lats2, non_ds2.T, cmap='jet')
# Add the circle at the specified position
# cir = Circle((lon, lat), radius, color='#FF6E00', fill=True, transform=ccrs.PlateCarree())
# ax2.add_patch(cir)

# # Add text inside the circle
# ax2.text(lon, lat, '', color='black', fontsize=16, ha='center', va='center')#, 
#          # bbox=dict(facecolor='white', edgecolor='#FF6E00'),# boxstyle='round,pad=0.3'), 
#          # transform=ccrs.PlateCarree())

# ax2.set_xticks(np.arange(82, 88.61, 1))
ax2.set_yticks(np.arange(100, 950.1, 100))
# ax2.set_xlim([])
ax2.set_ylim([100, 950.1])
ax2.invert_yaxis()
dtFmt = mdates.DateFormatter('%H')
ax1.xaxis.set_major_formatter(dtFmt)

# Modify the X-tick labels to show longitude with "E"
# ax2.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(82, 88.61, 1)], fontsize=10, fontweight='bold')
# ax2.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 25.1, 1)], fontsize=10, fontweight='bold')

# Hide Y-tick labels for ax2
ax2.set_yticklabels([])

# Add coastlines, borders, and states for both subplots
# for ax in [ax2]:
#     ax.coastlines(resolution='10m', color='black', linewidth=0.8)
#     ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.5)
#     ax.add_feature(cfeature.STATES.with_scale('10m'), edgecolor='black', linewidth=0.5)

# # Add the circle and text to both subplots
# for ax in [ax1, ax2]:
#     circle = Circle((longitude, latitude), radius, color='none', fill=True, transform=ccrs.PlateCarree())
#     ax.add_patch(circle)
#     ax.text(longitude, latitude, '+', fontsize=12, fontweight='bold', ha='center', va='center',
#             bbox=dict(boxstyle='square', facecolor='none', edgecolor='black', pad=0.5),
#             transform=ccrs.PlateCarree())
# # Add an arrow with length of 2 cm pointing SE (southeast direction)
# arrow_length = 1.7  # Approximate geographic distance (adjust as necessary)
# dx = arrow_length * np.cos(np.radians(68))  # x component for SE direction (45 degrees)
# dy = arrow_length * np.sin(np.radians(45))  # y component for SE direction (45 degrees)

# ax1.annotate('', xy=(longitude + dx, latitude - dy), xytext=(longitude, latitude),
#              arrowprops=dict(facecolor='black', edgecolor='black', shrink=0, width=0.2, headwidth=0.1),
#              transform=ccrs.PlateCarree())
# # Add ">" symbol at the arrow tip (end of the arrow)
# ax1.text(longitude + dx-0.12, latitude - dy, '>', fontsize=22, rotation=300, fontweight='bold',
#          ha='center', va='center', transform=ccrs.PlateCarree())
#############

# Add colorbars for both plots
# cbar1 = plt.colorbar(pcm1, ax=ax1, orientation='vertical', shrink=0.4)
# cbar1.set_label('Hail (mm)', fontsize=10)
# Format the x-axis with hours (H) using matplotlib's date formatter
dtFmt = mdates.DateFormatter('%H')
ax2.xaxis.set_major_formatter(dtFmt)

cbar2 = plt.colorbar(pcm2, ax=[ax1, ax2], orientation='vertical', shrink=0.9)
cbar2.set_label('Hail mixing ratio (kg kg-1)', fontsize=14, fontweight='bold')
cbar2.ax.tick_params(labelsize=10)  # Adjust tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
cbar2.ax.text(0.51, 1.05, '      × 10-8', fontsize=15, fontweight='bold', ha='center', transform=cbar2.ax.transAxes)

# Adjust the position and size of the second colorbar (cbar2)
cbar2.ax.set_position([0.77, 0.2, 0.4, 0.55])  # Left, Bottom, Width, Height
# Add titles to subplots
# ax1.set_title('(a) Event 1', fontsize=12, fontweight='bold')
# ax2.set_title('(a) Event', fontsize=12, fontweight='bold')
# p = fig.suptitle('Hail Events Comparison', fontsize=14, fontweight='bold')# Show the plot
# p.set_position([0.45, 0.755, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, hspace=0.3, wspace=0.2)
# ax1.set_xlabel('lons')
ax1.set_ylabel('pressure (hpa) ', fontsize=14, fontweight='bold')
ax1.set_xlabel('time(UTC)', fontsize=14, fontweight='bold')
ax2.set_xlabel('time(UTC)', fontsize=14, fontweight='bold')
# Update plot parameters for font size, boldness, and tick sizes
plt.rcParams.update({
    "font.weight": "bold",          # Set the default font weight to bold
    "axes.labelweight": "bold",     # Axis label font weight
    'xtick.labelsize': 15,          # X-axis tick label size
    'ytick.labelsize': 15,          # Y-axis tick label size
    "axes.linewidth": 2,            # Line width for the axes
    "patch.linewidth": 2,           # Line width for patches (e.g., circles, rectangles)
    'xtick.major.size': 19,         # Major tick size for X-axis
    'ytick.major.size': 19,         # Major tick size for Y-axis
    'xtick.major.width': 2,         # Major tick width for X-axis
    'ytick.major.width': 2,         # Major tick width for Y-axis
    'axes.titlesize': 16,           # Font size for subplot (ax1, ax2) titles
    'axes.titleweight': 'bold',     # Font weight for subplot titles
    'figure.titlesize': 16,         # Font size for the overall figure title (suptitle)
    'figure.titleweight': 'bold',   # Font weight for the overall figure title
})

plt.show()
