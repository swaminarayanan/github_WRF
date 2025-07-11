
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.ticker import FuncFormatter
import metpy.calc
from metpy.units import units
# from metpy.calc import unrotate_winds
import iris.analysis.cartography
import iris
import iris.plot as iplt
# Load the dataset
#ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/20200303.nc')
trr1 = xr.open_dataset(r'/media/lab/My Passport/hail/ncei_terrain data/GEBCO_01_Mar_2025_34026bc640b3/gebco_2024_n25.0_s15.0_w80.0_e90.0.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/potent_vort2020.nc')
mds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
db1 = ds1.sel(latitude=slice(22.6, 23.4), longitude=slice(80, 90))
tbr1 = trr1.sel(lat=slice(22.6, 23.4), lon=slice(80, 90))
mdb1 = mds1.sel(lat=slice(22.6, 23.4), lon=slice(80, 90), lev=slice(1000, 700))
pb1 = ds2.sel(latitude=slice(23.4, 22.6), longitude=slice(80, 90))
latb = trr1['lat'].values
lonb = trr1['lon'].values
theta = db1['t'].mean(dim=['latitude']).isel(valid_time=8).squeeze()#-273.16 # Fixed dataset reference
dub1 = db1['u'].mean(dim=['latitude']).isel(valid_time=8).squeeze()
dvb1 = db1['v'].mean(dim=['latitude']).isel(valid_time=8).squeeze()
tbr1 = tbr1['elevation'].mean(dim=['lat']).values#.sel(lat=slice(22.0, 22.5), lon=slice(80, 90))
pb1 = pb1['pv'].mean(dim=['latitude']).isel(valid_time=8).squeeze().values / 1*1.0e+06
hlb1 = mdb1['qhail'].mean(dim=['lat']).isel(time=16).squeeze() / 1*1.0e+05
levb1, lonb1 = dub1['pressure_level'].values, dub1['longitude'].values
levb2, lonb2 = hlb1['lev'].values, hlb1['lon'].values
###########################2 nd plot
da1 = ds1.sel(latitude=slice(15, 25), longitude=slice(84.8, 85.4), pressure_level=slice(1000, 700))
tar1 = trr1.sel(lat=slice(15, 25), lon=slice(84.8, 85.4))
mda1 = mds1.sel(lat=slice(15, 25), lon=slice(84.3, 85.2), lev=slice(1000, 700))
pa1 = ds2.sel(latitude=slice(25, 15), longitude=slice(84.8, 85.4), pressure_level=slice(1000, 700))
lata = tar1['lat'].values
lona = tar1['lon'].values
theta = da1['t'].mean(dim=['longitude']).isel(valid_time=8).squeeze()#-273.16 # Fixed dataset reference
dua1 = da1['u'].mean(dim=['longitude']).isel(valid_time=8).squeeze()
dva1 = da1['v'].mean(dim=['longitude']).isel(valid_time=8).squeeze()
tar1 = tar1['elevation'].mean(dim=['lon']).values#.sel(lat=slice(22.0, 22.5), lon=slice(84.8, 85.4))
pa1 = pa1['pv'].mean(dim=['longitude']).isel(valid_time=8).squeeze().values / 1*1.0e+06
hla1 = mda1['qhail'].mean(dim=['lon']).isel(time=16).squeeze() / 1*1.0e+05
leva1, lata1 = dua1['pressure_level'].values, dua1['latitude'].values
leva2, lata2 = hla1['lev'].values, hla1['lat'].values

#############################
def altitude_to_hpa(altitude_m):
    # Constants
    P0 = 1013.25  # Sea level pressure in hPa
    L = 0.0065    # Temperature lapse rate in K/m
    T0 = 288.15   # Standard temperature at sea level in K
    g = 9.80665   # Gravity in m/s²
    M = 0.0289644 # Molar mass of Earth's air in kg/mol
    R = 8.31447   # Universal gas constant in J/(mol·K)
    # Calculate pressure using the barometric formula
    pressure_hpa = P0 * (1 - (L * altitude_m) / T0) ** ((g * M) / (R * L))
    return pressure_hpa
