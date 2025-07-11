



import xarray as xr
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
from cartopy.io import shapereader
from shapely.geometry import Point, Polygon
from shapely.ops import unary_union
from cartopy.io import shapereader as shpreader
from cartopy.feature import ShapelyFeature

# Load the dataset
ds = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20190315.nc')
ds11 = ds['qcloud'].isel(time=20).sel(lat=slice(23, 23.6), lon=slice(85, 85.6)).squeeze()#list(range(16, 17)) + list(range(25, 26)) + list(range(32, 32)))
ds12 = ds['qice'].isel(time=20).sel(lat=slice(23, 23.6), lon=slice(85, 85.6)).squeeze()#.isel(time=list(range(16, 17)) + list(range(25, 26)) + list(range(32, 32)))  # Select the specific humidity variable
ds13 = ds['qgraup'].isel(time=20).sel(lat=slice(23, 23.6), lon=slice(85, 85.6)).squeeze()#.isel(time=list(range(16, 17)) + list(range(25, 26)) + list(range(32, 32)))  # Select the specific humidity variable
ds14 = ds['qhail'].isel(time=20).sel(lat=slice(23, 23.6), lon=slice(85, 85.6)).squeeze()#.isel(time=list(range(16, 17)) + list(range(25, 26)) + list(range(32, 32))) # Select the specific humidity variable
ds15 = ds['qrain'].isel(time=20).sel(lat=slice(23, 23.6), lon=slice(85, 85.6)).squeeze()#.isel(time=list(range(16, 17)) + list(range(25, 26)) + list(range(32, 32)))  # Select the specific humidity variable
ds16 = ds['qsnow'].isel(time=20).sel(lat=slice(23, 23.6), lon=slice(85, 85.6)).squeeze()#.isel(time=list(range(16, 17)) + list(range(25, 26)) + list(range(32, 32)))  # Select the specific humidity variable
#mogadishu equator
ds1 = ds11.mean(dim=['lat']) / 1*1.0e+05

# ds1 = ds1.values
ds2 = ds12.mean(dim=['lat']) / 1*1.0e+08
ds3 = ds13.mean(dim=['lat']) / 1*1.0e+06
ds4 = ds14.mean(dim=['lat']) / 1*1.0e+08
ds5 = ds15.mean(dim=['lat']) / 1*1.0e+06
ds6 = ds16.mean(dim=['lat']) / 1*1.0e+05
##################
s1 = ds1.values
s2 = ds2.values
s3 = ds3.values
s4 = ds4.values
s5 = ds5.values
s6 = ds6.values

# Replace zeros with np.nan  # means removing
ds1 = xr.where(ds1 == 0, np.nan, ds1)
ds2 = xr.where(ds2 == 0, np.nan, ds2)
ds3 = xr.where(ds3 == 0, np.nan, ds3)
ds4 = xr.where(ds4 == 0, np.nan, ds4)
ds5 = xr.where(ds5 == 0, np.nan, ds5)
ds6 = xr.where(ds6 == 0, np.nan, ds6)

##################
s1 = ds1.values
s2 = ds2.values
s3 = ds3.values
s4 = ds4.values
s5 = ds5.values
s6 = ds6.values

lons1 = ds1['lon'].values  # Time values
lons2 = ds2['lon'].values  # Time values
lons3 = ds3['lon'].values  # Time values
lons4 = ds4['lon'].values  # Time values
lons5 = ds5['lon'].values  # Time values
lons6 = ds6['lon'].values  # Time values

lev1 = ds1['lev'].values  # Pressure levels
lev2 = ds2['lev'].values  # Pressure levels
lev3 = ds3['lev'].values  # Pressure levels
lev4 = ds4['lev'].values  # Pressure levels
lev5 = ds5['lev'].values  # Pressure levels
lev6 = ds6['lev'].values  # Pressure levels

# Define the minimum and maximum range for contour levels
min_value = 0

