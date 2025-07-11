

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Load the NetCDF file (replace with your actual dataset file paths)
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20200303.nc')
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
sp_hd1 = ds7['specific_humidity'].mean(dim=['lat']).squeeze() 
sp_hd2 = ds8['specific_humidity'].mean(dim=['lat']).squeeze() 
dbz1 = ds1['dbz'].mean(dim=['lat']).squeeze() 
dbz2 = ds2['dbz'].mean(dim=['lat']).squeeze() 
# ept11 = ds33['theta_e1'].mean(dim=['lon']).squeeze()
# ept22 = ds44['theta_e2'].mean(dim=['lon']).squeeze()

# Set up a map projection
proj = ccrs.PlateCarree()

# # Create a figure and axis with Cartopy projection
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 10))

# # Plot for cape1, t1, sh1 (ds1 and ds3 data)
# Create the figure and GridSpec with 3 columns and 1 row
fig = plt.figure(figsize=(20, 20))
gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], wspace=0.12)  # Adjusted to 3 columns
mpl.rcParams['figure.facecolor'] = 'white'
# ax1 = fig.add_subplot(gs[0, 0])  # First column

# # Plot shaded CAPE using contourf (filled contour)
# vert1_p = ax1.contourf(vert1['lon'], vert1['lev'], vert1, cmap='YlOrBr', 
#                                   levels=np.linspace(vert1.min(), vert1.max(), 10))

# # Plot Temperature using contour (line contours with labels)
# # ept1_p = ax1.contour(ept1['lat'], ept1['lev'], ept1, colors='k', linewidths=2, 
# #                           levels=np.linspace(ept1.min(), ept1.max(), 9))
# # ax1.clabel(ept1_p, inline=True, fontsize=15, fmt='%1.0f')
# ax1.set_xticks(np.arange(22.8, 23.51, 0.1))
# ax1.set_xlim([84.8, 85.4])
# ax1.set_xticklabels([])

# ax11 = ax1.twiny()
# ax21 = ax11.xticks()

# ept1_p = ax11.plot(ept1.values, ept1['lev'], color='k', linewidth=2)
# # ept11_p = ax1.contour(ept1['lat'], ept11['lev'], ept11, colors='k', linewidths=2, 
# #                           levels=np.linspace(ept11.min(), ept11.max(), 4))
# # ax1.clabel(ept11_p, inline=True, fontsize=15, fmt='%1.0f')

# # # Plot Specific Humidity using dotted contour lines (dashed contourf)
# # sh1_filled_contour = ax1.contour(ds3['lon'], ds3['lev'], sh1, cmap='seismic', alpha=0.7, linewidths=2,
# #                                   levels=np.linspace(sh1.min(), sh1.max(), 10), 
# #                                   linestyles='--')
# # ax1.clabel(sh1_filled_contour, inline=True, fontsize=17, fmt='%1.2f')
# # Axis and ticks formatting

# ax1.set_yticks(np.arange(100, 950.1, 100))
# ax1.set_ylim([100, 931])
# ax1.set_title('(a)  ', fontweight='bold', fontsize=22)
# # ax1.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax1.set_ylabel('Pressure(hpa)', fontweight='bold', fontsize=20)
# ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
# # Rotate the x-axis tick labels by 90 degrees
# ax1.tick_params(axis='y', rotation=45) # Rotate y-axis labels (if needed)
# ax1.tick_params(axis='x',  rotation=45)  # Rotate y-axis labels (if needed)
# # ax1.set_yticklabels([])
# ax1.invert_yaxis()

# # Set top x-axis (ax11) ticks and labels
# ax11.set_xticks(np.arange(310, 390.1, 10))  # Same ticks as the bottom
# ax11.set_xlim([320, 390])  # Sync limits with the bottom axis
# # ax11.set_xlabel('Longitude (Top)', fontweight='bold', fontsize=14)  # Label top x-axis
###################################
##############################
ax1 = fig.add_subplot(gs[0, 0])  # First column

# Plot shaded CAPE using contourf (filled contour)
vert1_p = ax1.contourf(vert1['lon'], vert1['lev'], vert1, cmap='YlOrBr', 
                       levels=np.linspace(vert1.min(), vert1.max(), 10))

# Plot Temperature using contour (line contours with labels)
ept1_p = ax1.plot(ept1.values, ept1['lev'], color='k', linewidth=2)
# ax1.clabel(ept1_p, inline=True, fontsize=15, fmt='%1.0f')

