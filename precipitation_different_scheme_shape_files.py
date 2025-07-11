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
##############################

india_shapefile = Reader(r'/home/lab/Desktop/Narayanswamy/hail_work/jarkh_shp/Jharkhand.shp')
india_geometries = list(india_shapefile.geometries())
india_polygon = unary_union(india_geometries)
india_feature = ShapelyFeature(india_geometries, ccrs.PlateCarree(), facecolor='none', edgecolor='black')
# Define a function to check if a point is inside India
def is_inside_india(lat, lon, india_polygon):
    point = Point(lon, lat)
    return india_polygon.contains(point)
# Load the dataset


ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20200303.nc')
ds3 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds4 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
ds5 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20190421.nc')
ds6 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20200303.nc')
ds7 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
ds8 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20200303.nc')
ds9 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20190421.nc')
ds10 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20200303.nc')

ds11 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20190421.nc')
ds22 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20200303.nc')

dsa = ds1['rainnc'].isel(time=48).sel(lat=slice(15, 25), lon=slice(80, 90)).squeeze()#.values
dsb = ds2['rainnc'].isel(time=48).sel(lat=slice(21, 25.81), lon=slice(83, 88)).squeeze()#.values
dsc = ds3['rainnc'].isel(time=48).sel(lat=slice(15, 25), lon=slice(80, 90)).squeeze()#.values
dsd = ds4['rainnc'].isel(time=48).sel(lat=slice(21, 25.81), lon=slice(83, 88)).squeeze()#.values
dse = ds5['rainnc'].isel(time=48).sel(lat=slice(15, 25), lon=slice(80, 90)).squeeze()#.values
dsf = ds6['rainnc'].isel(time=48).sel(lat=slice(21, 25.81), lon=slice(83, 88)).squeeze()#.values
dsg = ds7['rainnc'].isel(time=48).sel(lat=slice(15, 25), lon=slice(80, 90)).squeeze()#.values
dsh = ds8['rainnc'].isel(time=48).sel(lat=slice(21, 25.81), lon=slice(83, 88)).squeeze()#.values
dsi = ds9['rainnc'].isel(time=48).sel(lat=slice(15, 25), lon=slice(80, 90)).squeeze()#.values
dsj = ds10['rainnc'].isel(time=48).sel(lat=slice(21, 25.81), lon=slice(83, 88)).squeeze()#.values

ds1 = ds11['precipitation'].sum(dim='time').sel(lat=slice(15, 25), lon=slice(80, 90))#.squeeze()#.values
ds2 = ds22['precipitation'].sum(dim='time').sel(lat=slice(21, 26), lon=slice(83, 88))#.squeeze()#.values

lons1 = dsa['lon']
lats1 = dsa['lat']
lons2 = dsb['lon']
lats2 = dsb['lat']

lons11 = ds1['lon']
lats11 = ds1['lat']
lons22 = ds2['lon']
lats22 = ds2['lat']
#################################Model data

mask1 = np.zeros((len(lats1), len(lons1)), dtype=int)

for i in range(len(lats1)):
    for j in range(len(lons1)):
        if is_inside_orissa(lats1[i], lons1[j], orissa_polygon):
            mask1[i, j] = 1
        else:
            mask1[i, j] = 0 
##############
mask = np.zeros((len(lats2), len(lons2)), dtype=int)

for k in range(len(lats2)):
    for l in range(len(lons2)):
        if is_inside_india(lats2[k], lons2[l], india_polygon):
            mask[k, l] = 1
        else:
            mask[k, l] = 0 
            ##################GPM Data
mask11 = np.zeros((len(lats11), len(lons11)), dtype=int)

for m in range(len(lats11)):
    for n in range(len(lons11)):
        if is_inside_orissa(lats11[m], lons11[n], orissa_polygon):
            mask11[m, n] = 1
        else:
            mask11[m, n] = 0 
##############
mask22 = np.zeros((len(lats22), len(lons22)), dtype=int)

