

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Circle
import matplotlib.gridspec as gridspec

# Load the dataset
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/ice_mixing_ratio.nc')

# Select the region of interest
# ds1 = ds1.sel(lon=slice(86.4, 87.7), lat=slice(20.40, 21.91))
# ds2 = ds2.sel(lon=slice(84.8, 85.4), lat=slice(22.8, 23.4))

# # Calculate non-cumulative data by taking the difference between consecutive time steps
dsa = ds1['qice'].isel(lev=15)#.diff(dim='time', n=1) / 1*1.0e+03 #.sel(lev=350,method='nearest')#.sel(lon=slice(86.5, 87.51),lat=slice(21,22)).squeeze()
dsb = ds2['precipitation']#.sel(lev=350,method='nearest')#.sel(lon=slice(86.5, 87.51),lat=slice(21,22)).squeeze()
# # dd = ds1['hailcast_d'].sel(lat=slice(22.8, 23.4), lon=slice(84.8, 85.4)).isel(time=17).squeeze()
# dd = dd.values
# non_cumulative_ds1 = ds1['rainc'].diff(dim='time', n=1)# / 10.0  # Convert to cm
# non_cumulative_ds2 = ds1['rainnc'].diff(dim='time', n=1)# / 10.0  # Convert to cm
# dsa = non_cumulative_ds1 + non_cumulative_ds2
# non_cumulative_ds11 = ds2['rainc'].diff(dim='time', n=1)# / 10.0  # Convert to cm
# non_cumulative_ds22 = ds2['rainnc'].diff(dim='time', n=1)# / 10.0  # Convert to cm
# dsb = non_cumulative_ds11 + non_cumulative_ds22

# a = ds1['hailcast_d'].sel(lon=86.9,lat=21.5,method='nearest').isel(time=16).values# Extract the longitude and latitude values
# b = ds1['hailcast_d'].sel(lon=86.9,lat=21.5,method='nearest').isel(time=17).values# Extract the longitude and latitude values
# c = ds1['hailcast_d'].sel(lon=86.9,lat=21.5,method='nearest').isel(time=18).values# Extract the longitude and latitude values
# d = ds1['hailcast_d'].sel(lon=86.9, lat=21.5, method='nearest').isel(time=15).values
# print(a, b, c, d)
lons1 = dsa['lon']
lats1 = dsa['lat']
lons2 = dsb['lon']
lats2 = dsb['lat']

# Define the position and radius of the circle
latitude1 = 21.5    # Example latitude
longitude1 = 86.95   # Example longitude
radius = 0.005          # Adjusted radius to be in degrees
latitude2 = 22.95    # Example latitude
longitude2 = 85.05   # Example longitude
radius = 0.005          # Adjusted radius to be in degrees

# Define the contour levels (now in cm)
k = np.arange(0.01, 0.5, 0.01)  # Adjusted contour levels for cmplt.grid(True, linestyle='--', linewidth=0.7, alpha=0.9, color='gray')

