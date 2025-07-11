import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib as mpl
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20190315.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20200303.nc')
ds3 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20190315.nc')
ds4 = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20200303.nc')
ds1 = ds1.sel(lat=slice(21.5, 24), lon=slice(84, 86.6))#.isel(time=20)
ds2 = ds2.sel(lat=slice(21.5, 24), lon=slice(84, 86.6))#.isel(time=16)
ds3 = ds3.sel(lat=slice(21.5, 24), lon=slice(84, 86.6))#.isel(time=20)
ds4 = ds4.sel(lat=slice(21.5, 24), lon=slice(84, 86.6))#.isel(time=16)

ds1 = ds3['rainnc']  # Assuming 'qice' exists in the dataset
ds1 = ds1.mean(dim=['lat', 'lon']).squeeze()  # Time-series data for levels
ds1 = ds1.diff(dim='time')# ds1 = ds1.isel(lev=1)
# Extract longitudeds2_mean and latitude
# times = ds1['time'].values  # Time values
# levels = ds1['lev'].values  # Pressure levels or model levels

# Example input sequence
sequence = ds1  # Replace ds1 with your actual sequence, e.g., [1, 2, 3, 4, 5]

# Handle odd-length sequences by removing the last element
if len(sequence) % 2 != 0:
    print(f"Sequence has an odd length ({len(sequence)}). Removing the last element: {sequence[-1]}")
    sequence = sequence[:-1]

# Calculate averages of consecutive pairs
averages = [(sequence[i] + sequence[i + 1]) / 2 for i in range(0, len(sequence), 2)]

# Convert the list of averages to a NumPy array
averages_array = np.array(averages)

# Print the values in column format without brackets
print("Averages as a column:")
for avg in averages_array:
    print(f"{avg:.4f}")