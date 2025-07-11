import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
import pandas as pd
import matplotlib as mpl
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Circle

# Load the dataset
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20200303.nc')
ds1 = ds1.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4))#.isel(time=20)
ds2 = ds2.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4))#.isel(time=16)
rain1 = ds1['qrain'].isel(time=20).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
cloud1 = ds1['qcloud'].isel(time=20).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
graup1 = ds1['qgraup'].isel(time=20).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
snow1 = ds1['qsnow'].isel(time=20).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
ice1 = ds1['qice'].isel(time=20).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
rain2 = ds2['qrain'].isel(time=16).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
cloud2 = ds2['qcloud'].isel(time=16).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
graup2 = ds2['qgraup'].isel(time=16).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
snow2 = ds2['qsnow'].isel(time=16).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
ice2 = ds2['qice'].isel(time=16).mean(dim=['lat', 'lon']).squeeze()/ 1*1.0e+06
# proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(6, 9))
gs = gridspec.GridSpec(1, 2, width_ratios=[1], wspace=0.12)  # Adjusted to 3 columns
# mpl.rcParams['figure.facecolor'] = 'white'
fig.patch.set_facecolor('lightblue')  # Set background color for the entire figure
ax1 = fig.add_subplot(gs[0, 0])  # First column
ax1.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax1.plot(rain1.values, rain1['lev'], color='b', linewidth=2)  # Example plot on top axis
ax1.plot(cloud1.values, cloud1['lev'], color='k', linewidth=2)  # Example plot on top axis
ax1.plot(graup1.values, graup1['lev'], color='r', linewidth=2)  # Example plot on top axis
ax1.plot(snow1.values, snow1['lev'], color='m', linewidth=2)  # Example plot on top axis
ax1.plot(ice1.values, ice1['lev'], color='orange', linewidth=2)  # Example plot on top axis
# ax1.set_xticks(np.arange(84.8, 85.4, 0.1))
# ax1.set_xlim([84.8, 85.4])  # Updated x-axis limits for the bottom axis
# ax1.set_yticks(np.arange(100, 950.1, 100))
# ax1.set_ylim([100, 931])
ax1.set_title('(a) case 1', fontweight='bold', fontsize=22)
ax1.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
# ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax1.tick_params(axis='y', rotation=90)  # Rotate y-axis labels if needed
ax1.invert_yaxis()  # Invert y-axis
ax1.tick_params(axis='both', length=5, width=1.2)
ax1.tick_params(axis='both', labelsize=16)
# ax11 = ax1.twiny()  # Create a twin x-axis sharing the y-axis with ax1
ax1.set_xticks(np.arange(0, 150.1, 25))  # Set ticks on the top x-axis
ax1.set_xlim([0, 150])  # Adjust top axis limits to match top axis data range
ax1.set_yticks(np.arange(200, 1000.1, 100))  # Set ticks on the top x-axis
ax1.set_ylim([1000, 200])  # Adjust top axis limits to match top axis data range
ax1.set_xlabel(r'Mixing ratio (g/kg) $\times 10^{-3}$', fontweight='bold', fontsize=17)
# ax1.set_xticklabels([])
ax1.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

ax2 = fig.add_subplot(gs[0, 1])  # First column
ax2.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax2.plot(rain2.values, rain2['lev'], color='b', linewidth=2)  # Example plot on top axis
ax2.plot(cloud2.values, cloud2['lev'], color='k', linewidth=2)  # Example plot on top axis
ax2.plot(graup2.values, graup2['lev'], color='r', linewidth=2)  # Example plot on top axis
ax2.plot(snow2.values, snow2['lev'], color='m', linewidth=2)  # Example plot on top axis
ax2.plot(ice2.values, ice2['lev'], color='orange', linewidth=2)  # Example plot on top axis
# ax2.set_xticks(np.arange(84.8, 85.4, 0.1))
# ax2.set_xlim([84.8, 85.4])  # Updated x-axis limits for the bottom axis
# ax2.set_yticks(np.arange(100, 950.1, 100))
# ax2.set_ylim([100, 931])
ax2.set_title('(b) case 2', fontweight='bold', fontsize=22)
ax2.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
# ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax2.tick_params(axis='y', rotation=90)  # Rotate y-axis labels if needed
ax2.invert_yaxis()  # Invert y-axis
ax2.tick_params(axis='both', length=5, width=1.2)
ax2.tick_params(axis='both', labelsize=16)
# ax21 = ax2.twiny()  # Create a twin x-axis sharing the y-axis with ax2
ax2.set_xticks(np.arange(0, 150.1, 25))  # Set ticks on the top x-axis
ax2.set_xlim([0, 150])  # Adjust top axis limits to match top axis data range
ax2.set_yticks(np.arange(200, 1000.1, 100))  # Set ticks on the top x-axis
ax2.set_ylim([950, 200])  # Adjust top axis limits to match top axis data range
ax2.set_yticklabels([])
ax2.set_xlabel(r'Mixing ratio (g/kg) $\times 10^{-3}$', fontweight='bold', fontsize=21)
ax2.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.35, color='gray')
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 24,
    'ytick.major.size': 24,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})
plt.show()