# max_value1 = np.max(ds1)  # Assuming ds1 is your data array
# levels1 = np.linspace(0, max_value1, 10)  # Adjust 100 for the number of levels you need
# max_value2 = np.max(ds2)  # Assuming ds1 is your data array
# levels2 = np.linspace(20, max_value2, 10)  # Adjust 100 for the number of levels you need
# max_value3 = np.max(ds3)  # Assuming ds1 is your data array
# levels3 = np.linspace(50, max_value3, 10)  # Adjust 100 for the number of levels you need
# max_value4 = np.max(ds4)  # Assuming ds1 is your data array
# levels4 = np.linspace(120, max_value4, 10)  # Adjust 100 for the number of levels you need
# max_value5 = np.max(ds5)  # Assuming ds1 is your data array
# levels5 = np.linspace(35, max_value5, 10)  # Adjust 100 for the number of levels you need
# max_value6 = np.max(ds6)  # Assuming ds1 is your data array
# levels6 = np.linspace(100, max_value6, 10)  # Adjust 100 for the number of levels you need
max_value1 = np.max(ds1)  # Assuming ds1 is your data array
levels1 = np.linspace(0, max_value1, 10)  # Adjust 100 for the number of levels you need
max_value2 = np.max(ds2)  # Assuming ds1 is your data array
levels2 = np.linspace(0, max_value2, 10)  # Adjust 100 for the number of levels you need
max_value3 = np.max(ds3)  # Assuming ds1 is your data array
levels3 = np.linspace(0, max_value3, 10)  # Adjust 100 for the number of levels you need
max_value4 = np.max(ds4)  # Assuming ds1 is your data array
levels4 = np.linspace(0, max_value4, 10)  # Adjust 100 for the number of levels you need
max_value5 = np.max(ds5)  # Assuming ds1 is your data array
levels5 = np.linspace(0, max_value5, 10)  # Adjust 100 for the number of levels you need
max_value6 = np.max(ds6)  # Assuming ds1 is your data array
levels6 = np.linspace(0, max_value6, 10)  # Adjust 100 for the number of levels you need
# Create the plot
# fig, ax1 = plt.subplots(2, 4, figsize=(10, 10))
fig = plt.figure(figsize=(16, 16))
gs = gridspec.GridSpec(3, 2, width_ratios=[4, 4], hspace=0.15, wspace=0.12)
ax1 = fig.add_subplot(gs[0, 0])#, projection=ccrs.PlateCarree())

# Create a contour plot with specified levels
pcm1 = ax1.contourf(lons1, lev1, ds1, cmap='rainbow', levels = levels1, extend='both')#, levels=level)

# Set x-axis ticks to display 12 monthly spaced ticks with year information
# x_ticks = np.linspace(start=lons1.min(), stop=lons1.max(), num=10)  # Create 10 evenly spaced ticks
x_ticks = np.arange(85, 85.61, 0.1)  # Create 10 evenly spaced ticks

x_ticks = x_ticks[:7]  # Limit to 12 ticks for the x-axis
# Format the x-axis labels to display months and years in 'MMM-YYYY' format
ax1.set_xticks(x_ticks)
ax1.set_xticklabels([f'{tick:.3f}' for tick in x_ticks], rotation=45)  # Format with 2 decimal places
# ax1.set_xticks(np.arange(60, 100.1, 5))
ax1.set_xticklabels([])

# Set y-axis ticks based on data range
# y_ticks = np.linspace(lev1.min() + 0.001, lev1.max(), num=10)  # Adjusted for better spacing
ax1.set_ylim([100, 1000])  # Set limits to 50–1000 hPa (adjust if needed)

y_ticks = np.arange(100, 1000.2, 100)  # Adjusted for better spacing

ax1.set_yticks(y_ticks)
ax1.invert_yaxis()  # Invert y-axis for vertical profile (top-to-bottom)

