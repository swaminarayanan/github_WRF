import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from metpy.calc import specific_humidity_from_mixing_ratio
from metpy.units import units
import matplotlib as mpl

# Set matplotlib path chunk size to handle large datasets
mpl.rcParams['agg.path.chunksize'] = 10000

# Load the datasets
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')

# Extract the mixing ratio (qvapor) from both datasets (no need for degC unit conversion)
m1 = ds1['qvapor']  # Dataset 1: mixing ratio
m2 = ds2['qvapor']  # Dataset 2: mixing ratio

# Calculate specific humidity from mixing ratio
sh1 = specific_humidity_from_mixing_ratio(m1)  # Dataset 1 specific humidity
sh2 = specific_humidity_from_mixing_ratio(m2)  # Dataset 2 specific humidity
sh1 = sh1.data
sh2 = sh2.data


# Combine the specific humidity (sh1) into an xarray Dataset for 2019 data
ds1_sh = xr.Dataset({
    'specific_humidity': (['time', 'lev', 'lat', 'lon'], sh1)
}, coords={
    'time': ds1['time'],
    'lev': ds1['lev'],
    'lat': ds1['lat'],
    'lon': ds1['lon']
})

# Save the 2019 dataset to a NetCDF file
output_filename1 = 'specific_humidity_20190421.nc'
ds1_sh.to_netcdf(output_filename1)

# Combine the specific humidity (sh2) into an xarray Dataset for 2020 data
ds2_sh = xr.Dataset({
    'specific_humidity': (['time', 'lev', 'lat', 'lon'], sh2)
}, coords={
    'time': ds2['time'],
    'lev': ds2['lev'],
    'lat': ds2['lat'],
    'lon': ds2['lon']
})

# Save the 2020 dataset to a NetCDF file
output_filename2 = 'sh_2020.nc'
ds2_sh.to_netcdf(output_filename2)

print(f"Data saved to {output_filename1} and {output_filename2}")