# Set x-axis and y-axis tick parameters and limits
ax1.set_xticks(np.arange(84.8, 85.4, 0.1))
ax1.set_xlim([84.8, 85.4])  # Updated x-axis limits for the bottom axis
ax1.set_yticks(np.arange(100, 950.1, 100))
ax1.set_ylim([100, 931])
ax1.set_title('(a)', fontweight='bold', fontsize=22)
ax1.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax1.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax1.invert_yaxis()  # Invert y-axis

# Set up the top x-axis (ax11)
ax11 = ax1.twiny()  # Create a twin x-axis sharing the y-axis with ax1
ax11.set_xticks(np.arange(310, 390.1, 10))  # Set ticks on the top x-axis
ax11.set_xlim([310, 390])  # Adjust top axis limits to match top axis data range
ax11.set_xlabel('Temperature (K)', fontweight='bold', fontsize=21)
ax1.set_xticklabels([])
ax11.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

# Plot data on the top x-axis
ax11.plot(ept1.values, ept1['lev'], color='k', linewidth=2)  # Example plot on top axis
# Commented-out lines: Adjust or uncomment if needed
# ept11_p = ax11.contour(ept1['lat'], ept11['lev'], ept11, colors='k', linewidths=2, 
#                        levels=np.linspace(ept11.min(), ept11.max(), 4))
# ax1.clabel(ept11_p, inline=True, fontsize=15, fmt='%1.0f')

# Specific Humidity plot (dotted contour lines)
# Uncomment and adjust this as needed
# sh1_filled_contour = ax1.contour(ds3['lon'], ds3['lev'], sh1, cmap='seismic', alpha=0.7, linewidths=2,
#                                  levels=np.linspace(sh1.min(), sh1.max(), 10), 
#                                  linestyles='--')
# ax1.clabel(sh1_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# Display the plot
# Plot for cape2, t2, sh2 (ds2 and ds4 data)
ax2 = fig.add_subplot(gs[0, 1])  # First column

# Plot shaded CAPE using contourf (filled contour)
vert2_p = ax2.contourf(vert2['lon'], vert2['lev'], vert2, cmap='YlOrBr', 
                                  levels=np.linspace(vert2.min(), vert2.max(), 10))

# Plot Temperature using contour (line contours with labels)
# ax22 = ax2.twiny()
# ept2_p = ax22.plot(ept2.values, ept2['lev'], color='k')
# ax2.clabel(ept2_p, inline=True, fontsize=15, fmt='%1.0f')
# ept22_p = ax2.contour(ept22['lat'], ept22['lev'], ept22, colors='k', linewidths=2, 
#                           levels=np.linspace(ept22.min(), ept22.max(), 4))
# ax2.clabel(ept22_p, inline=True, fontsize=15, fmt='%1.0f')

# Plot Specific Humidity using dotted contour lines (dashed contourf)
# sh2_filled_contour = ax2.contour(ds4['lon'], ds4['lev'], sh2, cmap='seismic', alpha=0.7, linewidths=2,
#                                   levels=np.linspace(sh2.min(), sh2.max(), 10), 
#                                   linestyles='--')
# ax2.clabel(sh2_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# Axis and ticks formatting
ax2.set_xticks(np.arange(84.8, 85.4, 0.1))
ax2.set_xlim([84.8, 85.4])  # Updated x-axis limits for the bottom axis
ax2.set_yticks(np.arange(100, 950.1, 100))
ax2.set_ylim([100, 931])
ax2.set_title('(b)', fontweight='bold', fontsize=22)
# ax2.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=20)
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax2.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax2.invert_yaxis()  # Invert y-axis
ax2.set_xticklabels([])
ax2.set_yticklabels([])


# ax2.invert_yaxis()
ax2.set_title('(b) ', fontweight='bold', fontsize=22)
# ax2.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax2.set_ylabel('Pressure', fontweight='bold', fontsize=24)
# ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
# Rotate the x-axis tick labels by 90 degrees
# ax2.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
ax2.tick_params(axis='y', rotation=90)  # Rotate y-axis labels (if needed)
ax2.tick_params(axis='x', rotation=45)  # Rotate y-axis labels (if needed)

