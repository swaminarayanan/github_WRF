
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
dsa1 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/20190421.nc')
trr = xr.open_dataset(r'/media/lab/My Passport/hail/ncei_terrain data/GEBCO_01_Mar_2025_34026bc640b3/gebco_2024_n25.0_s15.0_w80.0_e90.0.nc')
# pva1 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/potent_vort2020.nc')
mds1 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/20190421_ice_snow.nc')

dsa2 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/20200303.nc')
pva2 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/potent_vort2020.nc')
mds2 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/20200303_ice_snow.nc')


dsa1 = dsa1.sel(latitude=slice(21.4, 21.5), longitude=slice(80, 90))
trr1 = trr.sel(lat=slice(21.4, 21.5), lon=slice(80, 90))
mds1 = mds1.sel(latitude=slice(21.5, 21 ), longitude=slice(80, 90))
pv1 = mds1.sel(latitude=slice(21.5, 21), longitude=slice(80, 90))
lata = trr1['lat'].values
lona = trr1['lon'].values
# theta1 = dsa['t'].mean(dim=['latitude']).isel(valid_time=6).squeeze()#-273.16 # Fixed dataset reference
a = dsa1['u'].mean(dim=['latitude']).isel(valid_time=9).squeeze()
b = dsa1['v'].mean(dim=['latitude']).isel(valid_time=9).squeeze()
c = dsa1['w'].mean(dim=['latitude']).isel(valid_time=9).squeeze() * 10
c1 = a + b 
dua1 = c1/2
dva1 = c 

tbr1 = trr1['elevation'].mean(dim=['lat']).values#.sel(lat=slice(22.0, 22.5), lon=slice(15, 25))
pb1 = pv1['pv'].mean(dim=['latitude']).isel(valid_time=9).squeeze() / 1*1.0e+06
h1 = mds1['ciwc'].mean(dim=['latitude']).isel(valid_time=9).squeeze() / 1*1.0e+05
h2 = mds1['cswc'].mean(dim=['latitude']).isel(valid_time=9).squeeze() / 1*1.0e+05
hl1 = h1 + h2
leva1, lona1 = c1['pressure_level'].values, c1['longitude'].values
leva2, lona2 = hl1['pressure_level'].values, hl1['longitude'].values
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

dsa2 = dsa2.sel(latitude=slice(23, 23), longitude=slice(80, 90))
trr2 = trr.sel(lat=slice(22.99, 23), lon=slice(80, 90))
mds2 = mds2.sel(latitude=slice(23, 23), longitude=slice(80, 90))
pv2 = pva2.sel(latitude=slice(23, 23), longitude=slice(80, 90))
latb = trr2['lat'].values
lonb = trr2['lon'].values
# theta2 = dsa['t'].mean(dim=['latitude']).isel(valid_time=6).squeeze()#-273.16 # Fixed dataset reference

d = dsa2['u'].mean(dim=['latitude']).isel(valid_time=6).squeeze()
e = dsa2['v'].mean(dim=['latitude']).isel(valid_time=6).squeeze()
f = dsa2['w'].mean(dim=['latitude']).isel(valid_time=6).squeeze() * 10
c2 = d + e 
dua2 = c2/2
dva2 = f

tbr2 = trr2['elevation'].mean(dim=['lat']).values#.sel(lat=slice(22.0, 22.5), lon=slice(80, 90))
pb2 = pv2['pv'].mean(dim=['latitude']).isel(valid_time=6).squeeze() / 1*1.0e+06
h3 = mds2['ciwc'].mean(dim=['latitude']).isel(valid_time=6).squeeze() / 1*1.0e+05
h4 = mds2['cswc'].mean(dim=['latitude']).isel(valid_time=6).squeeze() / 1*1.0e+05
hl2 = h3 + h4
levb1, lonb1 = dua2['pressure_level'].values, dua2['longitude'].values
levb2, lonb2 = hl2['pressure_level'].values, hl2['longitude'].values

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
pcm1 = ax1.contourf(pb1['longitude'], pb1['pressure_level'], pb1, cmap='jet', 
                    levels=np.linspace(-0.8, 0.8, 10), extend='both')
hail1 = ax1.contour(lona2, leva2, hl1, colors='maroon', linewidths=1, 
                          levels=np.linspace(1, hl2.max(), 8))
ax1.clabel(hail1, inline=True, fontsize=15, fmt='%1.0f')
quivera1 = ax1.quiver(lona_grid1_s, leva_grid1_s, ua1_s, va1_s, scale=300, width=0.001, headlength=5, headwidth=4, color="k")#, transform=ccrs.PlateCarree())

