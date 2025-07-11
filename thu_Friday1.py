

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from metpy.units import units
from metpy.calc import parcel_profile, dewpoint_from_relative_humidity, cape_cin
import metpy.calc
import matplotlib as mpl
import pint
import metpy.calc as mpcalc
# Set matplotlib path chunk size to handle large datasets
mpl.rcParams['agg.path.chunksize'] = 10000
# Open dataset
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/ERA5data/20200303.nc')
# Extract temperature and RH, selecting all time steps
temp = ds1['t'].values - 273.16  # Convert to Celsius
rh = ds1['r'].values  # Extract RH
time_steps, levels, lat, lon = temp.shape  # Extract dimensions
# Extract pressure levels (assuming it's 1D with shape (27,))
pressure = ds1['pressure_level'].values  # Shape (27,)
# Expand pressure to 4D shape (time, levels, lat, lon)
pressure = np.tile(pressure[np.newaxis, :, np.newaxis, np.newaxis], (time_steps, 1, lat, lon))
# Assign MetPy units
pressure = pressure * units.hPa
temp = temp * units.degC
rh = rh / 100.0  # Convert RH percentage to fraction (0-1)
# Compute dewpoint temperature (same shape as temp)
Td = dewpoint_from_relative_humidity(temp, rh)
# Compute parcel profile for all time steps
prof = np.empty((time_steps, levels, lat, lon), dtype=object)  # Placeholder for profiles

for t in range(time_steps):  # Loop over time steps
    for pl in range(levels):
        for i in range(lat):
            for j in range(lon):
                prof[t, pl, i, j] = parcel_profile(pressure[t, pl, i, j], temp[t, pl, i, j], Td[t, pl, i, j][0]).to('degC')
# prof = prof * units.degC
tim_steps, level, lat1, lon1 = temp.shape  # Extract dimensions
ureg = pint.UnitRegistry()  # Or u.UnitRegistry() from astropy.units
cape_units = ureg.J / ureg.kg  # Example units for CAPE
cin_units = ureg.J / ureg.kg   # Example units for CIN
prof = prof * ureg.degC# Create regular NumPy arrays to store the NUMERICAL values
cape_data = np.zeros((tim_steps, level, lat1, lon1), dtype=float)  # Or appropriate dtype
cin_data = np.zeros((tim_steps, level, lat1, lon1), dtype=float)
for t in range(tim_steps):
    for i in range(lat1):
        for j in range(lon1):
            # Extract magnitudes
            # p_val = pressure[t, p, i, j].magnitude
            # T_val = temp[t, p, i, j].magnitude
            # Td_val = Td[t, p, i, j].magnitude
            # prof = prof[t, p, i, j].magnitude

            cape, cin = metpy.calc.cape_cin(pressure[t, :, i, j], temp[t, :, i, j], Td[t, :, i, j], prof[t, :, i, j])
                
                
                
                
                
# import numpy as np
# import pint

# # Initialize Pint Unit Registry
# ureg = pint.UnitRegistry()

# # Example dimensions based on `temp.shape`
# tim_steps, level, lat1, lon1 = 10, 20, 50, 50  # Example dimensions (modify as needed)

# # Generate random profile data
# prof_data = np.random.rand(tim_steps, level, lat1, lon1)  # Raw numerical values

# # ✅ Assign units correctly and convert to Kelvin (avoiding offset errors)
# prof = prof_data * ureg.degC  # Assign °C
# prof = prof.to(ureg.K)  # Convert °C to Kelvin (solves OffsetUnitCalculusError)

# # ✅ Extract numerical values as NumPy array
# prof_array = prof.magnitude  # Now `prof_array` is pure numerical values

# # Define CAPE and CIN units
# cape_units = ureg.J / ureg.kg  
# cin_units = ureg.J / ureg.kg  

# # Initialize output arrays
# cape_data = np.zeros((tim_steps, level, lat1, lon1), dtype=float)
# cin_data = np.zeros((tim_steps, level, lat1, lon1), dtype=float)

# # Define a function for CAPE/CIN calculations
# def calculate_cape_cin(p, T, Td, prof):
#     """
#     Dummy function to compute CAPE and CIN.
#     Replace with actual formula (e.g., using MetPy).
#     """
#     cape = np.random.rand() * 1000  # Fake CAPE value
#     cin = np.random.rand() * -50  # Fake CIN value
#     return cape, cin

# # Loop through dataset
# for t in range(tim_steps):
#     for p in range(level):
#         for i in range(lat1):
#             for j in range(lon1):
#                 # Extract magnitude values
#                 prof_val = prof_array[t, p, i, j]  # Now `prof_array` is pure numerical

#                 # Compute CAPE & CIN (replace with actual calculation)
#                 cape, cin = calculate_cape_cin(0, 0, 0, prof_val)  # Replace 0s with real values

#                 # Store results
#                 cape_data[t, p, i, j] = cape
#                 cin_data[t, p, i, j] = cin

# # Convert arrays to Pint Quantities
# cape_data = cape_data * cape_units
# cin_data = cin_data * cin_units

# # Print shape confirmation
# print("CAPE shape:", cape_data.shape)
# print("CIN shape:", cin_data.shape)
import metpy.calc as mpcalc
from metpy.units import units
import numpy as np

# Example dimensions
tim_steps = 10
levels = 20  # Vertical levels
lat, lon = 50, 50  # Grid size

# Example data (random for demo)
pressure = np.linspace(1000, 100, levels)[:, np.newaxis, np.newaxis] * units.hPa
temp = np.random.uniform(-40, 30, (tim_steps, levels, lat, lon)) * units.degC
Td = np.random.uniform(-50, 20, (tim_steps, levels, lat, lon)) * units.degC

# Initialize CAPE array (3D CAPE)
cape_data = np.zeros((tim_steps, levels, lat, lon))

for t in range(tim_steps):  # Time loop
    for p in range(levels):  # Loop over vertical levels
        for i in range(lat):
            for j in range(lon):
                # Compute CAPE at each level
                try:
                    cape, cin = mpcalc.cape_cin(
                        pressure[:, i, j],  # Full vertical pressure profile
                        temp[t, :, i, j],  # Full vertical temperature profile
                        Td[t, :, i, j],  # Full vertical dew point profile
                        parcel_profile=mpcalc.parcel_profile(pressure[:, i, j], temp[t, p, i, j], Td[t, p, i, j])
                    )
                    cape_data[t, p, i, j] = cape.magnitude  # Store CAPE for that level
                except:
                    cape_data[t, p, i, j] = np.nan  # Handle errors

import matplotlib.pyplot as plt

# Select a specific lat-lon point
lat_index, lon_index = 25, 25  # Adjust as needed

plt.figure(figsize=(6, 8))
plt.plot(cape_data[0, :, lat_index, lon_index], pressure[:, 0, 0], label="CAPE Profile")
plt.gca().invert_yaxis()  # Invert y-axis (Pressure decreases with height)
plt.xlabel("CAPE (J/kg)")
plt.ylabel("Pressure (hPa)")
plt.title("Vertical CAPE Profile")
plt.legend()
plt.show()
