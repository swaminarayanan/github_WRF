import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20200303/gfs.0p25.2020032300.f000.grib2'

# Open the GRIB file
with pygrib.open(file_path) as grbs:
    for grb in grbs:
        print(f"Message: {grb.messagenumber}")
        print(f"Name: {grb.name}")
        print(f"Short name: {grb.shortName}")
        print(f"Level: {grb.level}")
        print(f"Date: {grb.dataDate}")
        print(f"Time: {grb.dataTime}")
        print(f"Units: {grb.units}")
        print(f"Latitudes and Longitudes shape: {grb.latlons()[0].shape}")
        print("-----")

########################################

import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20200303/gfs.0p25.2020032300.f000.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# List to store variable information
variables = []

# Loop through each message in the GRIB file
for grb in grbs:
    var_info = (grb.parameterName, grb.typeOfLevel, grb.level)
    variables.append(var_info)
    print(f"Variable: {grb.parameterName}, Type of Level: {grb.typeOfLevel}, Level: {grb.level}")

# Print the number of variables
print(f"\nTotal number of variables: {len(variables)}")

# Close the GRIB file
grbs.close()

#######################################
import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20200323/gfs.0p25.2020032300.f000.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# List to store specific humidity variable information
temperature_vars = []

# Loop through each message in the GRIB file
for grb in grbs:
    # Check if the variable is Specific Humidity
    if grb.parameterName == 'cape':
        var_info = (grb.parameterName, grb.typeOfLevel, grb.level)
        temperature_vars.append(var_info)
        print(f"Variable: {grb.parameterName}, Type of Level: {grb.typeOfLevel}, Level: {grb.level}")

# Print the number of Specific Humidity variables
print(f"\nTotal number of temperature variables: {len(temperature_vars)}")

# Close the GRIB file
grbs.close()
#############################################
import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20200323/gfs.0p25.2020032300.f000.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# List to store CAPE variable information
Relative_humidity_vars = []

# Loop through each message in the GRIB file
for grb in grbs:
    # Check if the variable is Convective Available Potential Energy
    if grb.parameterName == 'Relative humidity':
        var_info = (grb.parameterName, grb.typeOfLevel, grb.level)
        Relative_humidity_vars.append(var_info)
        print(f"Variable: {grb.parameterName}, Type of Level: {grb.typeOfLevel}, Level: {grb.level}")

# Print the number of CAPE variables
print(f"\nTotal number of Relative humidity variables: {len(Relative_humidity_vars)}")

# Close the GRIB file
grbs.close()


###################
import pygrib

# Replace with the path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20200323/gfs.0p25.2020032300.f000.grib2'
grbs = pygrib.open(file_path)

# Display basic information about each message in the GRIB file
for i, grb in enumerate(grbs):
    print(f"Message {i + 1}")
    print("Parameter:", grb.parameterName)
    print("Level:", grb.level)
    print("Data Date:", grb.dataDate)
    print("Forecast Time:", grb.forecastTime)
    print("Valid Date:", grb.validDate)
    print("Units:", grb.units)
    print("Shape of Data:", grb.values.shape)
    print("-" * 30)





# Collect unique parameters and levels in the file
parameters = set()
for grb in grbs:
    parameters.add((grb.parameterName, grb.level))

print("Available Parameters and Levels:")
for param, level in parameters:
    print(f"{param} at level {level}")



import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20190315/gfs.0p25.2019031500.f000.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# Iterate through each message in the GRIB file and print variable details
print("Available variables in the GRIB file:")
for grb in grbs:
    print(f"Variable: {grb.name}, Level Type: {grb.typeOfLevel}, Level: {grb.level}, Units: {grb.units}")

# Close the GRIB file
grbs.close()


import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20190315/gfs.0p25.2019031500.f000.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# List to store Geopotential Height variable information
geopotential_height_vars = []