# Example usage:
altitude = tbr1  # meters
tbr1 = altitude_to_hpa(altitude)
lonb_grid1, levb_grid1 = np.meshgrid(lonb1, levb1)
ub1, vb1 = dub1.values, dvb1.values
lonb_grid1_s = lonb_grid1[::, ::]
levb_grid1_s = levb_grid1[::, ::]
ub1_s = ub1[::, ::]
vb1_s = vb1[::, ::]
##############################2 nd plot
# Example usage:
altitude1 = tar1  # meters
tar1 = altitude_to_hpa(altitude1)
tar1 = np.where(tar1>1000, 1000, tar1)
lona_grid1, leva_grid1 = np.meshgrid(lata1, leva1)
ua1, va1 = dua1.values, dva1.values
lona_grid1_s = lona_grid1[::, ::]
leva_grid1_s = leva_grid1[::, ::]
ua1_s = ua1[::, ::]
va1_s = va1[::, ::]
##################################
fig = plt.figure(figsize=(22, 16))
gs = gridspec.GridSpec(2, 1, wspace=0.15, hspace=0.305)
ax1 = fig.add_subplot(gs[0, 0])#, projection=ccrs.PlateCarree())
pcm1 = ax1.contourf(lonb1, levb1, pb1, cmap='jet', 
                    levels=np.linspace(-0.8, 0.8, 10), extend='both')
hail1 = ax1.contour(lonb2, levb2, hlb1, colors='maroon', linewidths=1, 
                          levels=np.linspace(0.1, hlb1.max(), 8))
ax1.clabel(hail1, inline=True, fontsize=15, fmt='%1.0f')
quiverb1 = ax1.quiver(lonb_grid1_s, levb_grid1_s, ub1_s, vb1_s, scale=200, width=0.001, headlength=5, headwidth=4, color="k")#, transform=ccrs.PlateCarree())

ax1.set_xlabel("lon", fontsize=24)
ax1.set_ylabel("pressure level (hpa)", fontsize=24)
ax1.set_yticks(np.arange(700, 1001, 50))  # Ensure the range is within actual data limits
ax1.set_xticks(np.arange(80, 90.1, 1))  # Ensure the range is within actual data limits
ax1.invert_yaxis()# ax1.set_xticks(np.arange(82.5, 85.1, 0.5))#, crs=ccrs.PlateCarree())
ax1.tick_params(axis="both", labelsize=22)
ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}°E"))
# ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
ax1.xaxis.set_tick_params(rotation=45)
ax1.yaxis.set_tick_params(rotation=45)
# ax2 = ax1.twinx()
# ax2.contourf(lon, lat, ds.values, cmap='jet')
ax1.plot(lonb, tbr1, color='maroon')
ax1.fill_between(lonb, tbr1, tbr1.max() + 0.5, color='grey', alpha=0.99)  # alpha controls transparency# ax2.set_xticks(np.arange(80, 90.1, 1))
ax1.set_ylim([1000, 700])  # Adjust top axis limits to match top axis data range
ax1.set_xlim([80, 90])  # Adjust top axis limits to match top axis data range
# ax1.quiverkey(quiver1, 0.8, 1.05, 10, "10 m/s", labelpos="E",
#               coordinates="axes", fontproperties={"size": 12})
# ax1.invert_yaxis()
cbar1 = plt.colorbar(pcm1, ax=[ax1], orientation='vertical', shrink=0.7, format="%.1f")
cbar1.set_label(r'Potential Vorticity (K $\mathrm{m^2}$ $\mathrm{kg^{-1}}$ $\mathrm{s^{-1}}$)', fontsize=18)
cbar1.ax.text(0.69, 1.05,r'$\times   10^{-6}$', fontsize=25, fontweight='bold', ha='center', transform=cbar1.ax.transAxes)
cbar1.ax.tick_params(labelsize=20)  # Set tick label size
cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
cbar1.ax.set_position([0.765, 0.185, 0.65, 0.6])  # Adjust colorbar position: [left, bottom, width, height]
ax1.text(81.6, 980, "Terrain height in hpa", fontsize=20, color='white', fontweight='bold')
ax1.tick_params(axis='both', length=5, width=1.2, labelsize=18)
#############################
ax2 = fig.add_subplot(gs[1, 0])#, projection=ccrs.PlateCarree())
pcma1 = ax2.contourf(lata1, leva1, pa1, cmap='jet', 
                    levels=np.linspace(-0.8, 0.8, 10), extend='both')