ax22 = ax2.twiny()  # Create a twin x-axis sharing the y-axis with ax1
ax22.set_xticks(np.arange(310, 390.1, 10))  # Set ticks on the top x-axis
ax22.set_xlim([310, 390])  # Adjust top axis limits to match top axis data range
ax22.set_xlabel('Temperature (K)', fontweight='bold', fontsize=21)
ax22.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
# Plot data on the top x-axis
ax22.plot(ept2.values, ept2['lev'], color='k', linewidth=2)  # Example plot on top axis

# # Add colorbars for both plots
# cbar1 = plt.colorbar(cape1_filled_contour, ax=ax1, orientation='vertical', shrink=0.7)
# cbar1.set_label('CAPE (J/kg)', fontsize=22)
# cbar1.ax.tick_params(labelsize=20)  # Set tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=45)  # Rotate y-axis labels if needed


ax3 = fig.add_subplot(gs[1, 0])  # First column

# Plot shaded CAPE using contourf (filled contour)
rel1_p = ax3.contourf(rel1['lon'], rel1['lev'], rel1, cmap='YlOrBr', 
                                  levels=np.linspace(rel1.min(), rel1.max(), 10))

# Plot Temperature using contour (line contours with labels)
# div1_p = ax3.contour(div1['lon'], div1['lev'], div1, colors='k', linewidths=2, 
#                           levels=np.linspace(div1.min(), div1.max(), 10), label='r'$\times   10^{-4}$'')
# ax3.clabel(div1_p, inline=True, fontsize=15, fmt='%1.0f')
div1_p = ax3.contour(div1['lon'], div1['lev'], div1, colors='k', linewidths=2, 
                      levels=np.linspace(div1.min(), div1.max(), 10))  # Proper LaTeX formatting
ax3.clabel(div1_p, inline=True, fontsize=15, fmt='%1.0f')
# Add a label to the contour plot (for the legend)
h1, = ax3.plot([], [], 'k-', label=r'$ \times 10^{-4}$')  # Empty plot for legend

# Add the legend inside the figure
ax3.legend(loc='upper right', fontsize=19)  # Adjust `loc` as needed# # Plot Specific Humidity using dotted contour lines (dashed contourf)
# sh1_filled_contour = ax1.contour(ds3['lon'], ds3['lev'], sh1, cmap='seismic', alpha=0.7, linewidths=2,
#                                   levels=np.linspace(sh1.min(), sh1.max(), 10), 
#                                   linestyles='--')
# ax1.clabel(sh1_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# Axis and ticks formatting
ax3.set_yticks(np.arange(100, 950.1, 100))
ax3.set_ylim([100, 931])
# ax3.set_yticklabels([])
ax3.set_xticks(np.arange(84.8, 85.41, 0.1))
ax3.set_xlim([84.8, 85.4])
# ax3.set_xticklabels([])
ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))

ax3.invert_yaxis()
ax3.set_title('(c)  ', fontweight='bold', fontsize=22)
# ax3.set_xlabel('Longitude', fontweight='bold', fontsize=20)
ax3.set_ylabel('Pressure(hpa)', fontweight='bold', fontsize=22)
ax3.set_xlabel('longitude', fontweight='bold', fontsize=22)
# ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
# Rotate the x-axis tick labels by 90 degrees
ax3.tick_params(axis='y', rotation=45) # Rotate y-axis labels (if needed)
ax3.tick_params(axis='x',  rotation=45)  # Rotate y-axis labels (if needed)

# Plot for cape2, t2, sh2 (ds2 and ds4 data)
ax4 = fig.add_subplot(gs[1, 1])  # First column

# Plot shaded CAPE using contourf (filled contour)
rel2_p = ax4.contourf(rel2['lon'], rel2['lev'], rel2, cmap='YlOrBr', 
                                  levels=np.linspace(rel2.min(), rel2.max(), 10))

# Plot Temperature using contour (line contours with labels)
div2_p = ax4.contour(div2['lon'], div2['lev'], div2, colors='k', linewidths=2, 
                          levels=np.linspace(div2.min(), div2.max(), 10))
ax4.clabel(div2_p, inline=True, fontsize=15, fmt='%1.0f')
h1, = ax4.plot([], [], 'k-', label=r'$ \times 10^{-4}$')  # Empty plot for legend

# Add the legend inside the figure
ax4 .legend(loc='upper right', fontsize=19)  # Adjust `loc` as needed# # Plot Specific Humidity using dotted contour lines (dashed contourf)