ax2 = fig.add_subplot(gs[0, 1])#, projection=ccrs.PlateCarree())

# Create a contour plot with specified levels
pcm2 = ax2.contourf(lons2, lev2, ds2, cmap='rainbow', levels = levels2, extend='both')#, levels=level)
# Set x-axis ticks to display 12 monthly spaced ticks with year information
# x_ticks = np.linspace(start=lons2.min(), stop=lons2.max(), num=10)  # Create 10 evenly spaced ticks
x_ticks = np.arange(85, 85.61, 0.1)  # Create 10 evenly spaced ticks
x_ticks = x_ticks[:7]  # Limit to 12 ticks for the x-axis
# Format the x-axis labels to display months and years in 'MMM-YYYY' format
ax2.set_xticks(x_ticks)
ax2.set_xticklabels([f'{tick:.2f}' for tick in x_ticks], rotation=45)  # Format with 2 decimal places
# ax1.set_xticks(np.arange(60, 100.1, 5))
ax2.set_xticklabels([])

# Set y-axis ticks based on data range
ax2.set_ylim([100, 1000])  # Set limits to 50–1000 hPa (adjust if needed)

y_ticks = np.arange(100, 1000.2, 100)  # Adjusted for better spacing
ax2.set_yticks(y_ticks)
ax2.invert_yaxis()  # Invert y-axis for vertical profile (top-to-bottom)
# ax8.set_yticks(np.arange(60, 100.1, 5))
ax2.set_yticklabels([])

ax3 = fig.add_subplot(gs[1, 0])#, projection=ccrs.PlateCarree())

# Create a contour plot with specified levels
pcm3 = ax3.contourf(lons3, lev3, ds3, cmap='rainbow', levels = levels3, extend='both')#, levels=level)

# Set x-axis ticks to display 12 monthly spaced ticks with year information
# x_ticks = np.linspace(start=lons3.min(), stop=lons3.max(), num=10)  # Create 10 evenly spaced ticks
x_ticks = np.arange(85, 85.61, 0.1)  # Create 10 evenly spaced ticks
x_ticks = x_ticks[:7]  # Limit to 12 ticks for the x-axis
# Format the x-axis labels to display months and years in 'MMM-YYYY' format
ax3.set_xticks(x_ticks)
ax3.set_xticklabels([f'{tick:.2f}' for tick in x_ticks], rotation=45)  # Format with 2 decimal places
# ax1.set_xticks(np.arange(60, 100.1, 5))
ax3.set_xticklabels([])

# Set y-axis ticks based on data range
ax3.set_ylim([100, 1000])  # Set limits to 50–1000 hPa (adjust if needed)

y_ticks = np.arange(100, 1000.2, 100)  # Adjusted for better spacing
ax3.set_yticks(y_ticks)
ax3.invert_yaxis()  # Invert y-axis for vertical profile (top-to-bottom)

ax4 = fig.add_subplot(gs[1, 1])#, projection=ccrs.PlateCarree())

# Create a contour plot with specified levels
pcm4 = ax4.contourf(lons4, lev4, ds4, cmap='rainbow', levels = levels4, extend='both')#, levels=level)

# Set x-axis ticks to display 12 monthly spaced ticks with year information
# x_ticks = np.linspace(start=lons4.min(), stop=lons4.max(), num=10)  # Create 10 evenly spaced ticks
x_ticks = np.arange(85, 85.61, 0.1)  # Create 10 evenly spaced ticks
x_ticks = x_ticks[:7]  # Limit to 12 ticks for the x-axis
# Format the x-axis labels to display months and years in 'MMM-YYYY' format
ax4.set_xticks(x_ticks)
ax4.set_xticklabels([f'{tick:.2f}' for tick in x_ticks], rotation=45)  # Format with 2 decimal places
# ax1.set_xticks(np.arange(60, 100.1, 5))
ax4.set_xticklabels([])

