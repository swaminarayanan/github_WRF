import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from metpy.units import units
import metpy.calc as mpcalc
import matplotlib as mpl

# Set matplotlib path chunk size to handle large datasets
mpl.rcParams['agg.path.chunksize'] = 10000

# Load the datasets
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20190315.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20200303.nc')

# Extract the u and v wind components and assign units (meters per second)
ds1uwind = ds1['u'].metpy.quantify() * units('m/s')  # u-wind in meters per second
ds1vwind = ds1['v'].metpy.quantify() * units('m/s')  # v-wind in meters per second
ds2uwind = ds2['u'].metpy.quantify() * units('m/s')  # u-wind in meters per second
ds2vwind = ds2['v'].metpy.quantify() * units('m/s')  # v-wind in meters per second

# Compute vorticity and divergence
vort1 = mpcalc.vorticity(ds1uwind, ds1vwind)
vort2 = mpcalc.vorticity(ds2uwind, ds2vwind)
div1 = mpcalc.divergence(ds1uwind, ds1vwind)
div2 = mpcalc.divergence(ds2uwind, ds2vwind)
vort1 = vort1.data
vort2 = vort2.data
div1 = div1.data
div2 = div2.data


# Combine the relative vorticity and divergence into an xarray Dataset for 2019 data
ds1_sh = xr.Dataset({
    'relative_vorticity': (['time', 'lev', 'lat', 'lon'], vort1),
    'divergence': (['time', 'lev', 'lat', 'lon'], div1)
}, coords={
    'time': ds1['time'],
    'lev': ds1['lev'],
    'lat': ds1['lat'],
    'lon': ds1['lon']
})

# Save the 2019 dataset to a NetCDF file
output_filename1 = 'rvdv_2019.nc'
ds1_sh.to_netcdf(output_filename1)

# Combine the relative vorticity and divergence into an xarray Dataset for 2020 data
ds2_sh = xr.Dataset({
    'relative_vorticity': (['time', 'lev', 'lat', 'lon'], vort2),
    'divergence': (['time', 'lev', 'lat', 'lon'], div2)
}, coords={
    'time': ds2['time'],
    'lev': ds2['lev'],
    'lat': ds2['lat'],
    'lon': ds2['lon']
})

# Save the 2020 dataset to a NetCDF file
output_filename2 = 'rvdv_2020.nc'
ds2_sh.to_netcdf(output_filename2)

print(f"Data saved to {output_filename1} and {output_filename2}")