for r in range(len(lats22)):
    for s in range(len(lons22)):
        if is_inside_india(lats22[r], lons22[s], india_polygon):
            mask22[r, s] = 1
        else:
            mask22[r, s] = 0 

#################################
# # # # Replace values less than 1 with np.nan
dsa1 = dsa.where(mask1 == 1)
dsb1 = dsb.where(mask == 1)
dsc1 = dsc.where(mask1 == 1)
dsd1 = dsd.where(mask == 1)
dse1 = dse.where(mask1 == 1)
dsf1 = dsf.where(mask == 1)
dsg1 = dsg.where(mask1 == 1)
dsh1 = dsh.where(mask == 1)
dsi1 = dsi.where(mask1 == 1)
dsj1 = dsj.where(mask == 1)

ds1 = ds1.where(mask11 == 1)
ds2 = ds2.where(mask22 == 1)

dsa1 = np.where(dsa1 < 1, np.nan, dsa1)
dsb1 = np.where(dsb1 < 1, np.nan, dsb1)
dsc1 = np.where(dsc1 < 1, np.nan, dsc1)
dsd1 = np.where(dsd1 < 1, np.nan, dsd1)
dse1 = np.where(dse1 < 1, np.nan, dse1)
dsf1 = np.where(dsf1 < 1, np.nan, dsf1)
dsg1 = np.where(dsg1 < 1, np.nan, dsg1)
dsh1 = np.where(dsh1 < 1, np.nan, dsh1)
dsi1 = np.where(dsi1 < 1, np.nan, dsi1)
dsj1 = np.where(dsj1 < 1, np.nan, dsj1)

ds1 = np.where(ds1 < 1, np.nan, ds1)
ds2 = np.where(ds2 < 1, np.nan, ds2)

lev1 = np.arange(0, 100.1, 5)
lev2 = np.arange(0, 25.1, 5)

# Create the plot with Cartopy
fig = plt.figure(figsize=(26, 21))
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], hspace=0.2, wspace=0.1)

