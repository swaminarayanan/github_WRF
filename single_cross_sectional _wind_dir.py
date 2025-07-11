
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
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/20200303.nc')
trr1 = xr.open_dataset(r'/media/lab/My Passport/hail/ncei_terrain data/GEBCO_01_Mar_2025_34026bc640b3/gebco_2024_n25.0_s15.0_w80.0_e90.0.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/potent_vort2020.nc')
mds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
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
###########################
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
altitude1 = tar1  # meters
tar1 = altitude_to_hpa(altitude1)
tar1 = np.where(tar1>1000, 1000, tar1)
lona_grid1, leva_grid1 = np.meshgrid(lata1, leva1)
ua1, va1 = dua1.values, dva1.values
lona_grid1_s = lona_grid1[::, ::]
leva_grid1_s = leva_grid1[::, ::]
ua1_s = ua1[::, ::]
va1_s = va1[::, ::]
fig = plt.figure(figsize=(19, 8))
gs = gridspec.GridSpec(1, 1)#, width_ratios=[1, 1], wspace=0.15)
ax2 = fig.add_subplot(gs[0, 0])#, projection=ccrs.PlateCarree())
pcma1 = ax2.contourf(lata1, leva1, pa1, cmap='jet', 
                    levels=np.linspace(-0.8, 0.8, 10), extend='both')
haila1 = ax2.contour(lata2, leva2, hla1, colors='maroon', linewidths=1, 
                          levels=np.linspace(0.2, hla1.max(), 4))
ax2.clabel(haila1, inline=True, fontsize=15, fmt='%1.0f')
quiver1 = ax2.quiver(lona_grid1_s, leva_grid1_s, ua1_s, va1_s, scale=200, width=0.001, headlength=5, headwidth=4, color="k")#, transform=ccrs.PlateCarree())

ax2.set_xlabel("lat", fontsize=18)
ax2.set_ylabel("pressure level", fontsize=18)
ax2.set_yticks(np.arange(700, 1001, 50))  # Ensure the range is within actual data limits
ax2.set_xticks(np.arange(15, 25.1, 1))  # Ensure the range is within actual data limits
ax2.invert_yaxis()# ax2.set_xticks(np.arange(82.5, 85.1, 0.5))#, crs=ccrs.PlateCarree())
ax2.tick_params(axis="both", labelsize=16)
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.1f}°N"))
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
ax2.tick_params(axis='both', length=5, width=1.2, labelsize=12)
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 18,
    'ytick.labelsize': 18,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 14,
    'ytick.major.size': 14,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 16,  # For axes titles
    'figure.titlesize': 18  # For overall figure title
})
plt.show()