# Plot Specific Humidity using dotted contour lines (dashed contourf)
# sh2_filled_contour = ax2.contour(ds4['lon'], ds4['lev'], sh2, cmap='seismic', alpha=0.7, linewidths=2,
#                                   levels=np.linspace(sh2.min(), sh2.max(), 10), 
#                                   linestyles='--')
# ax2.clabel(sh2_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# Axis and ticks formatting
ax4.set_yticks(np.arange(100, 950.1, 100))
ax4.set_ylim([100, 931])
ax4.set_yticklabels([])
ax4.set_xticks(np.arange(84.8, 85.41, 0.1))
ax4.set_xlim([84.8, 85.4])
# ax4.set_xticklabels([])
ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))

ax4.invert_yaxis()
ax4.set_title('(d) ', fontweight='bold', fontsize=22)
ax4.set_xlabel('longitude', fontweight='bold', fontsize=22)

# ax4.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax2.set_ylabel('Pressure', fontweight='bold', fontsize=24)
# ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
# Rotate the x-axis tick labels by 90 degrees
# ax2.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
ax4.tick_params(axis='y', rotation=90)  # Rotate y-axis labels (if needed)
ax4.tick_params(axis='x', rotation=45)  # Rotate y-axis labels (if needed)

# # Add colorbars for both plots
# cbar1 = plt.colorbar(cape1_filled_contour, ax=ax1, orientation='vertical', shrink=0.7)
# cbar1.set_label('CAPE (J/kg)', fontsize=22)
# cbar1.ax.tick_params(labelsize=20)  # Set tick label size
# cbar1.ax.yaxis.set_tick_params(rotation=45)  # Rotate y-axis labels if needed


# #################################
# ax5 = fig.add_subplot(gs[2, 0])  # First column

# # Plot shaded CAPE using contourf (filled contour)
# sp_hd1_p = ax5.contourf(sp_hd1['lon'], sp_hd1['lev'], sp_hd1, cmap='YlOrBr', 
#                                   levels=np.linspace(sp_hd1.min(), sp_hd1.max(), 10))

# # Plot Temperature using contour (line contours with labels)
# dbz1_p = ax5.contour(dbz1['lon'], dbz1['lev'], dbz1, colors='k', linewidths=2, 
#                           levels=np.linspace(dbz1.min(), dbz1.max(), 10))
# ax5.clabel(dbz1_p, inline=True, fontsize=15, fmt='%1.0f')

# # # Plot Specific Humidity using dotted contour lines (dashed contourf)
# # sh1_filled_contour = ax1.contour(ds3['lon'], ds3['lev'], sh1, cmap='seismic', alpha=0.7, linewidths=2,
# #                                   levels=np.linspace(sh1.min(), sh1.max(), 10), 
# #                                   linestyles='--')
# # ax1.clabel(sh1_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# # Axis and ticks formatting
# ax5.set_yticks(np.arange(100, 950.1, 100))
# ax5.set_ylim([100, 931]) 
# ax5.set_xticks(np.arange(85, 85.61, 0.1))
# ax5.set_xlim([85, 85.6])
# # ax5.set_yticklabels([])
# # ax5.set_xticklabels([])

# ax5.invert_yaxis()
# ax5.set_title('(e)  ', fontweight='bold', fontsize=22)
# ax5.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax5.set_ylabel('Pressure(hpa)', fontweight='bold', fontsize=20)
# ax5.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
# # Rotate the x-axis tick labels by 90 degrees
# ax5.tick_params(axis='y', rotation=45) # Rotate y-axis labels (if needed)
# ax5.tick_params(axis='x',  rotation=45)  # Rotate y-axis labels (if needed)

# # Plot for cape2, t2, sh2 (ds2 and ds4 data)
# ax6 = fig.add_subplot(gs[2, 1])  # First column

# # Plot shaded CAPE using contourf (filled contour)
# sp_hd2_p = ax6.contourf(sp_hd2['lon'], sp_hd2['lev'], sp_hd2, cmap='YlOrBr', 
#                                   levels=np.linspace(sp_hd2.min(), sp_hd2.max(), 10))