haila1 = ax2.contour(lata2, leva2, hla1, colors='maroon', linewidths=1, 
                          levels=np.linspace(0.2, hla1.max(), 4))
ax2.clabel(haila1, inline=True, fontsize=15, fmt='%1.0f')
quivera1 = ax2.quiver(lona_grid1_s, leva_grid1_s, ua1_s, va1_s, scale=200, width=0.001, headlength=5, headwidth=4, color="k")#, transform=ccrs.PlateCarree())

ax2.set_xlabel("lat", fontsize=24)
ax2.set_ylabel("pressure level (hpa)", fontsize=24)
ax2.set_yticks(np.arange(700, 1001, 50))  # Ensure the range is within actual data limits
ax2.set_xticks(np.arange(15, 25.1, 1))  # Ensure the range is within actual data limits
ax2.invert_yaxis()# ax2.set_xticks(np.arange(82.5, 85.1, 0.5))#, crs=ccrs.PlateCarree())
ax2.tick_params(axis="both", labelsize=22)
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}°N"))
# ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
ax2.xaxis.set_tick_params(rotation=45)
ax2.yaxis.set_tick_params(rotation=45)
# ax2 = ax2.twinx()
# ax2.contourf(lon, lat, ds.values, cmap='jet')
ax2.plot(lata, tar1, color='maroon')
ax2.fill_between(lata, tar1, tar1.max() + 0.5, color='grey', alpha=0.99)  # alpha controls transparency# ax2.set_xticks(np.arange(84.8, 85.4.1, 1))
ax2.set_ylim([1000, 700])  # Adjust top axis limits to match top axis data range
ax2.set_xlim([15, 25])  # Adjust top axis limits to match top axis data range
# ax2.quiverkey(quiver1, 0.8, 1.05, 10, "10 m/s", labelpos="E",
#               coordinates="axes", fontproperties={"size": 12})
# ax2.invert_yaxis()
cbar2 = plt.colorbar(pcma1, ax=[ax2], orientation='vertical', shrink=0.7, format="%.1f")
cbar2.set_label(r'Potential Vorticity (K $\mathrm{m^2}$ $\mathrm{kg^{-1}}$ $\mathrm{s^{-1}}$)', fontsize=18)
cbar2.ax.text(0.69, 1.05,r'$\times   10^{-6}$', fontsize=25, fontweight='bold', ha='center', transform=cbar2.ax.transAxes)
cbar2.ax.tick_params(labelsize=20)  # Set tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
cbar2.ax.set_position([0.765, 0.185, 0.65, 0.6])  # Adjust colorbar position: [left, bottom, width, height]
ax2.text(21.6, 990, "Terrain height in hpa", fontsize=20, color='white', fontweight='bold')
# cbar2.set_position([0.8, 0.94, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# Colorbar on the left side
# cbar2 = plt.colorbar(quiver1, ax=ax2, orientation='vertical', shrink=0.7)
# cbar2.set_label(r'Potential Vorticity (K $\mathrm{m^2}$ $\mathrm{kg^{-1}}$ $\mathrm{s^{-1}}$)', fontsize=22)
# cbar2.ax.text(0.5, 1.05, r'$\times   10^{-6}$', fontsize=25, fontweight='bold', ha='center', transform=cbar2.ax.transAxes)
# cbar2.ax.tick_params(labelsize=20)  # Set tick label size
# cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
# cbar2.ax.set_position([0.05, 0.185, 0.03, 0.6])  # Adjust colorbar position: [left, bottom, width, height]
ax2.tick_params(axis='both', length=5, width=1.2, labelsize=18)
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 19,
    'ytick.major.size': 19,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 16,  # For axes titles
    'figure.titlesize': 18  # For overall figure title
})
# plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/lon_lat_crossectional_orography1.png', dpi=500)
plt.show()











