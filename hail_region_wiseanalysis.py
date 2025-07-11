

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Circle
# Load the dataset
ds = xr.open_dataset(r'/home/lab/Desktop/Narayanswamy/hail_work/hail/milbrandt_20190421.nc')
# ds = ds.sel(lon=slice(85, 85.6), lat=slice(23, 23.6))
# Select the region of interest
# ds = ds.sel(lon= slice(86.4, 87.7), lat=slice(20.40, 21.91))

# Define the contour levels
k = np.arange(1, 12.1, 1)
k = np.arange(0.01, 0.5, 0.01)  # Adjusted contour levels for cm

# Extract the longitude and latitude values
lons = ds['lon']
lats = ds['lat']
# Define the position and radius of the circle
latitude = 22.95    # Example latitude
longitude = 85.07  # Example longitude
radius = 0.05          # Adjusted radius to be in degrees

# Loop through time steps from 0 to 48
for time_step in range(49):  # 0 to 48 inclusive
    # Extract the variable at the specific time step
    # var1 = ds['hailnc'].isel(time=time_step).squeeze().sel(lev=450)

    var1 = ds['hailcast_d'].isel(time=time_step).squeeze()
    # var1 = var1.sel(lev=450)


    # Plotting
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())  # Corrected the subplot index

    # Set the extent to your specific region of interest
    # ax1.set_extent([86.20, 87.30, 21.3, 21.60], crs=ccrs.PlateCarree())

    # Create a contour plot
    pcm1 = ax1.contourf(lons, lats, var1, cmap='jet', rm=ccrs.PlateCarree())

    # Add India's coastlines and state boundaries within the specific domain
    ax1.coastlines(resolution='10m', color='black', linewidth=0.1)
    ax1.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.1)
    ax1.add_feature(cfeature.STATES.with_scale('10m'), edgecolor='black', linewidth=0.1)
    # Set x-axis ticks based on data range
    x_ticks = np.linspace(lons.min(), lons.max(), num=5)  # 5 evenly spaced ticks
    ax1.set_xticks(x_ticks)
    
    # Set y-axis ticks based on data range
    y_ticks = np.linspace(lats.min(), lats.max(), num=5)  # 5 evenly spaced ticks
    ax1.set_yticks(y_ticks)
    # Add the circle at the specified position
    # circle = Circle((longitude, latitude), radius, color='#FF6E00', fill=True, transform=ccrs.PlateCarree())
    # ax1.add_patch(circle)

    # Add a colorbar
    plt.colorbar(pcm1, ax=ax1, orientation='vertical')

    # Set the title to indicate the time step
    ax1.set_title(f'Time Step: {time_step}')

    # Save the plot to a file (optional)
    plt.savefig(f'time_step_{time_step}.png')

    # Show the plot
    plt.show()

    # Close the plot to free up memory
    plt.close(fig)
