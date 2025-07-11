

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Circle

# Load the dataset
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
# ds = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20200303.nc')

# Select the region of interest
# ds = ds.sel(lon=slice(86.4, 87.7), lat=slice(20.40, 21.91))

# Calculate non-cumulative data by taking the difference between consecutive time steps
ds = ds1['hailnc'].sel(lon=slice(84.0, 87.0),lat=slice(22.0, 25.0)).squeeze()
# dd = ds1['hailcast_d'].sel(lat=slice(22.8, 23.4), lon=slice(84.8, 85.4)).isel(time=17).squeeze()
# dd = dd.values
a = ds1['hailnc'].sel(lon=86.9,lat=21.5,method='nearest').isel(time=16).values# Extract the longitude and latitude values
b = ds1['hailcast_d'].sel(lon=86.9,lat=21.5,method='nearest').isel(time=17).values# Extract the longitude and latitude values
c = ds1['hailcast_d'].sel(lon=86.9,lat=21.5,method='nearest').isel(time=18).values# Extract the longitude and latitude values
d = ds1['hailcast_d'].sel(lon=86.9, lat=21.5, method='nearest').isel(time=15).values
# print(a, b, c, d)
lons = ds['lon']
lats = ds['lat']

# Define the position and radius of the circle
latitude = 23.3    # Example latitude
longitude = 85.3   # Example longitude
radius = 0.05          # Adjusted radius to be in degrees

# Define the contour levels (now in cm)
k = np.arange(0.01, 0.5, 0.01)  # Adjusted contour levels for cmplt.grid(True, linestyle='--', linewidth=0.7, alpha=0.9, color='gray')

# Loop through non-cumulative time steps from 0 to 47 (since diff reduces the time dimension by 1)
for time_step in range(15, 19):  # 0 to 47 inclusive
    # Extract the non-cumulative variable at the specific time step
    var1 = ds.isel(time=time_step).squeeze()
    var1 = xr.where(var1 < 0.1, np.nan, var1)

    # Create the plot with Cartopy
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())  # Corrected the projection placement

    # Create a contour plot
    pcm1 = ax1.contourf(lons, lats, var1, cmap='jet', transform=ccrs.PlateCarree())

    # Add India's coastlines and state boundaries within the specific domain
    ax1.coastlines(resolution='10m', color='black', linewidth=0.1)
    ax1.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.1)
    ax1.add_feature(cfeature.STATES.with_scale('10m'), edgecolor='black', linewidth=0.1)

    # # Add the circle at the specified position
    # circle = Circle((longitude, latitude), radius, color='#FF6E00', fill=True, transform=ccrs.PlateCarree())
    # ax1.add_patch(circle)
    
    # # Add text inside the circle
    # ax1.text(longitude, latitude, '0.9', color='black', fontsize=16, ha='center', va='center')#, 
    #          # bbox=dict(facecolor='white', edgecolor='#FF6E00'),# boxstyle='round,pad=0.3'), 
    #          # transform=ccrs.PlateCarree())

    # # Set x-axis ticks based on data range
    # x_ticks = np.linspace(lons.min(), lons.max(), num=0.2)  # 5 evenly spaced ticks
    # ax1.set_xticks(x_ticks)
    
    # # Set y-axis ticks based on data range
    y_ticks = np.linspace(22.0, 25.0, 20)  # 5 evenly spaced ticks
    ax1.set_yticks(y_ticks)
    x_ticks = np.linspace(84.0, 87.0, 20)  # 5 evenly spaced ticks
    ax1.set_xticks(x_ticks)
    
    # # Set y-axis ticks based on data range
    # y_ticks = np.linspace(lats.min(), lats.max(), num=0.2)  # 5 evenly spaced ticks
    # ax1.set_yticks(y_ticks)
    ax1.set_xlim(84.0, 87.0)
    ax1.set_ylim(22.0, 25.0)
    ax1.tick_params(axis='x', rotation=45)  # Rotate y-axis labels (if needed)

    # Add a colorbar with updated label in cm
    cbar = plt.colorbar(pcm1, ax=ax1, orientation='vertical', shrink=0.7)
    cbar.set_label('Hail (mm)')  # Update the color bar label to cm

    # Set the title to indicate the time step
    ax1.set_title(f'Time Step: {time_step}')

    # Save the plot to a file (optional)
    # plt.savefig(f'time_step_{time_step}.png')
    plt.grid(True, linestyle='--', linewidth=1, alpha=0.2, color='gray')
    # Show the plot
    plt.show()
    
    # Close the plot to free up memory
    plt.close(fig)