############# modified oorographic lifting wind flow

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.ticker import FuncFormatter
import metpy.calc
from metpy.units import units
# from metpy.calc import unrotate_winds
dsa = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/20200303.nc')
trr = xr.open_dataset(r'/media/lab/My Passport/hail/ncei_terrain data/GEBCO_01_Mar_2025_34026bc640b3/gebco_2024_n25.0_s15.0_w80.0_e90.0.nc')
pva = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/potent_vort2020.nc')
mds = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')

ds1 = dsa.sel(latitude=slice(15, 25), longitude=slice(84.75, 84.75))
trr1 = trr.sel(lat=slice(15, 25), lon=slice(84.6, 85.4))
mds1 = mds.sel(lat=slice(15, 25), lon=slice(84.9, 85.5), lev=slice(1000, 700))
pv1 = pva.sel(latitude=slice(25, 15), longitude=slice(84.6, 85.5))
lata = trr1['lat'].values
lona = trr1['lon'].values
theta1 = dsa['t'].mean(dim=['longitude']).isel(valid_time=6).squeeze()#-273.16 # Fixed dataset reference
a = ds1['u'].mean(dim=['longitude']).isel(valid_time=6).squeeze()
b = ds1['v'].mean(dim=['longitude']).isel(valid_time=6).squeeze()
c = ds1['w'].mean(dim=['longitude']).isel(valid_time=6).squeeze() * 10
c1 = a + b 
dua1 = c1
dva1 = c 
tbr1 = trr1['elevation'].mean(dim=['lon']).values#.sel(lat=slice(22.0, 22.5), lon=slice(15, 25))
pb1 = pv1['pv'].mean(dim=['longitude']).isel(valid_time=6).squeeze().values / 1*1.0e+06
hl1 = mds1['qhail'].mean(dim=['lon']).isel(time=16).squeeze() / 1*1.0e+05
leva1, lona1 = c1['pressure_level'].values, c1['latitude'].values
leva2, lona2 = hl1['lev'].values, hl1['lat'].values
def altitude_to_hpa(altitude_m):
    # Constants
    P0 = 1013.25  # Sea level pressure in hPa
    L = 0.0065    # Temperature lapse rate in K/m
    T0 = 288.15   # Standard temperature at sea level in K
    g = 9.80665   # Gravity in m/s²
    M = 0.0289644 # Molar mass of Earth's air in kg/mol
    R = 8.31447   # Universal gas constant in J/(mol·K)
    # Calculate pressure using the barometric formula
    pressure_hpa = P0 * (1 - (L * altitude_m) / T0) ** ((g * M) / (R * L))
    return pressure_hpa
# Example usage:
altitude1 = tbr1  # meters
tbr1 = altitude_to_hpa(altitude1)

lona_grid1, leva_grid1 = np.meshgrid(lona1, leva1)
ua1, va1 = dua1.values, dva1.values
lona_grid1_s = lona_grid1[::, ::]
leva_grid1_s = leva_grid1[::, ::]
ua1_s = ua1[::, ::]
va1_s = va1[::, ::]

ds2 = dsa.sel(latitude=slice(22.5, 22.5), longitude=slice(80, 90))
trr2 = trr.sel(lat=slice(23.3, 23.4), lon=slice(80, 90))
mds2 = mds.sel(lat=slice(22.75, 23.5), lon=slice(80, 90), lev=slice(1000, 700))
pv2 = pva.sel(latitude=slice(23.0, 23.0), longitude=slice(80, 90))
latb = trr2['lat'].values
lonb = trr2['lon'].values
# theta2 = dsa['t'].mean(dim=['latitude']).isel(valid_time=6).squeeze()#-273.16 # Fixed dataset reference

