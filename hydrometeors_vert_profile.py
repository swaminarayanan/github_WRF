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


# Load the NetCDF file (replace with your actual dataset file paths)
ds1 = xr.open_dataset(r'/home/swami/work/qrain_20190315.nc')
ds2 = xr.open_dataset(r'/home/swami/work/qrain_20200303.nc')
ds3 = xr.open_dataset(r'/home/swami/work/qgraup_20190315.nc')
ds4 = xr.open_dataset(r'/home/swami/work/qgraup_20200303.nc')
ds5 = xr.open_dataset(r'/home/swami/work/qhail_20190315.nc')
ds6 = xr.open_dataset(r'/home/swami/work/qhail_20200303.nc')
ds7 = xr.open_dataset(r'/home/swami/work/qsnow_20190315.nc')
ds8 = xr.open_dataset(r'/home/swami/work/qsnow_20200303.nc')

# Extract variables
vert1 = ds1['qrain'].isel(time=20).mean(dim=['lat']).squeeze() / 1*1.0e+07
vert2 = ds2['qrain'].isel(time=20).mean(dim=['lat']).squeeze() / 1*1.0e+07
ept1 = ds3['qgraup'].isel(time=20).mean(dim=['lat']).squeeze() / 1*1.0e+07
ept2 = ds4['qgraup'].isel(time=20).mean(dim=['lat']).squeeze() / 1*1.0e+07
rel1 = ds5['qhail'].isel(time=20).mean(dim=['lat']).squeeze() / 1*1.0e+07
rel2 = ds6['qhail'].isel(time=20).mean(dim=['lat']).squeeze() / 1*1.0e+07
div1 = ds7['qsnow'].isel(time=20).mean(dim=['lat']).squeeze() / 1*1.0e+07
div2 = ds8['qsnow'].isel(time=20).mean(dim=['lat']).squeeze() / 1*1.0e+07
# multyplying with a nan values
vert1 = xr.where(vert1 <= 20, np.nan, vert1)
vert2 = xr.where(vert2 <= 20, np.nan, vert2)
ept1 = xr.where(ept1 <= 20, np.nan, ept1)
ept2 = xr.where(ept2 <= 20, np.nan, ept2)
rel1 = xr.where(rel1 <= 20, np.nan, rel1)
rel2 = xr.where(rel2 <= 20, np.nan, rel2)
div1 = xr.where(div1 <= 20, np.nan, div1)
div2 = xr.where(div2 <= 20, np.nan, div2)
# levels
k = np.arange(0, 1850.1, 200)
l = np.arange(0, 5090.1, 500)
m = np.arange(0, 1600.1, 200)
n = np.arange(0, 1850.1, 200)

fig = plt.figure(figsize=(19, 20))
# Adjusted to 3 columns
gs = gridspec.GridSpec(4, 2, width_ratios=[1, 1], wspace=0.15, hspace=0.2)
mpl.rcParams['figure.facecolor'] = 'white'

ax1 = fig.add_subplot(gs[0, 0])  # First column

# Plot shaded CAPE using contourf (filled contour)
vert1_p = ax1.contourf(vert1['lon'], vert1['lev'], vert1, levels=k, cmap='jet')
ax1.set_xticks(np.arange(80, 90.1, 1))
ax1.set_xlim([80, 90])  # Updated x-axis limits for the bottom axis
ax1.set_yticks(np.arange(100, 920.1, 100))
ax1.set_ylim([100, 931])
ax1.set_title('(a) qrain', fontweight='bold', fontsize=22)
ax1.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=18)
ax1.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax1.tick_params(axis='both', length=10, width=2.5, direction='out', pad=5)
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax1.tick_params(axis='y', rotation=0)  # Rotate y-axis labels if needed
ax1.invert_yaxis()  # Invert y-axis
ax1.set_xticklabels([])

ax2 = fig.add_subplot(gs[0, 1])  # First column

