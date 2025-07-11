import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Function to calculate terminal velocity based on diameter
def terminal_velocity(diameter):
    g = 9.81  # acceleration due to gravity (m/s^2)
    rho_hail = 917  # density of hail (kg/m^3)
    rho_air = 1.225  # density of air (kg/m^3)
    Cd = 0.47  # drag coefficient for a sphere

    radius = diameter / 2
    volume = (4 / 3) * np.pi * radius**3
    mass = rho_hail * volume
    A = np.pi * radius**2

    v_t = np.sqrt((2 * mass * g) / (rho_air * Cd * A))
    return v_t, radius  # Return both terminal velocity and radius
l = np.arange(150, 550.1, 50)
# Load the NetCDF files
ds12 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20190315.nc')
ds22 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20200303.nc')

# Process hail diameter and calculate terminal velocity for both datasets
def process_hailcast(ds, time_indices):
    hd = ds['hailcast_d'].isel(time=time_indices).mean(dim='time').squeeze()
    hd_values = hd.values  # Convert to a NumPy array
    lon = ds['lon'].values
    lat = ds['lat'].values

    terminal_velocities = np.zeros(hd_values.shape)
    radii = np.zeros(hd_values.shape)

    for i in range(hd_values.shape[0]):
        for j in range(hd_values.shape[1]):
            v_t, r = terminal_velocity(hd_values[i, j])
            terminal_velocities[i, j] = v_t
            radii[i, j] = r

    return lon, lat, terminal_velocities, radii

lon1, lat1, terminal_velocities1, radii1 = process_hailcast(ds12, [16, 17, 25, 26, 32])
lon2, lat2, terminal_velocities2, radii2 = process_hailcast(ds22, [15, 16, 17, 18, 19, 24, 25, 26, 32])

# # Plotting the results
fig = plt.figure(figsize=(12, 6))
gs = gridspec.GridSpec(1, 2, wspace=0.115, hspace=0.25)

# # Plot for the first dataset
ax1 = fig.add_subplot(gs[0, 0], projection=ccrs.PlateCarree())
pcm1 = ax1.contourf(lon1, lat1, terminal_velocities1, levels = l, cmap='jet', shrink=0.4)
# cbar1 = plt.colorbar(pcm1, ax=ax1, orientation='vertical', shrink=0.7)
# cbar1.set_label('Terminal Velocity (m/s)')
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
# ax1.set_title('(a) Ranchi 20190315')
# First subplot: ax1
ax1.set_xticks(np.arange(82, 88.61, 1))
ax1.set_yticks(np.arange(21, 25.1, 1))
ax1.set_xlim([82, 88.1])
ax1.set_ylim([21, 25.1])
ax1.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(82, 88.61, 1)], fontsize=13, fontweight='bold', rotation=45)
ax1.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 25.1, 1)], fontsize=13, fontweight='bold', rotation=45)
ax1.tick_params(axis='both', length=8, width=1.4)
# Plot for the second dataset
ax2 = fig.add_subplot(gs[0, 1], projection=ccrs.PlateCarree())
pcm2 = ax2.contourf(lon2, lat2, terminal_velocities2, levels = l, cmap='jet', shrink=0.4)
cbar2 = plt.colorbar(pcm2, ax=[ax1, ax2], orientation='vertical')
cbar2.set_label('Terminal Velocity (m/s)')
cbar2.ax.tick_params(axis='both', labelsize=10, length=5, width=1.2)  # Use 'labelsize' to adjust tick font size
cbar2.ax.set_position([0.755, 0.27, 0.2, 0.4])  # Left, Bottom, Width, Height
ax2.set_xlabel('Longitude')
# ax2.set_ylabel('Latitude')
# ax2.set_title('(b) Ranchi 20200303')
ax2.set_xticks(np.arange(82, 88.61, 1))
ax2.set_yticks(np.arange(21, 25.1, 1))
ax2.set_xlim([82, 88.1])
ax2.set_ylim([21, 25.1])

# Modify the X-tick labels to show longitude with "E"
ax2.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(82, 88.61, 1)], fontsize=13, fontweight='bold', rotation=45)
ax2.tick_params(axis='both', length=8, width=1.4)
# Hide Y-tick labels for ax2
ax2.set_yticklabels([])

# Add coastlines, borders, and states for both subplots
for ax in [ax1, ax2]:
    ax.coastlines(resolution='10m', color='black', linewidth=0.8)
    ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.5)
    ax.add_feature(cfeature.STATES.with_scale('10m'), edgecolor='black', linewidth=0.5)

ax1.set_title('(a) case 1', fontsize=14, fontweight='bold')
ax2.set_title('(b) case 2', fontsize=14, fontweight='bold')

# Adjust layout and show the plot
ax1.set_xlabel('lon')
ax1.set_ylabel('lat')
ax2.set_xlabel('lon')
plt.suptitle('Terminal velocity (Vt)', fontsize=16, fontweight='bold', x=0.44, y=0.78)# Update plot parameters for font size, boldness, and tick sizes
plt.rcParams.update({
    "font.weight": "bold",          # Set the default font weight to bold
    "axes.labelweight": "bold",     # Axis label font weight
    'xtick.labelsize': 10,          # X-axis tick label size
    'ytick.labelsize': 10,          # Y-axis tick label size
    "axes.linewidth": 2,            # Line width for the axes
    "patch.linewidth": 2,           # Line width for patches (e.g., circles, rectangles)
    'xtick.major.size': 8,         # Major tick size for X-axis
    'ytick.major.size': 8,         # Major tick size for Y-axis
    'xtick.major.width': 2,         # Major tick width for X-axis
    'ytick.major.width': 2,         # Major tick width for Y-axis
    'axes.titlesize': 16,           # Font size for subplot (ax1, ax2) titles
    'axes.titleweight': 'bold',     # Font weight for subplot titles
    'figure.titlesize': 16,         # Font size for the overall figure title (suptitle)
    'figure.titleweight': 'bold',   # Font weight for the overall figure title
})
plt.show()
