
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
## Python Modules Requirements
- Python: xarray, matplotlib, netCDF4, numpy, shapely.geometry, geopandas, cartopy, cartopy cfeatures, datetime, metpy, scipy etc,

## 📜 Python Scripts
- orograpy_lifting.py : Segregating different triggering mechanisms for the development of the hailstorm
  Assessment of Orographic  influence over undulating terrain (10 times amplified vertical wind for visualization)
- skew-t_log-p_thermodynamic_parcel-prof.py : Analysing the convective behaviour of hailstorms by using Skew-T
  Log-P diagrams.
- hailcast_d_bar_plot_comparison.py : Inter comparison of Hailmaxd for different Microphysics experiments against the observation
- gpm_obs_precipitation_different shape_files.py : Various microphysic's Spatial distribution of accumulated rainfall of cases
- W_theta_qvap_cross_sectional _plot.py : Vertical Distribution during thunderstorm activity of cases
- case1&2_RH_T2m_lfc_etc_diff_schemes.py : Evaluating the sensitivity of different microphysics parameterization on hailstorm simulation
- Theta_e_W_Rh_vertical.py : vertical evaluation of key atmospheric factors responsible for triggering hailstorm development.
- cape_t_sh_contourf_sing_img.py : thunderstorm instability using CAPE, Temperature and Specific Humidity.
- script.py : Processes NetCDF files and plots maps
- hail_plot.py: Plots hailstorm intensity using `matplotlib` and `cartopy`