d = ds2['u'].mean(dim=['latitude']).isel(valid_time=6).squeeze()
e = ds2['v'].mean(dim=['latitude']).isel(valid_time=6).squeeze()
f = ds2['w'].mean(dim=['latitude']).isel(valid_time=6).squeeze() * 10
c2 = d + e 
dua2 = c2
dva2 = f

tbr2 = trr2['elevation'].mean(dim=['lat']).values#.sel(lat=slice(22.0, 22.5), lon=slice(80, 90))
pb2 = pv2['pv'].mean(dim=['latitude']).isel(valid_time=6).squeeze().values / 1*1.0e+06
hl2 = mds2['qhail'].mean(dim=['lat']).isel(time=16).squeeze() / 1*1.0e+05
levb1, lonb1 = dua2['pressure_level'].values, dua2['longitude'].values
levb2, lonb2 = hl2['lev'].values, hl2['lon'].values

altitude2 = tbr2  # meters
tbr2 = altitude_to_hpa(altitude2)

lonb_grid1, levb_grid1 = np.meshgrid(lonb1, levb1)
ua2, va2 = dua2.values, dva2.values
lonb_grid1_s = lonb_grid1[::, ::]
levb_grid1_s = levb_grid1[::, ::]
ub1_s = ua2[::, ::]
vb1_s = va2[::, ::]

fig = plt.figure(figsize=(22, 16))
gs = gridspec.GridSpec(2, 1, wspace=0.15, hspace=0.305)
ax1 = fig.add_subplot(gs[0, 0])#, projection=ccrs.PlateCarree())
pcm1 = ax1.contourf(lona1, leva1, pb1, cmap='jet', 
                    levels=np.linspace(-0.8, 0.8, 10), extend='both')
hail1 = ax1.contour(lona2, leva2, hl1, colors='maroon', linewidths=1, 
                          levels=np.linspace(1, hl2.max(), 8))
ax1.clabel(hail1, inline=True, fontsize=15, fmt='%1.0f')
quivera1 = ax1.quiver(lona_grid1_s, leva_grid1_s, ua1_s, va1_s, scale=300, width=0.001, headlength=5, headwidth=4, color="k")#, transform=ccrs.PlateCarree())

ax1.set_xlabel("lat", fontsize=24)
ax1.set_ylabel("pressure level (hpa)", fontsize=24)
ax1.set_yticks(np.arange(700, 1001, 50))  # Ensure the range is within actual data limits
ax1.set_xticks(np.arange(15, 25.1, 1))  # Ensure the range is within actual data limits
ax1.invert_yaxis()# ax1.set_xticks(np.arange(82.5, 85.1, 0.5))#, crs=ccrs.PlateCarree())
ax1.tick_params(axis="both", labelsize=22)
ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}°N"))
# ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
ax1.xaxis.set_tick_params(rotation=45)
ax1.yaxis.set_tick_params(rotation=45)
# ax2 = ax1.twinx()
# ax2.contourf(lon, lat, ds.values, cmap='jet')
ax1.plot(lata, tbr1, color='maroon')
ax1.fill_between(lata, tbr1, tbr1.max() + 0.5, color='grey', alpha=0.99)  # alpha controls transparency# ax2.set_xticks(np.arange(15, 25.1, 1))
ax1.set_ylim([1000, 700])  # Adjust top axis limits to match top axis data range
ax1.set_xlim([15, 25])  # Adjust top axis limits to match top axis data range
# ax1.quiverkey(quiver1, 0.8, 1.05, 10, "10 m/s", labelpos="E",
#               coordinates="axes", fontproperties={"size": 12})
# # # ax1.invert_yaxis()
# cbar1 = plt.colorbar(pcm1, ax=[ax1], orientation='vertical', shrink=0.7, format="%.1f")
# cbar1.set_label(r'Potential Vorticity (K $\mathrm{m^2}$ $\mathrm{kg^{-1}}$ $\mathrm{s^{-1}}$)', fontsize=18)
# cbar1.ax.text(0.69, 1.05,r'$\times   10^{-6}$', fontsize=25, fontweight='bold', ha='center', transform=cbar1.ax.transAxes)
# cbar1.ax.tick_params(labelsize=20)  # Set tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
# cbar1.ax.set_position([0.771, 0.56, 0.35, 0.3])  # Adjust colorbar position: [left, bottom, width, height]
ax1.text(21.9, 991, "Terrain height in hpa", fontsize=20, color='white', fontweight='bold')
ax1.tick_params(axis='both', length=5, width=1.2, labelsize=18)

