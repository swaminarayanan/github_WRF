
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.ticker import FuncFormatter

# Load the dataset
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')

# Select the region of interest and calculate non-cumulative data
du1 = ds1['u'].sel(lev=250).isel(time=20).squeeze()
dv1 = ds1['v'].sel(lev=250).isel(time=20).squeeze()
du2 = ds2['u'].sel(lev=250).isel(time=17).squeeze()
dv2 = ds2['v'].sel(lev=250).isel(time=17).squeeze()
dt3 = ds1['hgt'].isel(time=20).squeeze()#-273.16
dt4 = ds2['hgt'].isel(time=17).squeeze()#-273.16 # Fixed dataset reference
dt = ds1['pblh'].isel(time=17).squeeze()#-273.16 # Fixed dataset reference

lat1, lon1 = du1['lat'].values, du1['lon'].values
lat2, lon2 = du2['lat'].values, du2['lon'].values
lon_grid1, lat_grid1 = np.meshgrid(lon1, lat1)
lon_grid2, lat_grid2 = np.meshgrid(lon2, lat2)

# Wind components
u1, v1 = du1.values, dv1.values
u2, v2 = du2.values, dv2.values

step = 35  # Adjust this to control the density of arrows
lon_grid1_s = lon_grid1[::step, ::step]
lat_grid1_s = lat_grid1[::step, ::step]
u1_s = u1[::step, ::step]
v1_s = v1[::step, ::step]

lon_grid2_s = lon_grid2[::step, ::step]
lat_grid2_s = lat_grid2[::step, ::step]
u2_s = u2[::step, ::step]
v2_s = v2[::step, ::step]
l = np.arange(0, 40, 5)
# Create the figure and grid specification
fig = plt.figure(figsize=(14, 6))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1], wspace=0.15)

# First subplot
ax1 = fig.add_subplot(gs[0, 0], projection=ccrs.PlateCarree())
contour1 = ax1.contourf(dt3['lon'], dt3['lat'], dt3, cmap='coolwarm', transform=ccrs.PlateCarree())
quiver1 = ax1.quiver(lon_grid1_s, lat_grid1_s, u1_s, v1_s, scale=560,
                     width=0.005, color="k", transform=ccrs.PlateCarree())
# ax1.set_title("Wind Direction 2019-03-15", fontsize=14, fontweight="bold")
ax1.add_feature(cfeature.COASTLINE, linewidth=0.8)
ax1.add_feature(cfeature.BORDERS, linestyle=":", linewidth=0.5)
ax1.add_feature(cfeature.STATES, linestyle=":", linewidth=0.5)
ax1.set_xlabel("Longitude", fontsize=12)
ax1.set_ylabel("Latitude", fontsize=12)
ax1.set_xticks(np.arange(np.min(lon1), np.max(lon1), 1), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(np.min(lat1), np.max(lat1), 1), crs=ccrs.PlateCarree())
ax1.tick_params(axis="both", labelsize=10)
ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.1f}°E"))
ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
ax1.xaxis.set_tick_params(rotation=45)
# ax1.quiverkey(quiver1, 0.8, 1.05, 10, "10 m/s", labelpos="E",
#               coordinates="axes", fontproperties={"size": 12})

# Second subplot
ax2 = fig.add_subplot(gs[0, 1], projection=ccrs.PlateCarree())
contour2 = ax2.contourf(dt4['lon'], dt4['lat'], dt4, cmap='coolwarm', transform=ccrs.PlateCarree())
quiver2 = ax2.quiver(lon_grid2_s, lat_grid2_s, u2_s, v2_s, scale=560,
                     width=0.005, color="k", transform=ccrs.PlateCarree())
# ax2.set_title("Wind Direction 2020-03-03", fontsize=14, fontweight="bold")
ax2.add_feature(cfeature.COASTLINE, linewidth=0.8)
ax2.add_feature(cfeature.BORDERS, linestyle=":", linewidth=0.5)
ax2.add_feature(cfeature.STATES, linestyle=":", linewidth=0.5)
ax2.set_xlabel("Longitude", fontsize=12)
# ax2.set_ylabel("Latitude", fontsize=12)
ax2.set_xticks(np.arange(np.min(lon2), np.max(lon2), 1), crs=ccrs.PlateCarree())
ax2.set_yticks(np.arange(np.min(lat2), np.max(lat2), 1), crs=ccrs.PlateCarree())
ax2.tick_params(axis="both", labelsize=10)
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.1f}°E"))
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
ax2.xaxis.set_tick_params(rotation=45)
ax2.set_yticklabels([])

# ax2.quiverkey(quiver2, 0.8, 1.05, 10, "10 m/s", labelpos="E",
#               coordinates="axes", fontproperties={"size": 12})

# Add a common colorbar
cbar = plt.colorbar(contour2, ax=[ax1, ax2], orientation='vertical', shrink=0.7, pad=0.02)
cbar.set_label('Terrain height (m)', fontsize=10, fontweight='bold')
cbar.ax.tick_params(labelsize=10)

# Add a common title
# p = plt.suptitle("Spatial Wind Direction Comparison", fontsize=16, fontweight="bold", y=0.95)
# p.set_position([0.45, 0.93, 0.3, 0.3])  # Left, Bottom, Width, Height

# Show the plot
plt.show()