ax1.set_xlabel("lon", fontsize=24)
ax1.set_ylabel("pressure level (hpa)", fontsize=24)
ax1.set_yticks(np.arange(300, 1001, 50))  # Ensure the range is within actual data limits
ax1.set_xticks(np.arange(80, 90.1, 1))  # Ensure the range is within actual data limits
# ax1.invert_yaxis()# ax1.set_xticks(np.arange(82.5, 85.1, 0.5))#, crs=ccrs.PlateCarree())
ax1.tick_params(axis="both", labelsize=22)
ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}°E"))
# # ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
ax1.xaxis.set_tick_params(rotation=45)
ax1.yaxis.set_tick_params(rotation=45)
# ax2 = ax1.twinx()
# ax2.contourf(lon, lat, ds.values, cmap='jet')
ax1.plot(lona, tbr1, color='maroon')
ax1.fill_between(lona, tbr1, tbr1.max() + 0.5, color='grey', alpha=0.99)  # alpha controls transparency# ax2.set_xticks(np.arange(15, 25.1, 1))
ax1.set_ylim([1000, 300])  # Adjust top axis limits to match top axis data range
ax1.set_xlim([80, 90])  # Adjust top axis limits to match top axis data range
# ax1.quiverkey(quiver1, 0.8, 1.05, 10, "10 m/s", labelpos="E",
#               coordinates="axes", fontproperties={"size": 12})
# # # ax1.invert_yaxis()
# cbar1 = plt.colorbar(pcm1, ax=[ax1], orientation='vertical', shrink=0.7, format="%.1f")
# cbar1.set_label(r'Potential Vorticity (K $\mathrm{m^2}$ $\mathrm{kg^{-1}}$ $\mathrm{s^{-1}}$)', fontsize=18)
# cbar1.ax.text(0.69, 1.05,r'$\times   10^{-6}$', fontsize=25, fontweight='bold', ha='center', transform=cbar1.ax.transAxes)
# cbar1.ax.tick_params(labelsize=20)  # Set tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
# cbar1.ax.set_position([0.771, 0.56, 0.35, 0.3])  # Adjust colorbar position: [left, bottom, width, height]
ax1.text(80.9, 991, "Terrain height in hpa", fontsize=20, color='white', fontweight='bold')
ax1.tick_params(axis='both', length=5, width=1.2, labelsize=18)

# fig = plt.figure(figsize=(22, 16))
# gs = gridspec.GridSpec(2, 1, wspace=0.15, hspace=0.305)
ax2 = fig.add_subplot(gs[1, 0])#, projection=ccrs.PlateCarree())
# pcm1 = ax1.contourf(pb2['longitude'], pb2['pressure_level'], pb2, cmap='jet', 
#                     levels=np.linspace(-0.8, 0.8, 10), extend='both')
pcm2 = ax2.contourf(pb2['longitude'], pb2['pressure_level'], pb2, cmap='jet', 
                    levels=np.linspace(-0.8, 0.8, 10), extend='both')
hail1 = ax2.contour(lonb2, levb2, hl2, colors='maroon', linewidths=1, 
                          levels=np.linspace(1, hl2.max(), 8))
ax2.clabel(hail1, inline=True, fontsize=15, fmt='%1.0f')
quiverb1 = ax2.quiver(lonb_grid1_s, levb_grid1_s, ub1_s, vb1_s, scale=300, width=0.001, headlength=5, headwidth=4, color="k")#, transform=ccrs.PlateCarree())

ax2.set_xlabel("lon", fontsize=24)
ax2.set_ylabel("pressure level (hpa)", fontsize=24)
ax2.set_yticks(np.arange(300, 1001, 50))  # Ensure the range is within actual data limits
ax2.set_xticks(np.arange(80, 90.1, 1))  # Ensure the range is within actual data limits
# ax2.invert_yaxis()# ax2.set_xticks(np.arange(82.5, 85.1, 0.5))#, crs=ccrs.PlateCarree())
# ax2.tick_params(axis="both", labelsize=22)
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}°E"))
# # ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.1f}°N"))
ax2.xaxis.set_tick_params(rotation=45)
ax2.yaxis.set_tick_params(rotation=45)
# # ax2 = ax2.twinx()
# ax2.contourf(lon, lat, ds.values, cmap='jet')
ax2.plot(lonb, tbr2, color='maroon')
ax2.fill_between(lonb, tbr2, tbr2.max() + 0.5, color='grey', alpha=0.99)  # alpha controls transparency# ax2.set_xticks(np.arange(80, 90.1, 1))
ax2.set_ylim([1000, 300])  # Adjust top axis limits to match top axis data range
# ax2.set_xlim([80, 90])  # Adjust top axis limits to match top axis data range
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




# dsa = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/ice_mixing_ratio.nc')