# # Plot Temperature using contour (line contours with labels)
# dbz2_p = ax6.contour(dbz2['lon'], dbz2['lev'], dbz2, colors='k', linewidths=2, 
#                           levels=np.linspace(dbz2.min(), dbz2.max(), 10))
# ax6.clabel(dbz2_p, inline=True, fontsize=15, fmt='%1.0f')

# # Plot Specific Humidity using dotted contour lines (dashed contourf)
# # sh2_filled_contour = ax2.contour(ds4['lon'], ds4['lev'], sh2, cmap='seismic', alpha=0.7, linewidths=2,
# #                                   levels=np.linspace(sh2.min(), sh2.max(), 10), 
# #                                   linestyles='--')
# # ax2.clabel(sh2_filled_contour, inline=True, fontsize=17, fmt='%1.2f')

# # Axis and ticks formatting
# ax6.set_yticks(np.arange(100, 950.1, 100))
# ax6.set_ylim([100, 931])
# ax6.set_yticklabels([])

# ax6.set_xticks(np.arange(85, 85.61, 0.1))
# ax6.set_xlim([85, 85.6])
# # ax6.set_yticklabels([])
# # ax6.set_xticklabels([])

# ax6.invert_yaxis()
# ax6.set_title('(f) ', fontweight='bold', fontsize=22)
# ax6.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# # ax2.set_ylabel('Pressure', fontweight='bold', fontsize=24)
# ax6.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
# # Rotate the x-axis tick labels by 90 degrees
# # ax2.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
# ax6.tick_params(axis='y', rotation=90)  # Rotate y-axis labels (if needed)
# ax6.tick_params(axis='x', rotation=45)  # Rotate y-axis labels (if needed)

# # Add colorbars for both plots

cbar1 = plt.colorbar(vert2_p, ax=[ax2, ax1], orientation='vertical', shrink=0.7)
cbar1.set_label('W (m/s)', fontsize=22)
# cbar1.ax.text(0.51, 1.05,r'$\times   10^{-4}$', fontsize=25, fontweight='bold', ha='center', transform=cbar1.ax.transAxes)
cbar1.ax.tick_params(labelsize=20)  # Set tick label size
cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
# cbar2.set_position([0.8, 0.94, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# cbar2.ax.set_position([0.755, 0.185, 0.65, 0.6])  # Adjust colorbar position: [left, bottom, width, height]
# p = fig.suptitle('CAPE, Relative humidity', fontsize=20, fontweight='bold')# Show the plot
# p.set_position([0.434, 0.99, 0.3, 0.2])  # (L-R, T-B,  cbar length vertical, CBAR width,   Adjust the po,sition and size of the colorbar
cbar2 = plt.colorbar(rel2_p, ax=[ax3, ax4], orientation='vertical', shrink=0.7)
cbar2.set_label('rel_vor (/s)', fontsize=22)
cbar2.ax.text(0.51, 1.05,r'$\times   10^{-4}$', fontsize=25, fontweight='bold', ha='center', transform=cbar2.ax.transAxes)
cbar2.ax.tick_params(labelsize=20)  # Set tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
# cbar2.set_position([0.8, 0.94, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# cbar3.ax.set_position([0.755, 0.185, 0.65, 0.6])  # Adjust colorbar position: [left, bottom, width, height]
# p1 = fig.suptitle('CAPE, Relative humidity', fontsize=20, fontweight='bold')# Show the plot
# p1.set_position([0.434, 0.99, 0.3, 0.2])  # (L-R, T-B,  cbar length vertical, CBAR width,   Adjust the po,sition and size of the colorbar
# cbar3 = plt.colorbar(sp_hd2_p, ax=[ax5, ax6], orientation='vertical', shrink=0.7)
# cbar3.set_label('specific humidity (kg/kg)', fontsize=22)
# cbar3.ax.tick_params(labelsize=20)  # Set tick label size
# cbar3.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed
# cbar2.set_position([0.8, 0.94, 0.3, 0.2])  # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
# cbar4.ax.set_position([0.755, 0.185, 0.65, 0.6])  # Adjust colorbar position: [left, bottom, width, height]
# p2 = fig.suptitle('CAPE, Relative humidity', fontsize=20, fontweight='bold')# Show the plot
# p2.set_position([0.434, 0.99, 0.3, 0.2])  # (L-R, T-B,  cbar length vertical, CBAR width,   Adjust the po,sition and size of the colorbar

plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 24,
    'ytick.major.size': 24,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})

# Adjust layout and show the plot
plt.show()