# Loop through each message in the GRIB file
for grb in grbs:
    # Check if the variable is Geopotential Height at isobaricInhPa levels
    if grb.parameterName == 'Geopotential height' and grb.typeOfLevel == 'isobaricInhPa':
        var_info = (grb.parameterName, grb.typeOfLevel, grb.level)
        geopotential_height_vars.append(var_info)
        print(f"Variable: {grb.parameterName}, Type of Level: {grb.typeOfLevel}, Level: {grb.level}")

# Print the number of Geopotential Height variables found
print(f"\nTotal number of Geopotential height variables: {len(geopotential_height_vars)}")

# Close the GRIB file
grbs.close()

#################
import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20190315/gfs.0p25.2019031500.f000.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# List to store Geopotential Height variable information
geopotential_height_vars = []

# Loop through each message in the GRIB file
for grb in grbs:
    # Check if the variable is Geopotential Height at isobaricInhPa levels
    if grb.parameterName == 'Geopotential height' and grb.typeOfLevel == 'isobaricInhPa':
        var_info = (grb.parameterName, grb.typeOfLevel, grb.level)
        geopotential_height_vars.append(var_info)
        print(f"Variable: {grb.parameterName}, Type of Level: {grb.typeOfLevel}, Level: {grb.level}")

# Print the number of Geopotential Height variables found
print(f"\nTotal number of Geopotential height variables: {len(geopotential_height_vars)}")

# Close the GRIB file
grbs.close()
###############################
import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20190315/gfs.0p25.2019031500.f000.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# List to store Specific Humidity variable information
specific_humidity_vars = []

# Loop through each message in the GRIB file
for grb in grbs:
    # Check if the variable is Specific Humidity at pressureFromGroundLayer levels
    if grb.parameterName == 'Specific humidity' and grb.typeOfLevel == 'heightAboveGround':
        var_info = (grb.parameterName, grb.typeOfLevel, grb.level)
        specific_humidity_vars.append(var_info)
        print(f"Variable: {grb.parameterName}, Type of Level: {grb.typeOfLevel}, Level: {grb.level}")

# Print the number of Specific Humidity variables found
print(f"\nTotal number of Specific humidity variables: {len(specific_humidity_vars)}")

# Close the GRIB file
grbs.close()
####################################3
import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20190315/gfs.0p25.2019031500.f000.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# List to store Temperature variable information
temperature_vars = []

# Loop through each message in the GRIB file
for grb in grbs:
    # Check if the variable is a type of Temperature
    if 'temperature' in grb.parameterName.lower():
        var_info = (grb.parameterName, grb.typeOfLevel, grb.level)
        temperature_vars.append(var_info)
        print(f"Variable: {grb.parameterName}, Type of Level: {grb.typeOfLevel}, Level: {grb.level}")

# Print the number of Temperature variables found
print(f"\nTotal number of Temperature variables: {len(temperature_vars)}")

# Close the GRIB file
grbs.close()
################################
import pygrib

# Path to your GRIB2 file
file_path = '/media/lab/My Passport/hail/gfs/20190315/gfs.0p25.2019031500.f006.grib2'

# Open the GRIB file
grbs = pygrib.open(file_path)

# List to store Relative Humidity variable information
relative_humidity_vars = []

# Loop through each message in the GRIB file
for grb in grbs:
    # Check if the variable is Relative Humidity at heightAboveGround levels
    if grb.parameterName == 'Relative humidity' and grb.typeOfLevel == 'heightAboveGround':
        var_info = (grb.parameterName, grb.typeOfLevel, grb.level)
        relative_humidity_vars.append(var_info)
        print(f"Variable: {grb.parameterName}, Type of Level: {grb.typeOfLevel}, Level: {grb.level}")

# Print the number of Relative Humidity variables found
print(f"\nTotal number of Relative Humidity variables at heightAboveGround levels: {len(relative_humidity_vars)}")

# Close the GRIB file
grbs.close()
