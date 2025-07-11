import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from shapely.geometry import Point
from shapely.ops import unary_union
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
from netCDF4 import Dataset as netcdf
from scipy.stats import ttest_1samp
import pandas as pd
from matplotlib.patches import Circle
from metpy.units import units
from metpy.calc import parcel_profile
from metpy.units import units
import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import add_metpy_logo, Hodograph, SkewT

ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
# # ds1 = ds1.sel(lat=slice(22.926, 23.084), lon=slice(84.958, 85.121))#.isel(time=20)
# ds1 = ds1.sel(lat=21.49, lon=86.9, method='nearest')  # Single point
# ds2 = ds2.sel(lat=slice(21.5, 24), lon=slice(84, 86.6))#.isel(time=16)
ds1 = ds1.sel(lon=slice(86.87,86.95),lat=slice(21.44,21.53)).mean(dim=['lon', 'lat'])
ds2 = ds2.sel(lon=slice(85.21,85.41),lat=slice(23.26,23.46)).mean(dim=['lon', 'lat'])
pressure1 = ds1['pressure'].isel(time=18).squeeze()  # Assuming 'qice' exists in the dataset
wspd1 = ds1['wspd'].isel(time=18).squeeze()   # Assuming 'qice' exists in the dataset
wdir1 = ds1['wdir'].isel(time=18).squeeze()   # Assuming 'qice' exists in the dataset
hgt1 = ds1['height'].isel(time=18).squeeze()   # Assuming 'qice' exists in the dataset
dew_point1 = ds1['td'].isel(time=18).squeeze()   # Assuming 'qice' exists in the dataset
temperature1 = ds1['tc'].isel(time=18).squeeze()  # Assuming 'qice' exists in the dataset
valid_mask1 = ~np.isnan(pressure1)  # Mask to identify valid pressure values
#################
pressure2 = ds2['pressure'].isel(time=16).squeeze()  # Assuming 'qice' exists in the dataset
wspd2 = ds2['wspd'].isel(time=16).squeeze()   # Assuming 'qice' exists in the dataset
wdir2 = ds2['wdir'].isel(time=16).squeeze()   # Assuming 'qice' exists in the dataset
hgt2 = ds1['height'].isel(time=16).squeeze()   # Assuming 'qice' exists in the dataset
dew_point2 = ds2['td'].isel(time=16).squeeze()   # Assuming 'qice' exists in the dataset
temperature2 = ds2['tc'].isel(time=16).squeeze()  # Assuming 'qice' exists in the dataset
valid_mask2 = ~np.isnan(pressure2)  # Mask to identify valid pressure values
# Mask missing pressure values and corresponding data
##############case 1 ############
pressure1 = pressure1[valid_mask1] * units.hPa
temperature1 = temperature1[valid_mask1] * units.degC
dew_point1 = dew_point1[valid_mask1] * units.degC
wspd1 = wspd1[valid_mask1] * units.knots
wdir1 = wdir1[valid_mask1] * units.degrees
u1, v1 = mpcalc.wind_components(wspd1, wdir1)
##############case 2 ############
pressure2 = pressure2[valid_mask2] * units.hPa
temperature2 = temperature2[valid_mask2] * units.degC
dew_point2 = dew_point2[valid_mask2] * units.degC
wspd2 = wspd2[valid_mask2] * units.knots
wdir2 = wdir2[valid_mask2] * units.degrees
u2, v2 = mpcalc.wind_components(wspd2, wdir2)

# Create the Skew-T plot
fig = plt.figure(figsize=(19, 12))
gs = gridspec.GridSpec(1, 2, wspace=0.2)  # Adjusted to 3 columns
# Create Skew-T in the first column
ax1 = SkewT(fig, subplot=gs[0, 0])  # Correct
# ax1 = fig.add_subplot(gs[0, 0])  # First column

# Plot the temperature and dewpoint
ax1.plot(pressure1, temperature1, 'r', label=' Environment Temperature')
ax1.ax.legend(fontsize=10)

# ax1.plot(pressure1, dew_point1, 'g', label='Dewpoint')

# Add wind barbs
ax1.plot_barbs(pressure1, wspd1 * np.cos(np.deg2rad(wdir1)), wspd1 * np.sin(np.deg2rad(wdir1)))

# Calculate and plot the parcel profile
parcel_profile1 = parcel_profile(pressure1, temperature1[0], dew_point1[0])
ax1.plot(pressure1, parcel_profile1.values - 273.16, 'k', linestyle='--', label='Parcel Temperature')
ax1.ax.legend(fontsize=10)

# Add title and legend
ax1.ax.set_title('(a) case 1')
ax1.ax.legend(loc='center right')

# Add enhancements like dry adiabats, moist adiabats, and mixing lines
ax1.plot_dry_adiabats()
ax1.plot_moist_adiabats()
ax1.plot_mixing_lines()

# Create a hodograph
ax_hod1 = inset_axes(ax1.ax, '35%', '35%', loc=1)  # Place hodograph inside Skew-T plot
hodo1 = Hodograph(ax_hod1, component_range=60.1)
hodo1.add_grid(increment=15)
hodo1.plot_colormapped(u1, v1, hgt1[0:23])

# Show the plot
########## 2nd plot ##################
# Create Skew-T in the first column
ax2 = SkewT(fig, subplot=gs[0, 1])  

# Plot the temperature and dewpoint
ax2.plot(pressure2, temperature2, 'r', label='Environment Temperature')
ax2.ax.legend(fontsize=10)

# ax2.plot(pressure2, dew_point2, 'g', label='Dewpoint')

# Add wind barbs
ax2.plot_barbs(pressure2, wspd2 * np.cos(np.deg2rad(wdir2)), wspd2 * np.sin(np.deg2rad(wdir2)))

# Calculate and plot the parcel profile
parcel_profile2 = parcel_profile(pressure2, temperature2[0], dew_point2[0])
ax2.plot(pressure2, parcel_profile2.values - 273.16, 'k', linestyle='--', label='Parcel Temperature')
ax2.ax.legend(fontsize=10)


# Add title and legend
ax2.ax.set_title('(b) case 2')
ax2.ax.legend(loc='center right')

# Add enhancements like dry adiabats, moist adiabats, and mixing lines
ax2.plot_dry_adiabats()
ax2.plot_moist_adiabats()
ax2.plot_mixing_lines()

# Create a hodograph
ax_hod2 = inset_axes(ax2.ax, '35%', '35%', loc=1)  # Place hodograph inside Skew-T plot
hodo2 = Hodograph(ax_hod2, component_range=60.1)
hodo2.add_grid(increment=15)
hodo2.plot_colormapped(u2, v2, hgt2[3:23])

plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 10,
    'ytick.major.size': 10,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 20,  # For axes titles
    'figure.titlesize': 20  # For overall figure title
})# Show the plot
plt.tight_layout()
plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/Skewt_logp.png', dpi=500, bbox_inches='tight')

plt.show()
###########3Ruff for the short analyis 
# cmap = plt.get_cmap('jet')
# img = plt.contourf(ds2['lon'], ds2['lat'], ds2['cape'].isel(time=16, lev=2).squeeze(), cmap=cmap, shading='auto')
# cbar = plt.colorbar(img, ax=img, orientation='vertical', pad=0.02)
# cbar.set_label('CAPE (J/kg)')                                                                                    
