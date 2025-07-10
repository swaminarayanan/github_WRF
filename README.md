
#########WRF-model Simulation with different microphysics schemes
###### Dissertation Title ########
######Numerical Modelling of Hailstorm Events Over Eastern India: Role of microphysics and orographic lifting

This project simulates premonsoon hailstorm events over Eastern India of different geographical locations by using the WRF model

This hailstorms geographical locations are located in case1: coastal land(2019/04/21) and case2: elevated inland(2020/03/03)
--Below are the outputs and sample plots.

## Features
- WRF simulations for hailstorm events
1) Evaluating the sensitivity of different microphysics parameterization on hailstorm
simulation.
2) Analyzing the convective behaviour of hailstorms by using Skew-T Log-P diagrams.
3) Segregating different triggering mechanisms for the development of the hailstorm.

- Spatial masking using shapefiles (India provinces)
- Python scripts for visualization and analysis
## Requirements
- Python: xarray, matplotlib, netCDF4, numpy, shapely.geometry, geopandas, cartopy, cartopy cfeatures, datetime, etc,

## 📜 Python Scripts
- `script.py`: Processes NetCDF files and plots maps
- `hail_plot.py`: Plots hailstorm intensity using `matplotlib` and `cartopy`