ax1 = fig.add_subplot(gs[0, 0], projection=ccrs.PlateCarree())
ax1.add_feature(orissa_feature)
pcm1 = ax1.contourf(lons1, lats1, dsa1, transform=ccrs.PlateCarree(), levels = lev1, cmap='GnBu', extend ='both')
ax1.set_xticks(np.arange(81, 88.1, 1))
ax1.set_yticks(np.arange(17, 23.1, 1))
ax1.set_xlim([81, 88])
ax1.set_ylim([17, 23])
# Modify the X-tick labels to show longitude with "E"
# ax1.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(81, 88.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# # Modify the Y-tick labels to show latitude with "N"
ax1.set_xticklabels([])
ax1.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(17, 23.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax1.tick_params(axis='both', length=6, width=1.6)
# Second subplot: ax2
ax1.set_title('(a) Ferrier', fontsize=18, fontweight='bold')
# Add colorbars for both plots
# cbar1 = plt.colorbar(pcm1, ax=[ax1], orientation='horizontal', shrink=0.5)
# cbar1.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar1.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar1.ax.set_position([0.15, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar1.ax.tick_params(length=2.5, width=1.2)
ax1.set_ylabel('lat', fontsize=18, fontweight='bold')

#################################
ax3 = fig.add_subplot(gs[0, 1], projection=ccrs.PlateCarree())
ax3.add_feature(orissa_feature)
pcm3 = ax3.contourf(lons1, lats1, dsc1, transform=ccrs.PlateCarree(), levels = lev1, cmap='GnBu', extend ='both')
ax3.set_xticks(np.arange(81, 88.1, 1))
ax3.set_yticks(np.arange(17, 23.1, 1))
ax3.set_xlim([81, 88])
ax3.set_ylim([17, 23])
# Modify the X-tick labels to show longitude with "E"
# ax3.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(81, 88.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# # Modify the Y-tick labels to show latitude with "N"
# ax3.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(17, 23.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax3.set_xticklabels([])
ax3.set_yticklabels([])
ax3.tick_params(axis='both', length=6, width=1.6)
# Second subplot: ax2
ax3.set_title('(b) Milbrandt', fontsize=18, fontweight='bold')
# Add colorbars for both plots
# cbar1 = plt.colorbar(pcm3, ax=[ax3], orientation='horizontal', shrink=0.5)
# cbar1.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar1.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar1.ax.set_position([0.15, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar1.ax.tick_params(length=2.5, width=1.2)
#ax3.set_ylabel('lat')
########################
ax5 = fig.add_subplot(gs[1, 0], projection=ccrs.PlateCarree())
ax5.add_feature(orissa_feature)
pcm5 = ax5.contourf(lons1, lats1, dse1, transform=ccrs.PlateCarree(), levels = lev1, cmap='GnBu', extend ='both')
ax5.set_xticks(np.arange(81, 88.1, 1))
ax5.set_yticks(np.arange(17, 23.1, 1))
ax5.set_xlim([81, 88])
ax5.set_ylim([17, 23])
# Modify the X-tick labels to show longitude with "E"
ax5.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(81, 88.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# Modify the Y-tick labels to show latitude with "N"
ax5.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(17, 23.1, 1)], fontsize=18, fontweight='bold', rotation=46)
# ax5.set_xticklabels([])
# ax5.set_yticklabels([])
ax5.tick_params(axis='both', length=6, width=1.6)
# Second subplot: ax2
ax5.set_title('(d) Morrison', fontsize=18, fontweight='bold')
# Add colorbars for both plots
# cbar1 = plt.colorbar(pcm5, ax=[ax5], orientation='horizontal', shrink=0.5)
# cbar1.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar1.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar1.ax.set_position([0.15, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar1.ax.tick_params(length=2.5, width=1.2)
ax5.set_ylabel('lat', fontsize=18, fontweight='bold')
ax5.set_xlabel('lon', fontsize=18, fontweight='bold')
###########################
ax7 = fig.add_subplot(gs[0, 2], projection=ccrs.PlateCarree())
ax7.add_feature(orissa_feature)
pcm7 = ax7.contourf(lons1, lats1, dsg1, transform=ccrs.PlateCarree(), levels = lev1, cmap='GnBu', extend ='both')
ax7.set_xticks(np.arange(81, 88.1, 1))
ax7.set_yticks(np.arange(17, 23.1, 1))
ax7.set_xlim([81, 88])
ax7.set_ylim([17, 23])
# # Modify the X-tick labels to show longitude with "E"
# ax7.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(81, 88.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# # Modify the Y-tick labels to show latitude with "N"
# ax7.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(17, 23.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax7.tick_params(axis='both', length=6, width=1.6)
# Second subplot: ax2
ax7.set_xticklabels([])
ax7.set_yticklabels([])
ax7.set_title('(c) Thomson', fontsize=18, fontweight='bold')
# Add colorbars for both plots
# cbar1 = plt.colorbar(pcm7, ax=[ax7], orientation='horizontal', shrink=0.5)
# cbar1.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar1.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar1.ax.set_position([0.15, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar1.ax.tick_params(length=2.5, width=1.2)
#ax7.set_ylabel('lat')
################################
ax9 = fig.add_subplot(gs[1, 1], projection=ccrs.PlateCarree())
ax9.add_feature(orissa_feature)
pcm9 = ax9.contourf(lons1, lats1, dsi1, transform=ccrs.PlateCarree(), levels = lev1, cmap='GnBu', extend ='both')
ax9.set_xticks(np.arange(81, 88.1, 1))
ax9.set_yticks(np.arange(17, 23.1, 1))
ax9.set_xlim([81, 88])
ax9.set_ylim([17, 23])
# Modify the X-tick labels to show longitude with "E"
ax9.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(81, 88.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# Modify the Y-tick labels to show latitude with "N"
# ax9.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(17, 23.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax9.set_yticklabels([])
ax9.tick_params(axis='both', length=6, width=1.6)
# Second subplot: ax2
ax9.set_title('(e) Wsm6', fontsize=18, fontweight='bold')
# Add colorbars for both plots
# cbar1 = plt.colorbar(pcm9, ax=[ax9], orientation='horizontal', shrink=0.5)
# cbar1.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar1.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar1.ax.set_position([0.15, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar1.ax.tick_params(length=2.5, width=1.2)
# ax9.set_ylabel('lat')
ax9.set_xlabel('lon', fontsize=18, fontweight='bold')
########################################
ax11 = fig.add_subplot(gs[1, 2], projection=ccrs.PlateCarree())
ax11.add_feature(orissa_feature)
pcm11 = ax11.contourf(lons11, lats11, ds1, transform=ccrs.PlateCarree(), levels = lev1, cmap='GnBu', extend ='both')
ax11.set_xticks(np.arange(81, 88.1, 1))
ax11.set_yticks(np.arange(17, 23.1, 1))
ax11.set_xlim([81, 88])
ax11.set_ylim([17, 23])
# Modify the X-tick labels to show longitude with "E"
ax11.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(81, 88.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# Modify the Y-tick labels to show latitude with "N"
# ax11.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(17, 23.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax11.tick_params(axis='both', length=6, width=1.6)
ax11.set_yticklabels([])
# Second subplot: ax2
ax11.set_title('(f) GPM', fontsize=18, fontweight='bold')
# Add colorbars for both plots
cbar1 = plt.colorbar(pcm11, ax=[ax1, ax3, ax5, ax7, ax9, ax11], orientation='horizontal', shrink=0.5)
cbar1.set_label('precipitation (mm)', fontsize=19, fontweight='bold')
cbar1.ax.tick_params(labelsize=14)  # Adjust tick label size
cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# Adjust the position and size of the second colorbar (cbar2)
cbar1.ax.set_position([0.31, 0.00001, 0.42, 0.3])  # Left, Bottom, Width, Height
cbar1.ax.tick_params(length=2.5, width=1.2)
# ax11.set_ylabel('lat')
ax11.set_xlabel('lon', fontsize=18, fontweight='bold')


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
plt.tight_layout()
plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/precipitation_orissa.png', dpi=500, bbox_inches='tight')
plt.show()




# Create the plot with Cartopy
fig = plt.figure(figsize=(23, 21))
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], hspace=0.2, wspace=0.0001)