# Plot shaded CAPE using contourf (filled contour)
vert2_p = ax2.contourf(vert2['lon'], vert2['lev'], vert2, levels=k, cmap='jet')
ax2.set_xticks(np.arange(80, 90.1, 1))
ax2.set_xlim([80, 90])  # Updated x-axis limits for the bottom axis
ax2.set_yticks(np.arange(100, 920.1, 100))
ax2.set_ylim([100, 931])
ax2.set_title('(b) qrain', fontweight='bold', fontsize=22)
# ax2.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax2.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax2.tick_params(axis='both', length=10, width=2.5, direction='out', pad=5)
ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax2.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax2.invert_yaxis()  # Invert y-axis
ax2.set_xticklabels([])
ax2.set_yticklabels([])

ax3 = fig.add_subplot(gs[1, 0])  # First column

# Plot shaded CAPE using contourf (filled contour)
ept1_p = ax3.contourf(ept1['lon'], ept1['lev'], ept1, levels=l, cmap='jet')
ax3.set_xticks(np.arange(80, 90.1, 1))
ax3.set_xlim([80, 90])  # Updated x-axis limits for the bottom axis
ax3.set_yticks(np.arange(100, 920.1, 100))
ax3.set_ylim([100, 931])
ax3.set_title('(c) qgraup', fontweight='bold', fontsize=22)
ax3.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=18)
ax3.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax3.tick_params(axis='both', length=10, width=2.5, direction='out', pad=5)
ax3.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax3.tick_params(axis='y', rotation=0)  # Rotate y-axis labels if needed
ax3.invert_yaxis()  # Invert y-axis
ax3.set_xticklabels([])

ax4 = fig.add_subplot(gs[1, 1])  # First column

# Plot shaded CAPE using contourf (filled contour)
ept2_p = ax4.contourf(ept2['lon'], ept2['lev'], ept2, levels=l, cmap='jet')
ax4.set_xticks(np.arange(80, 90.1, 1))
ax4.set_xlim([80, 90])  # Updated x-axis limits for the bottom axis
ax4.set_yticks(np.arange(100, 920.1, 100))
ax4.set_ylim([100, 931])
ax4.set_title('(d) qgraup', fontweight='bold', fontsize=22)
# ax4.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax4.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax4.tick_params(axis='both', length=10, width=2.5, direction='out', pad=5)
ax4.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax4.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax4.invert_yaxis()  # Invert y-axis
ax4.set_xticklabels([])
ax4.set_yticklabels([])

ax5 = fig.add_subplot(gs[2, 0])  # First column

# Plot shaded CAPE using contourf (filled contour)
rel1_p = ax5.contourf(rel1['lon'], rel1['lev'], rel1, levels=m, cmap='jet')
ax5.set_xticks(np.arange(80, 90.1, 1))
ax5.set_xlim([80, 90])  # Updated x-axis limits for the bottom axis
ax5.set_yticks(np.arange(100, 920.1, 100))
ax5.set_ylim([100, 931])
ax5.set_title('(e) qhail', fontweight='bold', fontsize=22)
ax5.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=18)
ax5.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax5.tick_params(axis='both', length=10, width=2.5, direction='out', pad=5)
ax5.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax5.tick_params(axis='y', rotation=0)  # Rotate y-axis labels if needed
ax5.invert_yaxis()  # Invert y-axis
ax5.set_xticklabels([])

ax6 = fig.add_subplot(gs[2, 1])  # First column

# Plot shaded CAPE using contourf (filled contour)
rel2_p = ax6.contourf(rel2['lon'], rel2['lev'], rel2, levels=m, cmap='jet')
ax6.set_xticks(np.arange(80, 90.1, 1))
ax6.set_xlim([80, 90])  # Updated x-axis limits for the bottom axis
ax6.set_yticks(np.arange(100, 920.1, 100))
ax6.set_ylim([100, 931])
ax6.set_title('(f) qhail', fontweight='bold', fontsize=22)
# ax6.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax6.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax6.tick_params(axis='both', length=10, width=2.5, direction='out', pad=5)
ax6.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax6.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax6.invert_yaxis()  # Invert y-axis
ax6.set_xticklabels([])
ax6.set_yticklabels([])

