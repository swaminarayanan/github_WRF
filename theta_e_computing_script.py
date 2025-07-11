import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from metpy.calc import equivalent_potential_temperature
from metpy.units import units
import matplotlib as mpl

# Set the agg.path.chunksize to avoid overflow issues
mpl.rcParams['agg.path.chunksize'] = 10000

# Load the datasets
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20200303.nc')

# Dimensions: (time: 49, lev: 24, lat: 609, lon: 549)
# Isolate pressure, temperature, and dewpoint (all 4D: time, lev, lat, lon)
p1 = ds1['pressure'] * units.hPa  # Dataset 1: pressure
T1 = ds1['tc'] * units.degC       # Dataset 1: temperature
Td1 = ds1['td'] * units.degC      # Dataset 1: dewpoint

p2 = ds2['pressure'] * units.hPa  # Dataset 2: pressure
T2 = ds2['tc'] * units.degC       # Dataset 2: temperature
Td2 = ds2['td'] * units.degC      # Dataset 2: dewpoint

###########################################
# Calculate the equivalent potential temperature (theta_e) for both datasets
theta_e1 = equivalent_potential_temperature(p1, T1, Td1)  # Dataset 1
theta_e2 = equivalent_potential_temperature(p2, T2, Td2)  # Dataset 2

# Extract the numpy data using .data or .values
theta_e1_data = theta_e1.data  # or use .values
theta_e2_data = theta_e2.data  # or use .values

# Combine theta_e1 into an xarray Dataset for 2019 data
ds1_theta = xr.Dataset({
    'theta_e1': (['time', 'lev', 'lat', 'lon'], theta_e1_data)  # Use extracted data
}, coords={
    'time': ds1['time'],
    'lev': ds1['lev'],
    'lat': ds1['lat'],
    'lon': ds1['lon']
})

# Save the 2019 dataset to a NetCDF file
output_filename1 = 'theta_e_wsm6_20190421.nc'
ds1_theta.to_netcdf(output_filename1)

# Combine theta_e2 into an xarray Dataset for 2020 data
ds2_theta = xr.Dataset({
    'theta_e2': (['time', 'lev', 'lat', 'lon'], theta_e2_data)  # Use extracted data
}, coords={
    'time': ds2['time'],
    'lev': ds2['lev'],
    'lat': ds2['lat'],
    'lon': ds2['lon']
})

# Save the 2020 dataset to a NetCDF file
output_filename2 = 'theta_e_wsm6_20200303.nc'
ds2_theta.to_netcdf(output_filename2)

print(f"Data saved to {output_filename1} and {output_filename2}")