# fig = plt.figure(figsize=(22, 16))
# gs = gridspec.GridSpec(2, 1, wspace=0.15, hspace=0.305)
ax2 = fig.add_subplot(gs[1, 0])#, projection=ccrs.PlateCarree())
pcm2 = ax2.contourf(lonb1, levb1, pb2, cmap='jet', 
                    levels=np.linspace(-0.8, 0.8, 10), extend='both')
hail1 = ax2.contour(lonb2, levb2, hl2, colors='maroon', linewidths=1, 
                          levels=np.linspace(1, hl2.max(), 8))
ax2.clabel(hail1, inline=True, fontsize=15, fmt='%1.0f')
quiverb1 = ax2.quiver(lonb_grid1_s, levb_grid1_s, ub1_s, vb1_s, scale=300, width=0.001, headlength=5, headwidth=4, color="k")#, transform=ccrs.PlateCarree())

ax2.set_xlabel("lon", fontsize=24)
ax2.set_ylabel("pressure level (hpa)", fontsize=24)
ax2.set_yticks(np.arange(700, 1001, 50))  # Ensure the range is within actual data limits
ax2.set_xticks(np.arange(80, 90.1, 1))  # Ensure the range is within actual data limits
ax2.invert_yaxis()# ax2.set_xticks(np.arange(82.5, 85.1, 0.5))#, crs=ccrs.PlateCarree())
ax2.tick_params(axis="both", labelsize=22)
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}°E"))
# ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
ax2.xaxis.set_tick_params(rotation=45)
ax2.yaxis.set_tick_params(rotation=45)
# ax2 = ax2.twinx()
# ax2.contourf(lon, lat, ds.values, cmap='jet')
ax2.plot(lonb, tbr2, color='maroon')
ax2.fill_between(lonb, tbr2, tbr2.max() + 0.5, color='grey', alpha=0.99)  # alpha controls transparency# ax2.set_xticks(np.arange(80, 90.1, 1))
ax2.set_ylim([1000, 700])  # Adjust top axis limits to match top axis data range
ax2.set_xlim([80, 90])  # Adjust top axis limits to match top axis data range
# ax2.quiverkey(quiver1, 0.8, 1.05, 10, "10 m/s", labelpos="E",
#               coordinates="axes", fontproperties={"size": 12})
# # ax2.invert_yaxis()
cbar2 = plt.colorbar(pcm2, ax=[ax1, ax2], orientation='vertical', shrink=0.7, format="%.1f")
cbar2.set_label(r'Potential Vorticity (K $\mathrm{m^2}$ $\mathrm{kg^{-1}}$ $\mathrm{s^{-1}}$)', fontsize=18)
cbar2.ax.text(0.69, 1.05,r'$\times   10^{-6}$', fontsize=25, fontweight='bold', ha='center', transform=cbar2.ax.transAxes)
cbar2.ax.tick_params(labelsize=20)  # Set tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
cbar2.ax.set_position([0.765, 0.12, 0.35, 0.7])  # Adjust colorbar position: [left, bottom, width, height]
ax2.text(81.6, 980, "Terrain height in hpa", fontsize=20, color='white', fontweight='bold')
ax2.tick_params(axis='both', length=5, width=1.2, labelsize=18)


plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 19,
    'ytick.major.size': 19,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 16,  # For axes titles
    'figure.titlesize': 18  # For overall figure title
})
# plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/lon_lat_crossectional_orography1.png', dpi=500)
plt.show()