ax2 = fig.add_subplot(gs[0, 0], projection=ccrs.PlateCarree())
ax2.add_feature(india_feature)
pcm2 = ax2.contourf(lons2, lats2, dsb1, transform=ccrs.PlateCarree(), levels = lev2, cmap='GnBu', extend ='both')
ax2.set_xticks(np.arange(83, 89.1, 1))
ax2.set_yticks(np.arange(21, 26.1, 1))
ax2.set_xlim([83, 88])
ax2.set_ylim([21, 26])
ax2.tick_params(axis='both', length=6, width=1.6)
# Modify the X-tick labels to show longitude with "E"
# ax2.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(83, 89.1, 1)], fontsize=18, fontweight='bold', rotation=0)
ax2.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 26.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax2.set_xticklabels([])
ax2.set_title('(a) Ferrier', fontsize=18, fontweight='bold')
# cbar2 = plt.colorbar(pcm2, ax=[ax2], orientation='horizontal', shrink=0.5)
# cbar2.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar2.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar2.ax.set_position([0.56, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar2.ax.tick_params(length=2.5, width=1.2)
ax2.set_ylabel('lat', fontsize=18, fontweight='bold')
#############
# Second subplot: ax4
ax4 = fig.add_subplot(gs[0, 1], projection=ccrs.PlateCarree())
ax4.add_feature(india_feature)
pcm4 = ax4.contourf(lons2, lats2, dsd1, transform=ccrs.PlateCarree(), levels = lev2, cmap='GnBu', extend ='both')
ax4.set_xticks(np.arange(83, 89.1, 1))
ax4.set_yticks(np.arange(21, 26.1, 1))
ax4.set_xlim([83, 88])
ax4.set_ylim([21, 26])
ax4.tick_params(axis='both', length=6, width=1.6)
# Modify the X-tick labels to show longitude with "E"
# ax4.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(83, 89.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# ax4.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 26.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax4.set_title('(b) Milbrandt', fontsize=18, fontweight='bold')
ax4.set_xticklabels([])
ax4.set_yticklabels([])
# cbar2 = plt.colorbar(pcm4, ax=[ax4], orientation='horizontal', shrink=0.5)
# cbar2.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar2.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar2.ax.set_position([0.56, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar2.ax.tick_params(length=2.5, width=1.2)
# ax4.set_ylabel('lat')
#################
# Second subplot: ax6
ax6 = fig.add_subplot(gs[1, 0], projection=ccrs.PlateCarree())
ax6.add_feature(india_feature)
pcm6 = ax6.contourf(lons2, lats2, dsf1, transform=ccrs.PlateCarree(), levels = lev2, cmap='GnBu', extend ='both')
ax6.set_xticks(np.arange(83, 89.1, 1))
ax6.set_yticks(np.arange(21, 26.1, 1))
ax6.set_xlim([83, 88])
ax6.set_ylim([21, 26])
ax6.tick_params(axis='both', length=6, width=1.6)
# Modify the X-tick labels to show longitude with "E"
ax6.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(83, 89.1, 1)], fontsize=18, fontweight='bold', rotation=0)
ax6.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 26.1, 1)], fontsize=18, fontweight='bold', rotation=46)
# ax6.set_xticklabels([])
# ax6.set_yticklabels([])
ax6.set_title('(d) Morrison', fontsize=18, fontweight='bold')
# cbar2 = plt.colorbar(pcm6, ax=[ax6], orientation='horizontal', shrink=0.5)
# cbar2.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar2.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar2.ax.set_position([0.56, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar2.ax.tick_params(length=2.5, width=1.2)
ax6.set_ylabel('lat', fontsize=18, fontweight='bold')
ax6.set_xlabel('lon', fontsize=18, fontweight='bold')
#######################
# Second subplot: ax8
ax8 = fig.add_subplot(gs[0, 2], projection=ccrs.PlateCarree())
ax8.add_feature(india_feature)
pcm8 = ax8.contourf(lons2, lats2, dsh1, transform=ccrs.PlateCarree(), levels = lev2, cmap='GnBu', extend ='both')
ax8.set_xticks(np.arange(83, 89.1, 1))
ax8.set_yticks(np.arange(21, 26.1, 1))
ax8.set_xlim([83, 88])
ax8.set_ylim([21, 26])
ax8.tick_params(axis='both', length=6, width=1.6)
# Modify the X-tick labels to show longitude with "E"
# ax8.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(83, 89.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# ax8.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 26.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax8.set_xticklabels([])
ax8.set_yticklabels([])
ax8.set_title('(c) Thomson', fontsize=18, fontweight='bold')
# cbar2 = plt.colorbar(pcm8, ax=[ax8], orientation='horizontal', shrink=0.5)
# cbar2.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar2.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar2.ax.set_position([0.56, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar2.ax.tick_params(length=2.5, width=1.2)
#ax8.set_ylabel('lat')
##############################################
# Second subplot: ax10
ax10 = fig.add_subplot(gs[1, 1], projection=ccrs.PlateCarree())
ax10.add_feature(india_feature)
pcm10 = ax10.contourf(lons2, lats2, dsj1, transform=ccrs.PlateCarree(), levels = lev2, cmap='GnBu', extend ='both')
ax10.set_xticks(np.arange(83, 89.1, 1))
ax10.set_yticks(np.arange(21, 26.1, 1))
ax10.set_xlim([83, 88])
ax10.set_ylim([21, 26])
ax10.tick_params(axis='both', length=6, width=1.6)
# Modify the X-tick labels to show longitude with "E"
ax10.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(83, 89.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# ax10.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 26.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax10.set_yticklabels([])
ax10.set_title('(e) Wsm6', fontsize=18, fontweight='bold')
# cbar2 = plt.colorbar(pcm10, ax=[ax10], orientation='horizontal', shrink=0.5)
# cbar2.set_label('precipitation (mm)', fontsize=9, fontweight='bold')
# cbar2.ax.tick_params(labelsize=14)  # Adjust tick label size
# cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# # Adjust the position and size of the second colorbar (cbar2)
# cbar2.ax.set_position([0.56, 0.00001, 0.3, 0.3])  # Left, Bottom, Width, Height
# cbar2.ax.tick_params(length=2.5, width=1.2)
ax10.set_xlabel('lon', fontsize=18, fontweight='bold')
############################
# Second subplot: ax12
ax12 = fig.add_subplot(gs[1, 2], projection=ccrs.PlateCarree())
ax12.add_feature(india_feature)
pcm12 = ax12.contourf(lons22, lats22, ds2, transform=ccrs.PlateCarree(), levels = lev2, cmap='GnBu', extend ='both')
ax12.set_xticks(np.arange(83, 89.1, 1))
ax12.set_yticks(np.arange(21, 26.1, 1))
ax12.set_xlim([83, 88])
ax12.set_ylim([21, 26])
ax12.tick_params(axis='both', length=6, width=1.6)
# Modify the X-tick labels to show longitude with "E"
ax12.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(83, 89.1, 1)], fontsize=18, fontweight='bold', rotation=0)
# ax12.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 26.1, 1)], fontsize=18, fontweight='bold', rotation=46)
ax12.set_yticklabels([])
ax12.set_title('(f) GPM', fontsize=18, fontweight='bold')
cbar2 = plt.colorbar(pcm12, ax=[ax2, ax4, ax6, ax8, ax10, ax12], orientation='horizontal', shrink=0.5)
cbar2.set_label('precipitation (mm)', fontsize=19, fontweight='bold')
cbar2.ax.tick_params(labelsize=14)  # Adjust tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels
# Adjust the position and size of the second colorbar (cbar2)
cbar2.ax.set_position([0.31, 0.00001, 0.42, 0.3])  # Left, Bottom, Width, Height
cbar2.ax.tick_params(length=2.5, width=1.2)
ax12.set_xlabel('lon', fontsize=18, fontweight='bold')







plt.rcParams.update({
    "font.weight": "bold",          # Set the default font weight to bold
    "axes.labelweight": "bold",     # Axis label font weight
    'xtick.labelsize': 18,          # X-axis tick label size
    'ytick.labelsize': 18,          # Y-axis tick label size
    "axes.linewidth": 1,            # Line width for the axes
    "patch.linewidth": 1,           # Line width for patches (e.g., circles, rectangles)
    'xtick.major.size': 16,         # Major tick size for X-axis
    'ytick.major.size': 16,         # Major tick size for Y-axis
    'xtick.major.width': 2,         # Major tick width for X-axis
    'ytick.major.width': 2,         # Major tick width for Y-axis
    'axes.titlesize': 20,           # Font size for subplot (ax1, ax2) titles
    'axes.titleweight': 'bold',     # Font weight for subplot titles
    'figure.titlesize': 16,         # Font size for the overall figure title (suptitle)
    'figure.titleweight': 'bold',   # Font weight for the overall figure title
})
plt.tight_layout()
plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/precipitation_jharkhand.png', dpi=500, bbox_inches='tight')

plt.show()