# Set y-axis ticks based on data range
ax4.set_ylim([100, 1000])  # Set limits to 50–1000 hPa (adjust if needed)

y_ticks = np.arange(100, 1000.2, 100)  # Adjusted for better spacing
ax4.set_yticks(y_ticks)
ax4.invert_yaxis()  # Invert y-axis for vertical profile (top-to-bottom)
# ax8.set_yticks(np.arange(60, 100.1, 5))
ax4.set_yticklabels([])

ax5 = fig.add_subplot(gs[2, 0])#, projection=ccrs.PlateCarree())

# Create a contour plot with specified levels
pcm5 = ax5.contourf(lons5, lev5, ds5, cmap='rainbow', levels = levels5, extend='both')#, levels=level)

# Set x-axis ticks to display 12 monthly spaced ticks with year information
# x_ticks = np.linspace(start=lons5.min(), stop=lons5.max(), num=10)  # Create 10 evenly spaced ticks
x_ticks = np.arange(85, 85.61, 0.1)  # Create 10 evenly spaced ticks
x_ticks = x_ticks[:7]  # Limit to 12 ticks for the x-axis
# Format the x-axis labels to display months and years in 'MMM-YYYY' format
ax5.set_xticks(x_ticks)
ax5.set_xticklabels([f'{tick:.1f}' for tick in x_ticks], rotation=45)  # Format with 2 decimal places
# ax1.set_xticks(np.arange(60, 100.1, 5))
# ax5.set_xticklabels([])

# Set y-axis ticks based on data range
ax5.set_ylim([100, 1000])  # Set limits to 50–1000 hPa (adjust if needed)

y_ticks = np.arange(100, 1000.2, 100)  # Adjusted for better spacing
ax5.set_yticks(y_ticks)
ax5.invert_yaxis()  # Invert y-axis for vertical profile (top-to-bottom)

ax6 = fig.add_subplot(gs[2, 1])#, projection=ccrs.PlateCarree())

# Create a contour plot with specified levels
pcm6 = ax6.contourf(lons6, lev6, ds6, cmap='rainbow', levels = levels6, extend='both')#, levels=level)

# Set x-axis ticks to display 12 monthly spaced ticks with year information
# x_ticks = np.linspace(start=lons6.min(), stop=lons6.max(), num=10)  # Create 10 evenly spaced ticks
x_ticks = np.arange(85, 85.61, 0.1) # Create 10 evenly spaced ticks
x_ticks = x_ticks[:7]  # Limit to 12 ticks for the x-axis
# Format the x-axis labels to display months and years in 'MMM-YYYY' format
ax6.set_xticks(x_ticks)
ax6.set_xticklabels([f'{tick:.1f}' for tick in x_ticks], rotation=45)  # Format with 2 decimal places
# ax1.set_xticks(np.arange(60, 100.1, 5))
#ax6.set_xticklabels([])

# Set y-axis ticks based on data range
ax6.set_ylim([100, 1000])  # Set limits to 50–1000 hPa (adjust if needed)

y_ticks = np.arange(100, 1000.2, 100)  # Adjusted for better spacing
ax6.set_yticks(y_ticks)
ax6.invert_yaxis()  # Invert y-axis for vertical profile (top-to-bottom)
# ax6.set_yticks(np.arange(60, 100.1, 5))
ax6.set_yticklabels([])

# Add a colorbar for qcloud
cbar1 = plt.colorbar(pcm1, ax=[ax1], orientation='vertical', shrink=0.7)
cbar1.set_label('qcloud (kg kg⁻¹)', fontsize=16, fontweight='bold')
# Add the scale (× 10⁷) to the top of the colorbar
cbar1.ax.text(0.65, 1.05,r'$\times   10^{-5}$', fontsize=18, fontweight='bold', ha='center', transform=cbar1.ax.transAxes)