# Loop through non-cumulative time steps from 0 to 47 (since diff reduces the time dimension by 1)
for time_step in range(16, 26):  # 0 to 47 inclusive
    # Extract the non-cumulative variable at the specific time step
    var1 = dsa.isel(time=time_step).squeeze()
    var1 = xr.where(var1 < 0, np.nan, var1)
    var2 = dsb.isel(time=time_step).squeeze()
    var2 = xr.where(var2 < 0.000001, np.nan, var2)
    # Create the plot with Cartopy
    fig = plt.figure(figsize=(10, 10))
    gs = gridspec.GridSpec(1, 2, wspace=0.42)  # Adjusted to 3 columns
    ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.PlateCarree())  # Corrected the projection placement

    # Create a contour plot
    pcm1 = ax1.contourf(lons1, lats1, var1, cmap='jet', transform=ccrs.PlateCarree())

    # Add India's coastlines and state boundaries within the specific domain
    ax1.coastlines(resolution='10m', color='black', linewidth=0.1)
    ax1.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.1)
    ax1.add_feature(cfeature.STATES.with_scale('10m'), edgecolor='black', linewidth=0.1)

    # Add the circle at the specified position
    circle = Circle((longitude1, latitude1), radius, color='#FF6E00', fill=True, transform=ccrs.PlateCarree())
    ax1.add_patch(circle)
    
    # # Add text inside the circle
    # ax1.text(longitude1, latitude1, '0.9', color='black', fontsize=16, ha='center', va='center')#, 
    #           # bbox=dict(facecolor='white', edgecolor='#FF6E00'),# boxstyle='round,pad=0.3'), 
    #           # transform=ccrs.PlateCarree())

    # # Set x-axis ticks based on data range
    # x_ticks = np.linspace(lons1.min(), lons1.max(), num=20)  # 5 evenly spaced ticks
    # ax1.set_xticks(x_ticks)
    
    # Set y-axis ticks based on data range
    y_ticks = np.linspace(19.6, 23.3, 20)  # 5 evenly spaced ticks
    ax1.set_yticks(y_ticks)
    x_ticks = np.linspace(84, 89.1, 20)  # 5 evenly spaced ticks
    ax1.set_xticks(x_ticks)
    
    # # Set y-axis ticks based on data range
    # y_ticks = np.linspace(lats.min(), lats.max(), num=0.2)  # 5 evenly spaced ticks
    # ax1.set_yticks(y_ticks)
    # ax1.set_xlim(85, 87.7)
    # ax1.set_ylim(19.4, 22.1)
    ax1.set_xlim(84, 89.1)
    ax1.set_ylim(19.6, 23.3)
    ax1.tick_params(axis='x', rotation=90)  # Rotate y-axis labels (if needed)

    # Add a colorbar with updated label in cm
    cbar = plt.colorbar(pcm1, ax=ax1, orientation='vertical', shrink=0.37)
    cbar.set_label('Hail (mm)')  # Update the color bar label to cm
    ax1.grid(True, linestyle='--', linewidth=1, alpha=0.2, color='gray')

    # Set the title to indicate the time step
    ax1.set_title(f'Time Step: {time_step}')
    ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree())  # Corrected the projection placement

    # Create a contour plot
    pcm2 = ax2.contourf(lons2, lats2, var2, cmap='jet', transform=ccrs.PlateCarree())

    # Add India's coastlines and state boundaries within the specific domain
    ax2.coastlines(resolution='10m', color='black', linewidth=0.1)
    ax2.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.1)
    ax2.add_feature(cfeature.STATES.with_scale('10m'), edgecolor='black', linewidth=0.1)

    # Add the circle at the specified position
    circle = Circle((longitude2, latitude2), radius, color='#FF6E00', fill=True, transform=ccrs.PlateCarree())
    ax2.add_patch(circle)
    
    # # Add text inside the circle
    # ax2.text(longitude2, latitude2, '0.9', color='black', fontsize=16, ha='center', va='center')#, 
    #           # bbox=dict(facecolor='white', edgecolor='#FF6E00'),# boxstyle='round,pad=0.3'), 
    #           # transform=ccrs.PlateCarree())

    # # Set x-axis ticks based on data range
    # x_ticks = np.linspace(lons2.min(), lons2.max(), num=20)  # 5 evenly spaced ticks
    # ax2.set_xticks(x_ticks)
    
    # Set y-axis ticks based on data range
    y_ticks = np.linspace(21, 25, 20)  # 5 evenly spaced ticks
    ax2.set_yticks(y_ticks)
    x_ticks = np.linspace(83, 87, 20)  # 5 evenly spaced ticks
    ax2.set_xticks(x_ticks)
    
    # # Set y-axis ticks based on data range
    # y_ticks = np.linspace(lats.min(), lats.max(), num=0.2)  # 5 evenly spaced ticks
    ax2.set_yticks(y_ticks)
    # ax2.set_xlim(84, 86.5)
    # ax2.set_ylim(22, 24)
    ax2.set_xlim(83, 87)
    ax2.set_ylim(21, 25)
    ax2.tick_params(axis='x', rotation=90)  # Rotate y-axis labels (if needed)

    # Add a colorbar with updated label in cm
    cbar = plt.colorbar(pcm2, ax=ax2, orientation='vertical', shrink=0.37)
    cbar.set_label('Hail (mm)')  # Update the color bar label to cm

    # Set the title to indicate the time step
    ax2.set_title(f'Time Step: {time_step}')

    # Save the plot to a file (optional)
    # plt.savefig(f'time_step_{time_step}.png')
    ax2.grid(True, linestyle='--', linewidth=1, alpha=0.2, color='gray')
    # Show the plot
    plt.rcParams.update({
        "font.weight": "bold",
        "axes.labelweight": "bold",
        'xtick.labelsize': 6,
        'ytick.labelsize': 6,
        "axes.linewidth": 2,
        "patch.linewidth": 2,
        'xtick.major.size': 6,
        'ytick.major.size': 6,
        'xtick.major.width': 2,
        'ytick.major.width': 2,
        'axes.titlesize': 22,  # For axes titles
        'figure.titlesize': 24  # For overall figure title
    })

    plt.show()
    
    # Close the plot to free up memory
    plt.close(fig)
