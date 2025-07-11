import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Load the NetCDF file (replace with your actual dataset file paths)
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20190315.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
ds3a = xr.open_dataset(r'/media/lab/My Passport/hail/theta_data_2019.nc')
ds4b = xr.open_dataset(r'/media/lab/My Passport/hail/theta_data_2020.nc')
ds5 = xr.open_dataset(r'/media/lab/My Passport/hail/rvdv_2019.nc')
ds6 = xr.open_dataset(r'/media/lab/My Passport/hail/rvdv_2020.nc')
ds7 = xr.open_dataset(r'/media/lab/My Passport/hail/specifichumidity_2019.nc')
ds8 = xr.open_dataset(r'/media/lab/My Passport/hail/specifichumidity_2020.nc')

# Select the data/media/lab/My Passport/hail/theta_data.nc
ds1 = ds1.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4)).isel(time=20)
ds2 = ds2.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4)).isel(time=16)
ds3 = ds3a.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4)).isel(time=20)
ds4 = ds4b.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4)).isel(time=16)
ds5 = ds5.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4)).isel(time=20) 
ds6 = ds6.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4)).isel(time=16) 
ds7 = ds7.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4)).isel(time=20)
ds8 = ds8.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4)).isel(time=16)
ds33 = ds3a.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4), lev=slice(1000, 400)).isel(time=20)
ds44 = ds4b.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.4), lev=slice(1000, 400)).isel(time=16)

# Extract variables
vert1 = ds1['w'].mean(dim=['lat']).squeeze()
vert2 = ds2['w'].mean(dim=['lat']).squeeze() 
ept1 = ds3['theta_e1'].mean(dim=['lon', 'lat']).squeeze() 
ept2 = ds4['theta_e2'].mean(dim=['lon', 'lat']).squeeze() 
rel1 = ds5['relative_vorticity'].mean(dim=['lat']).squeeze()/ 1*1.0e+04
xx = rel1.values 
rel2 = ds6['relative_vorticity'].mean(dim=['lat']).squeeze() / 1*1.0e+04
div1 = ds5['divergence'].mean(dim=['lat']).squeeze() / 1*1.0e+05
x = div1.values
div2 = ds6['divergence'].mean(dim=['lat']).squeeze() / 1*1.0e+05
sp_hd1 = ds7['specific_humidity'].mean(dim=['lat']).squeeze() / 1*1.0e+03
sp_hd2 = ds8['specific_humidity'].mean(dim=['lat']).squeeze() / 1*1.0e+03
dbz1 = ds1['dbz'].mean(dim=['lat']).squeeze() 
dbz2 = ds2['dbz'].mean(dim=['lat']).squeeze() 
# ept11 = ds33['theta_e1'].mean(dim=['lon']).squeeze()
# ept22 = ds44['theta_e2'].mean(dim=['lon']).squeeze()

# Set up a map projection
proj = ccrs.PlateCarree()

fig = plt.figure(figsize=(18, 6))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1], wspace=0.17)  # Adjusted to 3 columns
mpl.rcParams['figure.facecolor'] = 'white'
ax5 = fig.add_subplot(gs[0, 0])  # First column

# Plot shaded CAPE using contourf (filled contour)
sp_hd1_p = ax5.contourf(sp_hd1['lon'], sp_hd1['lev'], sp_hd1, cmap='YlOrBr', 
                        levels=np.linspace(sp_hd1.min(), sp_hd1.max(), 10))

# Plot Temperature using contour (line contours with labels)
dbz1_p = ax5.contour(dbz1['lon'], dbz1['lev'], dbz1, colors='k', linewidths=2)
ax5.clabel(dbz1_p, inline=True, fontsize=15, fmt='%1.0f')