# Add a colorbar for qice
cbar2 = plt.colorbar(pcm2, ax=[ax2], orientation='vertical', shrink=0.7)
cbar2.set_label('qice (kg kg⁻¹)', fontsize=16, fontweight='bold')
# Add the scale (× 10⁹) to the top of the colorbar
cbar2.ax.text(0.51, 1.05,r'$\times   10^{-8}$', fontsize=18, fontweight='bold', ha='center', transform=cbar2.ax.transAxes)

# Add a colorbar for qgraup
cbar3 = plt.colorbar(pcm3, ax=[ax3], orientation='vertical', shrink=0.7)
cbar3.set_label('qgraup (kg kg⁻¹)', fontsize=16, fontweight='bold')
# Add the scale (× 10⁷) to the top of the colorbar
cbar3.ax.text(0.51, 1.05,r'$\times   10^{-6}$', fontsize=18, fontweight='bold', ha='center', transform=cbar3.ax.transAxes)

# Add a colorbar for qhail
cbar4 = plt.colorbar(pcm4, ax=[ax4], orientation='vertical', shrink=0.7)
cbar4.set_label('qhail (kg kg⁻¹)', fontsize=16, fontweight='bold')
# Add the scale (× 10⁸) to the top of the colorbar
cbar4.ax.text(0.51, 1.05,r'$\times   10^{-8}$', fontsize=18, fontweight='bold', ha='center', transform=cbar4.ax.transAxes)

# Add a colorbar for qrain
cbar5 = plt.colorbar(pcm5, ax=[ax5], orientation='vertical', shrink=0.7)
cbar5.set_label('qrain (kg kg⁻¹)', fontsize=16, fontweight='bold')
# Add the scale (× 10⁷) to the top of the colorbar
cbar5.ax.text(0.51, 1.05, r'$\times   10^{-6}$', fontsize=18, fontweight='bold', ha='center', transform=cbar5.ax.transAxes)

# Add a colorbar for qsnow
cbar6 = plt.colorbar(pcm6, ax=[ax6], orientation='vertical', shrink=0.7)
cbar6.set_label('qsnow (kg kg⁻¹)', fontsize=16, fontweight='bold')
# Add the scale (× 10⁷) to the top of the colorbar
# cbar6.ax.text(0.51, 1.05, '      × 10', fontsize=18, fontweight='bold', ha='center', transform=cbar6.ax.transAxes)
cbar6.ax.text(0.51, 1.05, r'$\times   10^{-5}$', fontsize=18, fontweight='bold', ha='center', transform=cbar6.ax.transAxes)


# Set the title and labels
ax1.set_title('(a)qcloud', fontsize=16, fontweight='bold')
ax2.set_title('(b)qice', fontsize=16, fontweight='bold')
ax3.set_title('(c)qgraup', fontsize=16, fontweight='bold')
ax4.set_title('(d)qhail', fontsize=16, fontweight='bold')
ax5.set_title('(e)qrain', fontsize=16, fontweight='bold')
ax6.set_title('(f)qsnow', fontsize=16, fontweight='bold')
ax5.set_xlabel('lons', fontsize=16, fontweight='bold')
ax6.set_xlabel('lons', fontsize=16, fontweight='bold')

ax1.set_ylabel('Pressure Level (hPa)', fontsize=14, fontweight='bold')
ax3.set_ylabel('Pressure Level (hPa)', fontsize=14, fontweight='bold')
ax5.set_ylabel('Pressure Level (hPa)', fontsize=14, fontweight='bold')
p=plt.suptitle('Vertical Profile of hydrometeors', fontsize=20, fontweight='bold')
p.set_position([0.5029, 0.9255, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, hspace=0.3, wspace=0.2)

plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 10,
    'ytick.major.size': 10,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 16, # For axes titles
    'figure.titlesize': 20 # For overall figure title
})

# Show the plot
plt.show()

# Close the plot to free up memory
plt.close(fig)



