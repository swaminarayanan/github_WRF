import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.lines import Line2D
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Circle

# Load the dataset
ds11 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20190315.nc')
ds21 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20200303.nc')
ds12 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20190315.nc')
ds22 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')

# Select the region of interest and calculate non-cumulative data
dsa = ds11['precipitation'].sel(lat=slice(22.3, 24.3), lon=slice(84.6, 86.2))
dsb = ds21['precipitation'].sel(lat=slice(22.3, 24.3), lon=slice(84.6, 86.2))#.isel(time=16).squeeze()

dsc = ds12['rainc'].sel(lat=slice(22.3, 24.3), lon=slice(84.6, 86.2)).diff(dim='time', n=1).mean(dim=['lat', 'lon']).squeeze()#.isel(time=16).squeeze()
dsd = ds12['rainnc'].sel(lat=slice(22.3, 24.3), lon=slice(84.6, 86.2)).diff(dim='time', n=1).mean(dim=['lat', 'lon']).squeeze()#.isel(time=16).squeeze()

dse = ds22['rainc'].sel(lat=slice(22.3, 24.3), lon=slice(84.6, 86.2)).diff(dim='time', n=1).mean(dim=['lat', 'lon']).squeeze()#.isel(time=16).squeeze()
dsf = ds22['rainnc'].sel(lat=slice(22.3, 24.3), lon=slice(84.6, 86.2)).diff(dim='time', n=1).mean(dim=['lat', 'lon']).squeeze()#.isel(time=16).squeeze()
dsa = dsa.mean(dim=['lat', 'lon']).values
dsb = dsb.mean(dim=['lat', 'lon']).values# / 1*1.0e+08
# ds1 = ds1.mean(dim=['lat', 'lon']).values
# ds2 = ds2.mean(dim=['lat', 'lon']).values# / 1*1.0e+08
ds1 = dsc + dsd
ds2 = dsf + dsf
# Replace values less than 1 with np.nan
# ds1 = np.where(ds1 < 1, np.nan, ds1)
# ds2 = np.where(ds2 < 1, np.nan, ds2)

# Define the position and radius of the circle
lat = 23.45    # Example latitude
lon = 85.4   # Example longitude
rad = 0.05          # Adjusted radius to be in degrees

lev1 = np.arange(0, 23.6, 0.5)

# # Extract longitude and latitude
# lons2 = ds2['time'].values
# lats2 = ds2['lev'].values
# time = pd.to_datetime(ds2['time'].values)

# Define the position and radius of the circle
latitude = 23.1
longitude = 85.1
radius = 0.05
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(1, 1)#, width_ratios=[4, 4], hspace=0.15, wspace=0.12)

# # First subplot: ax1
ax1 = fig.add_subplot(gs[0, 0])

# Plotting the data with proper labels
ax1.plot(lev1, dsa, color='r', markersize=5, markerfacecolor='yellow',  linestyle='-', linewidth=1, label='case 1 obs ')
ax1.plot(lev1, dsb, color='k', markersize=5, markerfacecolor='green', linestyle='-', linewidth=1, label='case 2 obs ')
ax1.plot(lev1, ds1, color='r', markersize=5, markerfacecolor='yellow', linestyle=(0, (5, 10)), linewidth=1, label='case 1 model ')
ax1.plot(lev1, ds2, color='k', markersize=5, markerfacecolor='green', linestyle=(0, (5, 10)), linewidth=1, label='case 2 model ')

for x, y in zip(lev1, dsa):
    ax1.text(x, y, '1', fontsize=8, ha='center', va='center', color='red')
for x, y in zip(lev1, dsb):
    ax1.text(x, y, '2', fontsize=8, ha='center', va='center', color='k')
for x, y in zip(lev1, ds1):
    ax1.text(x, y, '1', fontsize=8, ha='center', va='center', color='red')
for x, y in zip(lev1, ds2):
    ax1.text(x, y, '2', fontsize=8, ha='center', va='center', color='k')

ax1.text(18.5, 1.81, '1', fontsize=7.4, color='r', fontweight='bold')
ax1.text(18.5, 1.68, '2', fontsize=7.4, color='k', fontweight='bold')
ax1.text(18.4, 1.557, '1', fontsize=7.4, color='r', fontweight='bold')
ax1.text(18.4, 1.43, '2', fontsize=7.4, color='k', fontweight='bold')
# Set X-axis ticks and limits
ax1.set_xticks(np.arange(0, 24.1, 3))
ax1.set_xlim([0, 24])
ax1.tick_params(axis='both', length=5, width=1.2)

# Set axis labels
ax1.set_ylabel('mean Precipitation (mm)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Time (UTC)', fontsize=12, fontweight='bold')

# Add a legend
# ax1.legend(fontsize=12, loc='upper right', title='Legend', title_fontsize=12)

ax1.legend(fontsize=12, loc='upper right', title=' ', title_fontsize=12, frameon=True)  # Ensure the legend frame is enabled
legend = ax1.get_legend()
legend.get_frame().set_facecolor('none')  # Transparent face color
legend.get_frame().set_alpha(0)          # Set alpha to 0 for transparency
# Update plot parameters for font size, boldness, and tick sizes
plt.rcParams.update({
    "font.weight": "bold",          # Set the default font weight to bold
    "axes.labelweight": "bold",     # Axis label font weight
    'xtick.labelsize': 8,          # X-axis tick label size
    'ytick.labelsize': 8,          # Y-axis tick label size
    "axes.linewidth": 2,            # Line width for the axes
    "patch.linewidth": 2,           # Line width for patches (e.g., circles, rectangles)
    'xtick.major.size': 14,         # Major tick size for X-axis
    'ytick.major.size': 14,         # Major tick size for Y-axis
    'xtick.major.width': 2,         # Major tick width for X-axis
    'ytick.major.width': 2,         # Major tick width for Y-axis
    'axes.titlesize': 16,           # Font size for subplot (ax1, ax1) titles
    'axes.titleweight': 'bold',     # Font weight for subplot titles
    'figure.titlesize': 16,         # Font size for the overall figure title (suptitle)
    'figure.titleweight': 'bold',   # Font weight for the overall figure title
})

plt.show()
