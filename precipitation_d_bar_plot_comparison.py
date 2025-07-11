import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Load datasets
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20200303.nc')
ds3 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds4 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
ds5 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
ds6 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20200303.nc')
ds7 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20190421.nc')
ds8 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20200303.nc')
ds9 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20190421.nc')
ds10 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20200303.nc')

ds11 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20190421.nc')
ds22 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20200303.nc')
# Select the region of interest and calculate non-cumulative data
dsa = ds11['precipitation'].sum(dim='time').sel(lat=slice(21, 21.8), lon=slice(86.5, 87.3)).mean()#.squeeze()#.values
dsb = ds22['precipitation'].sum(dim='time').sel(lat=slice(23.1, 23.5), lon=slice(85.1, 85.5)).mean()#.squeeze()#.values

# Extract scalar values
a = ds1['rainnc'].sel(lon=slice(86.6, 87.2), lat=slice(21.1, 21.6)).isel(time=48).mean().values.item()# This case actual time is 17 step
b = ds2['rainnc'].sel(lon=slice(85.1, 85.5), lat=slice(23.1, 23.5)).isel(time=48).mean().values.item()
c = ds3['rainnc'].sel(lon=slice(86.6, 87.2), lat=slice(21.1, 21.6)).isel(time=48).mean().values.item()
d = ds4['rainnc'].sel(lon=slice(85.1, 85.5), lat=slice(23.1, 23.5)).isel(time=48).mean().values.item()
e = ds5['rainnc'].sel(lon=slice(86.6, 87.2), lat=slice(21.1, 21.6)).isel(time=48).mean().values.item()
f = ds6['rainnc'].sel(lon=slice(85.1, 85.5), lat=slice(23.1, 23.5)).isel(time=48).mean().values.item()
g = ds7['rainnc'].sel(lon=slice(86.6, 87.2), lat=slice(21.1, 21.6)).isel(time=48).mean().values.item()
h = ds8['rainnc'].sel(lon=slice(85.1, 85.5), lat=slice(23.1, 23.5)).isel(time=48).mean().values.item()# This case actual time is 17 step
i = ds9['rainnc'].sel(lon=slice(86.6, 87.2), lat=slice(21.1, 21.6)).isel(time=48).mean().values.item()# This case actual time is 17 step
j = ds10['rainnc'].sel(lon=slice(85.1, 85.5), lat=slice(23.1, 23.5)).isel(time=48).mean().values.item()

# Define data
x = ['   Ferr', '   Milb', '   Thom', '   Morr', '   Wsm6', '  obs']
y1 = [a, c, e, g, i, dsa]
y2 = [b, d, f, h, j, dsb]

# Bar width
x_positions = np.arange(len(x))  # X positions for the bars
bar_width = 0.3

# Plot
fig = plt.figure(figsize=(4.8, 3.3))
gs = gridspec.GridSpec(1, 1, wspace=0.1, hspace=0.01)
fig.patch.set_facecolor('white')  # Set background color for the figure
ax1 = fig.add_subplot(gs[0, 0])
# ax1.set_facecolor('lightyellow')  # Set background color for the plot area

# Create bars
ax1.bar(x_positions - bar_width/2, y1, bar_width, label='case 1', color='red')
ax1.bar(x_positions + bar_width/2, y2, bar_width, label='case 2', color='blue')
# ax1.axhline(y=9, color='red', linestyle='--', linewidth=1)
# ax1.axhline(y=10, color='blue', linestyle='--', linewidth=1)

# Customize plot
ax1.set_xticks(x_positions)
ax1.set_xticklabels(x, rotation=45, ha='center')

# ax1.set_yticklabels(y1, rotation=0, ha='center')
# ax1.set_yticklabels(y2, rotation=0, ha='center')

# Adjust distance of labels from the axis
# ax1.tick_params(axis='x', pad=0)  # Move labels farther away from the axis
# plt.xlabel('WRF Physics', fontsize=12, fontweight='bold')
plt.ylabel('rainnc (mm)', fontsize=10, fontweight='bold')
ax1.tick_params(axis='both', length=5, width=1.2, labelsize=12)
# ax1.set_yticklabels([4, 14])# Add legend
ax1.legend()
# Axis and ticks formatting
ax1.set_yticks(np.arange(0, 40.1, 5))
ax1.set_ylim([0, 38])
ax1.tick_params(axis='y', rotation=0)  # Rotate y-axis labels (if needed)

# ax1.set_position([0.755, 0.2, 0.65, 0.6])  # Adjust colorbar position: [left, bottom, width, height]

# ax1.set_xticks(np.arange(80, 90.1, 1))
# ax1.set_xlim([80, 90])
# Update plot settings
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 12,
    'ytick.labelsize': 14,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 12,
    'ytick.major.size': 12,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 16,  # For axes titles
    'figure.titlesize': 18  # For overall figure title
})
# plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.3)
plt.tight_layout()
plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/accumulated_precipitatio_barplot.png', dpi=500, bbox_inches='tight')
plt.show()

