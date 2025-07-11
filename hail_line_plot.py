import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
import pandas as pd

# Load the NetCDF file (assuming hailcast_d is the variable)
ds = xr.open_dataset(r'/media/lab/My Passport/hail/milbrandt_20200303.nc')

# Subsetting the data to a small lat-lon range and squeezing to remove extra dimensions
ds = ds['hailcast_d'].sel(lat=slice(22.9, 23.1), lon=slice(84.97, 85.15)).squeeze()

# Calculate the mean of hailcast_d over lat and lon
hd = ds.mean(dim=('lat', 'lon')).values  # Assuming this is your data

# Extract the time variable from the dataset and convert it to pandas datetime format for plotting
time = pd.to_datetime(ds['time'].values)
# Plot setup
fig = plt.figure(figsize=(5, 2))
gs = gridspec.GridSpec(1, 1)
ax1 = fig.add_subplot(gs[0, 0])

# Plot the data
ax1.plot(time, hd, linewidth=3, color='grey')

# Step 1: Find the peak value and its corresponding time in the data
peak_idx = np.argmax(hd)  # Index of the peak value
peak_value = hd[peak_idx]  # Peak value of hd

# Step 2: Mark the peak value with a red star
ax1.plot(time[peak_idx], peak_value, marker='*', color='red', markersize=15, label='model')

# Step 3: Add a blue star at the 17th time step (time index 16)
ax1.plot(time[17], hd[17], marker='*', color='blue', markersize=6, label='observation')
ax1.legend()
# Rotate the labels for both x and y axis ticks
ax1.tick_params(axis='y', labelrotation=0)
ax1.tick_params(axis='x', labelrotation=90)

# Format the x-axis with hours (H) using matplotlib's date formatter
dtFmt = mdates.DateFormatter('%H')
ax1.xaxis.set_major_formatter(dtFmt)
# Set the title and axis labels
ax1.set_title('Area Cross Sectional Hail Diameter')
ax1.set_xlabel('Time (UTC)')
ax1.set_ylabel('Hail Diameter')

# Show the plot
plt.show()

# Close the plot to free up memory
plt.close(fig)
