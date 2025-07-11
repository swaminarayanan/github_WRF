
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
non_cumulative_ds1 = ds1['hailnc'].isel(time=20).squeeze().values
non_cumulative_ds2 = ds2['hailnc'].isel(time=17).squeeze().values

# Replace values less than 1 with np.nan
non_cumulative_ds1 = np.where(non_cumulative_ds1 < 0.05, np.nan, non_cumulative_ds1)
non_cumulative_ds2 = np.where(non_cumulative_ds2 < 0.05, np.nan, non_cumulative_ds2)

# Define the position and radius of the circle
lat = 23.45    # Example latitude
lon = 85.4   # Example longitude
rad = 0.05          # Adjusted radius to be in degrees


# Extract longitude and latitude
lons1 = ds1['lon'].values
lats1 = ds1['lat'].values
lons2 = ds2['lon'].values
lats2 = ds2['lat'].values

# Define the position and radius of the circle
latitude = 23.1
longitude = 85.1
radius = 0.05
lev1 = np.arange(0, 3, 0.5)
lev2 = np.arange(0, 3, 0.5)

# Create the plot with Cartopy
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(1, 2, width_ratios=[4, 4], hspace=0.15, wspace=0.12)

# First subplot: ax1
ax1 = fig.add_subplot(gs[0, 0], projection=ccrs.PlateCarree())
pcm1 = ax1.contourf(lons1, lats1, non_cumulative_ds1, cmap='jet', levels=lev1, extend='both')
ax1.set_xticks(np.arange(82, 88.61, 1))
ax1.set_yticks(np.arange(21, 25.1, 1))
ax1.set_xlim([82, 88.1])
ax1.set_ylim([21, 25.1])

# Modify the X-tick labels to show longitude with "E"
ax1.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(82, 88.61, 1)], fontsize=10, fontweight='bold')

# Modify the Y-tick labels to show latitude with "N"
ax1.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 25.1, 1)], fontsize=10, fontweight='bold')

# Second subplot: ax2
ax2 = fig.add_subplot(gs[0, 1], projection=ccrs.PlateCarree())
pcm2 = ax2.contourf(lons2, lats2, non_cumulative_ds2, cmap='jet', levels=lev2, extend='both')
# Add the circle at the specified position
# cir = Circle((lon, lat), radius, color='#FF6E00', fill=True, transform=ccrs.PlateCarree())
# ax2.add_patch(cir)

# # Add text inside the circle
# ax2.text(lon, lat, '', color='black', fontsize=16, ha='center', va='center')#, 
#          # bbox=dict(facecolor='white', edgecolor='#FF6E00'),# boxstyle='round,pad=0.3'), 
#          # transform=ccrs.PlateCarree())

ax2.set_xticks(np.arange(82, 88.61, 1))
ax2.set_yticks(np.arange(21, 25.1, 1))
ax2.set_xlim([82, 88.1])
ax2.set_ylim([21, 25.1])

# Modify the X-tick labels to show longitude with "E"
ax2.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(82, 88.61, 1)], fontsize=10, fontweight='bold')

# Hide Y-tick labels for ax2
ax2.set_yticklabels([])

# Add coastlines, borders, and states for both subplots
for ax in [ax1, ax2]:
    ax.coastlines(resolution='10m', color='black', linewidth=0.8)
    ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.5)
    ax.add_feature(cfeature.STATES.with_scale('10m'), edgecolor='black', linewidth=0.5)



for ax in [ax1]:
    circle = Circle((longitude, latitude), radius, color='none', fill=True, transform=ccrs.PlateCarree())
    ax.add_patch(circle)
    ax.text(longitude, latitude, '+', color='#35D7FF', fontsize=20, fontweight='bold', ha='center', va='center',
            transform=ccrs.PlateCarree())


for ax in [ax2]:
    circle = Circle((longitude, latitude), radius, color='none', fill=True, transform=ccrs.PlateCarree())
    ax.add_patch(circle)
    ax.text(longitude, latitude, '+', color='#AEF359', fontsize=20, fontweight='bold', ha='center', va='center',
            transform=ccrs.PlateCarree())


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
cbar2 = plt.colorbar(pcm2, ax=[ax2, ax1], orientation='vertical', shrink=0.7)
cbar2.set_label('Hail (mm)', fontsize=8, fontweight='bold')
cbar2.ax.tick_params(labelsize=10)  # Adjust tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels

# Adjust the position and size of the second colorbar (cbar2)
cbar2.ax.set_position([0.75, 0.35, 0.3, 0.3])  # Left, Bottom, Width, Height
# Add titles to subplots
ax1.set_title('(a) Ranchi 20190315', fontsize=12, fontweight='bold')
ax2.set_title('(b) Ranchi 20200303', fontsize=12, fontweight='bold')
p = fig.suptitle('Hail Events Comparison', fontsize=14, fontweight='bold')# Show the plot
p.set_position([0.45, 0.755, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, hspace=0.3, wspace=0.2)
ax1.set_xlabel('lons')
ax1.set_ylabel('lats')
ax2.set_xlabel('lons')
# Update plot parameters for font size, boldness, and tick sizes
plt.rcParams.update({
    "font.weight": "bold",          # Set the default font weight to bold
    "axes.labelweight": "bold",     # Axis label font weight
    'xtick.labelsize': 13,          # X-axis tick label size
    'ytick.labelsize': 13,          # Y-axis tick label size
    "axes.linewidth": 2,            # Line width for the axes
    "patch.linewidth": 2,           # Line width for patches (e.g., circles, rectangles)
    'xtick.major.size': 10,         # Major tick size for X-axis
    'ytick.major.size': 10,         # Major tick size for Y-axis
    'xtick.major.width': 2,         # Major tick width for X-axis
    'ytick.major.width': 2,         # Major tick width for Y-axis
    'axes.titlesize': 16,           # Font size for subplot (ax1, ax2) titles
    'axes.titleweight': 'bold',     # Font weight for subplot titles
    'figure.titlesize': 16,         # Font size for the overall figure title (suptitle)
    'figure.titleweight': 'bold',   # Font weight for the overall figure title
})

plt.show()