# # # Plot Specific Humidity using dotted contour lines (dashed contourf)
# # sh1_filled_contour = ax1.contour(ds3['lon'], ds3['lev'], sh1, cmap='seismic', alpha=0.7, linewidths=2,
# #                                   levels=np.linspace(sh1.min(), sh1.max(), 10), 
# #                                   linestyles='--')
# # ax1.clabel(sh1_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# # Axis and ticks formatting
ax5.set_yticks(np.arange(100, 950.1, 100))
ax5.set_ylim([100, 931])
ax5.set_xticks(np.arange(84.8, 85.4, 0.1))
ax5.set_xlim([84.8, 85.4])
# # ax5.set_yticklabels([])
# # ax5.set_xticklabels([])

ax5.invert_yaxis()
ax5.set_title('(e)  ', fontweight='bold', fontsize=22)
ax5.set_xlabel('Longitude', fontweight='bold', fontsize=16)
ax5.set_ylabel('Pressure(hpa)', fontweight='bold', fontsize=16)
ax5.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
# Rotate the x-axis tick labels by 90 degrees
ax5.tick_params(axis='y', rotation=45) # Rotate y-axis labels (if needed)
ax5.tick_params(axis='x',  rotation=45)  # Rotate y-axis labels (if needed)

# # Plot for cape2, t2, sh2 (ds2 and ds4 data)
ax6 = fig.add_subplot(gs[0, 1])  # First column

# Plot shaded CAPE using contourf (filled contour)
sp_hd2_p = ax6.contourf(sp_hd2['lon'], sp_hd2['lev'], sp_hd2, cmap='YlOrBr', 
                        levels=np.linspace(sp_hd2.min(), sp_hd2.max(), 10))

# Plot Temperature using contour (line contours with labels)
dbz2_p = ax6.contour(dbz2['lon'], dbz2['lev'], dbz2, colors='k', linewidths=2)
ax6.clabel(dbz2_p, inline=True, fontsize=15, fmt='%1.0f')

# # Plot Specific Humidity using dotted contour lines (dashed contourf)
# # sh2_filled_contour = ax2.contour(ds4['lon'], ds4['lev'], sh2, cmap='seismic', alpha=0.7, linewidths=2,
# #                                   levels=np.linspace(sh2.min(), sh2.max(), 10), 
# #                                   linestyles='--')
# # ax2.clabel(sh2_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# # Axis and ticks formatting
ax6.set_yticks(np.arange(100, 950.1, 100))
ax6.set_ylim([100, 931])
ax6.set_yticklabels([])

ax6.set_xticks(np.arange(84.8, 85.4, 0.1))
ax6.set_xlim([84.8, 85.4])
# ax6.set_yticklabels([])
# ax6.set_xticklabels([])

ax6.invert_yaxis()
ax6.set_title('(f) ', fontweight='bold', fontsize=22)
ax6.set_xlabel('Longitude', fontweight='bold', fontsize=16)
# ax2.set_ylabel('Pressure', fontweight='bold', fontsize=24)
ax6.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
# Rotate the x-axis tick labels by 90 degrees
# ax2.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
ax6.tick_params(axis='y', rotation=90)  # Rotate y-axis labels (if needed)
ax6.tick_params(axis='x', rotation=45)  # Rotate y-axis labels (if needed)

# Add colorbars for both plots

cbar1 = plt.colorbar(sp_hd2_p, ax=[ax5, ax6], orientation='vertical', shrink=0.7)
cbar1.set_label('kg/kg', fontsize=18)
cbar1.ax.text(0.51, 1.05,r'     $\times10^{-3}$', fontsize=25, fontweight='bold', ha='center', transform=cbar1.ax.transAxes)
cbar1.ax.set_position([0.76, 0.22, 0.5, 0.54])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar

# cbar1.ax.text(0.51, 1.05,r'$\times   10^{-4}$', fontsize=25, fontweight='bold', ha='center', transform=cbar1.ax.transAxes)
cbar1.ax.tick_params(labelsize=18)  # Set tick label size
cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    "axes.linewidth": 2,
     "patch.linewidth": 2,
    'xtick.major.size': 16,
    'ytick.major.size': 16,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})

# Adjust layout and show the plot
plt.show()
