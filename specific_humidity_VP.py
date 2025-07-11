
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Load the datasets
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/specifichumidity_2019.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/specifichumidity_2020.nc')

# Select data for a specific lat/lon range and time steps using integer slicing
ds1 = ds1.sel(lat=slice(23, 23.6), lon=slice(85, 85.6)).isel(time=20)  # Select first 20 time steps
ds2 = ds2.sel(lat=slice(23, 23.6), lon=slice(85, 85.6)).isel(time=17)  # Select first 17 time steps

sh1 = ds1['specific_humidity'].mean(dim=['lat', 'lon']).squeeze().values# - 273.16
sh2 = ds2['specific_humidity'].mean(dim=['lat', 'lon']).squeeze().values# - 273.16

# Create the figure and GridSpec with 3 columns and 1 row
fig = plt.figure(figsize=(12, 12))
gs = gridspec.GridSpec(1, 1)#, width_ratios=[4, 4, 4])  # Adjusted to 3 columns

# Plot theta_e
ax1 = fig.add_subplot(gs[0, 0])  # First column
mpl.rcParams['figure.facecolor'] = 'white'
# ax1.plot(te1, ds3['lev'], color='k', label='θₑ1')
# ax1.plot(te2, ds4['lev'], color='r', label='θₑ2')
# Plot with line and marker styles
ax1.plot(sh1, ds1['lev'], color='k', linestyle='-', marker='*', label='specific_humidity1')  # Dashed line with star markers
ax1.plot(sh2, ds2['lev'], color='r', linestyle='-', marker='*', label='specific_humidity2')   # Solid line with star markers
ax1.set_xticks(np.arange(0.00, 0.0091, 0.001))  # X-axis ticks from 0 to 150, step 20
ax1.set_xticks(np.arange(0.00, 0.0091, 0.001))  # X-axis ticks from 0 to 150, step 20
# ax1.plot(tc1, ds1['lev'], color='g', label='θₑ1')
# ax1.plot(tc2, ds2['lev'], color='r', label='θₑ2')
ax1.set_title('(a) specific humidity', fontweight='bold')
ax1.set_ylabel('Pressure Level', fontweight='bold', fontsize=16)
ax1.set_xlabel('spec_hum (m/kg)', fontweight='bold', fontsize=16)
ax1.legend()
ax1.invert_yaxis()
# Generate 7 evenly spaced ticks using numpy.linspace
# Set x and y ticks using np.arange() with 7 steps
ax1.set_yticks(np.arange(100, 1000.1, 100))  # Y-axis ticks from 0 to 1000, step 100

# Rotate the x-axis tick labels by 90 degrees
ax1.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
ax1.tick_params(axis='y', rotation=90)  # Rotate y-axis labels (if needed)
# # Plot RH
# ax2 = fig.add_subplot(gs[0, 1])  # Second column
# mpl.rcParams['figure.facecolor'] = 'white'
# ax2.plot(rh1, ds1['lev'], color='k', linestyle='-', marker='*', label='RH1')
# ax2.set_xticks(np.arange(0, 100.1, 20))  # X-axis ticks from 0 to 150, step 20
# ax2.plot(rh2, ds2['lev'], color='r', linestyle='-', marker='*', label='RH2')
# ax2.set_title('(b) RH', fontweight='bold')
# ax2.set_xticks(np.arange(0, 100.1, 20))  # X-axis ticks from 0 to 150, step 20
# # ax2.set_ylabel('Pressure Level', fontweight='bold', fontsize=16)
# ax2.set_xlabel('RH (%)', fontweight='bold', fontsize=16)
# ax2.legend()
# ax2.invert_yaxis()
# # Set x and y ticks using np.arange() with 7 steps
# ax2.set_yticks(np.arange(100, 1000.1, 100))  # Y-axis ticks from 0 to 1000, step 100

# # Rotate the x-axis tick labels by 90 degrees
# ax2.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
# ax2.tick_params(axis='y', rotation=90)  # Rotate y-axis labels (if needed)

# # Plot vertical velocity (w)tc
# ax3 = fig.add_subplot(gs[0, 2])  # Third column
# mpl.rcParams['figure.facecolor'] = 'white'
# ax3.plot(w1, ds1['lev'], color='k', linestyle='-', marker='*', label='W1')
# ax3.set_xticks(np.arange(-0.08, 0.31, 0.05))  # X-axis ticks from 0 to 150, step 20
# ax3.plot(w2, ds2['lev'], color='r', linestyle='-', marker='*', label='W2')
# ax3.set_title('(c) Vertical Velocity', fontweight='bold')
# ax3.set_xticks(np.arange(-0.1, 0.32, 0.05))  # X-axis ticks from 0 to 150, step 20
# # ax3.set_ylabel('Pressure Level', fontweight='bold', fontsize=16)
# ax3.set_xlabel('velocity (m/s)', fontweight='bold', fontsize=16)

# ax3.legend()
# ax3.invert_yaxis()
# # Set x and y ticks using np.arange() with 7 steps
# ax3.set_yticks(np.arange(100, 1000.1, 100))  # Y-axis ticks from 0 to 1000, step 100

# # Rotate the x-axis tick labels by 90 degrees
# ax3.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
# ax3.tick_params(axis='y', rotation=90)  # Rotate y-axis labels (if needed)
# Update plotting parameters
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 18,
    'ytick.labelsize': 18,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 12,
    'ytick.major.size': 12,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 16,  # For axes titles
    'figure.titlesize': 20  # For overall figure title
})

plt.tight_layout()
plt.show()
