



import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Load the NetCDF file (replace with your actual dataset file paths)
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20200303.nc')
ds3 = xr.open_dataset(r'/media/lab/My Passport/hail/specifichumidity_2019.nc')
ds4 = xr.open_dataset(r'/media/lab/My Passport/hail/specifichumidity_2020.nc')

# Select the data
ds1 = ds1.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=20)
# ds2 = ds2.isel(time=)
ds2 = ds2.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.6)).isel(time=16)
# ds4 = ds4.isel(time=16)

# Extract variables
cape1 = ds2['mcape'].mean(dim=['lat', 'lon']).squeeze()
t1 = ds2['rh'].mean(dim=['lat']).squeeze()
# sh1 = ds3['specific_humidity'].mean(dim=['lat']).squeeze()

cape2 = ds2['cin'].mean(dim=['lat']).squeeze()
t2 = ds2['tc'].mean(dim=['lat']).squeeze()
# sh2 = ds4['specific_humidity'].mean(dim=['lat']).squeeze()

# Set up a map projection
proj = ccrs.PlateCarree()

# # Create a figure and axis with Cartopy projection
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 10))

# # Plot for cape1, t1, sh1 (ds1 and ds3 data)
# Create the figure and GridSpec with 3 columns and 1 row
fig = plt.figure(figsize=(20, 8))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1], wspace=0.12)  # Adjusted to 3 columns
mpl.rcParams['figure.facecolor'] = 'white'
ax1 = fig.add_subplot(gs[0, 0])  # First column

# Plot shaded CAPE using contourf (filled contour)
cape1_filled_contour = ax1.contourf(ds1['lon'], ds1['lev'], cape1, cmap='YlOrBr', 
                                  levels=np.linspace(cape1.min(), cape1.max(), 10))

# Plot Temperature using contour (line contours with labels)
t1_contour = ax1.contour(ds1['lon'], ds1['lev'], t1, colors='k', linewidths=2, 
                          levels=np.linspace(t1.min(), t1.max(), 10))
ax1.clabel(t1_contour, inline=True, fontsize=15, fmt='%1.0f')

# # Plot Specific Humidity using dotted contour lines (dashed contourf)
# sh1_filled_contour = ax1.contour(ds3['lon'], ds3['lev'], sh1, cmap='seismic', alpha=0.7, linewidths=2,
#                                   levels=np.linspace(sh1.min(), sh1.max(), 10), 
#                                   linestyles='--')
# ax1.clabel(sh1_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# Axis and ticks formatting
ax1.set_yticks(np.arange(100, 1000.1, 100))
ax1.set_ylim([100, 1000])
ax1.set_xticks(np.arange(80, 90.1, 1))
ax1.set_xlim([80, 90])

ax1.invert_yaxis()
ax1.set_title('(a)  ', fontweight='bold', fontsize=22)
ax1.set_xlabel('Longitude', fontweight='bold', fontsize=20)
ax1.set_ylabel('Pressure(hpa)', fontweight='bold', fontsize=20)
ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0f}°E'.format(x)))
# Rotate the x-axis tick labels by 90 degrees
ax1.tick_params(axis='y', rotation=45) # Rotate y-axis labels (if needed)
ax1.tick_params(axis='x',  rotation=45)  # Rotate y-axis labels (if needed)

# Plot for cape2, t2, sh2 (ds2 and ds4 data)
ax2 = fig.add_subplot(gs[0, 1])  # First column

# Plot shaded CAPE using contourf (filled contour)
cape2_filled_contour = ax2.contourf(ds2['lon'], ds2['lev'], cape2, cmap='YlOrBr', 
                                  levels=np.linspace(cape2.min(), cape2.max(), 10))

# Plot Temperature using contour (line contours with labels)
t2_contour = ax2.contour(ds2['lon'], ds2['lev'], t2, colors='k', linewidths=2, 
                          levels=np.linspace(t2.min(), t2.max(), 10))
ax2.clabel(t2_contour, inline=True, fontsize=15, fmt='%1.0f')

# Plot Specific Humidity using dotted contour lines (dashed contourf)
# sh2_filled_contour = ax2.contour(ds4['lon'], ds4['lev'], sh2, cmap='seismic', alpha=0.7, linewidths=2,
#                                   levels=np.linspace(sh2.min(), sh2.max(), 10), 
#                                   linestyles='--')
# ax2.clabel(sh2_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# Axis and ticks formatting
ax2.set_yticks(np.arange(100, 1000.1, 100))
ax2.set_ylim([100, 1000])
ax2.set_yticklabels([])

ax2.set_xticks(np.arange(80, 90.1, 1))
ax2.set_xlim([80, 90])

ax2.invert_yaxis()
ax2.set_title('(b) ', fontweight='bold', fontsize=22)
ax2.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax2.set_ylabel('Pressure', fontweight='bold', fontsize=24)
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0f}°E'.format(x)))
# Rotate the x-axis tick labels by 90 degrees
# ax2.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
ax2.tick_params(axis='y', rotation=90)  # Rotate y-axis labels (if needed)
ax2.tick_params(axis='x', rotation=45)  # Rotate y-axis labels (if needed)

# # Add colorbars for both plots
# cbar1 = plt.colorbar(cape1_filled_contour, ax=ax1, orientation='vertical', shrink=0.7)
# cbar1.set_label('CAPE (J/kg)', fontsize=22)
# cbar1.ax.tick_params(labelsize=20)  # Set tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=45)  # Rotate y-axis labels if needed

cbar1 = plt.colorbar(cape1_filled_contour, ax=[ax1], orientation='vertical', shrink=0.7)
cbar1.set_label('CAPE (J/kg)', fontsize=22)
cbar1.ax.tick_params(labelsize=20)  # Set tick label size
cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
# cbar2.set_position([0.8, 0.94, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# cbar1.ax.set_position([0.755, 0.185, 0.65, 0.6])  # Adjust colorbar position: [left, bottom, width, height]
cbar2 = plt.colorbar(cape2_filled_contour, ax=[ax2], orientation='vertical', shrink=0.7)
cbar2.set_label('CIN (J/kg)', fontsize=22)
cbar2.ax.tick_params(labelsize=20)  # Set tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
# cbar2.set_position([0.8, 0.94, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# cbar2.ax.set_position([0.755, 0.185, 0.65, 0.6])  # Adjust colorbar position: [left, bottom, width, height]

# p = fig.suptitle('CAPE, Relative humidity', fontsize=20, fontweight='bold')# Show the plot
# p.set_position([0.434, 0.99, 0.3, 0.2])  # (L-R, T-B,  cbar length vertical, CBAR width,   Adjust the po,sition and size of the colorbar
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 16,
    'ytick.major.size': 16,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})

# Adjust layout and show the plot
plt.show()