ax7 = fig.add_subplot(gs[3, 0])  # First column

# Plot shaded CAPE using contourf (filled contour)
div1_p = ax7.contourf(div1['lon'], div1['lev'], div1, levels=n, cmap='jet')
ax7.set_xticks(np.arange(80, 90.1, 1))
ax7.set_xlim([80, 90])  # Updated x-axis limits for the bottom axis
ax7.set_yticks(np.arange(100, 920.1, 100))
ax7.set_ylim([100, 931])
ax7.set_title('(g) qsnow', fontweight='bold', fontsize=22)
ax7.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=18)
ax7.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: '{:.0f}°E'.format(x)))
ax7.tick_params(axis='both', length=10, width=2.5, direction='out', pad=5)
ax7.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax7.tick_params(axis='y', rotation=0)  # Rotate y-axis labels if needed
ax7.invert_yaxis()  # Invert y-axis

ax8 = fig.add_subplot(gs[3, 1])  # First column

# Plot shaded CAPE using contourf (filled contour)
div2_p = ax8.contourf(div2['lon'], div2['lev'], div2, levels=n, cmap='jet')
ax8.set_xticks(np.arange(80, 90.1, 1))
ax8.set_xlim([80, 90])  # Updated x-axis limits for the bottom axis
ax8.set_yticks(np.arange(100, 920.1, 100))
ax8.set_ylim([100, 931])
ax8.set_title('(h) qsnow', fontweight='bold', fontsize=22)
# ax8.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax8.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: '{:.0f}°E'.format(x)))
# Adjust tick length and direction
ax8.tick_params(axis='both', length=10, width=2.5, direction='out', pad=5)
ax8.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax8.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax8.invert_yaxis()  # Invert y-axis
ax8.set_yticklabels([])

cbar1 = plt.colorbar(vert2_p, ax=[ax1, ax2],
                     orientation='vertical', shrink=0.7)
cbar1.set_label('qrain (g kg-1)', fontsize=22)
cbar1.ax.text(0.51, 1.05, r'$\times   10^{-4}$', fontsize=25,
              fontweight='bold', ha='center', transform=cbar1.ax.transAxes)
cbar1.ax.tick_params(labelsize=18)  # Set tick label size
cbar1.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed

cbar2 = plt.colorbar(ept2_p, ax=[ax3, ax4], orientation='vertical', shrink=0.7)
cbar2.set_label('qgraup (g kg-1)', fontsize=22)
cbar2.ax.text(0.21, 1.05, r'$\times   10^{-4}$', fontsize=25,
              fontweight='bold', ha='center', transform=cbar2.ax.transAxes)
cbar2.ax.tick_params(labelsize=18)  # Set tick label size
cbar2.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed

cbar3 = plt.colorbar(rel2_p, ax=[ax6, ax5], orientation='vertical', shrink=0.7)
cbar3.set_label('qhail (g kg-1)', fontsize=22)
cbar3.ax.text(0.11, 1.05, r'$\times   10^{-4}$', fontsize=25,
              fontweight='bold', ha='center', transform=cbar3.ax.transAxes)
cbar3.ax.tick_params(labelsize=18)  # Set tick label size
cbar3.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed

cbar4 = plt.colorbar(div2_p, ax=[ax8, ax7], orientation='vertical', shrink=0.7)
cbar4.set_label('qsnow (g kg-1)', fontsize=22)
cbar4.ax.text(0.01, 1.05, r'$\times   10^{-4}$', fontsize=25,
              fontweight='bold', ha='center', transform=cbar4.ax.transAxes)
cbar4.ax.tick_params(labelsize=18)  # Set tick label size
cbar4.ax.yaxis.set_tick_params(rotation=0)  # Rotate y-axis labels if needed

plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
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
