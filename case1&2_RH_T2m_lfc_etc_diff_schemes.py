import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib as mpl
import pandas as pd

file_path = "/home/lab/Desktop/Narayanswamy/work_scripts/2019_03_15_hail.xlsx"  # Replace with the path to your Excel file
sheet_name1 = "Sheet3"    # 20190315 Replace with the sheet name if necessary
df1 = pd.read_excel(file_path, sheet_name=sheet_name1)
x_column = "SNO"  # Serial number for x-axis
y_column = "T_ERR_19"  # Temperature error for y-axis
y1_column = "T_ERR_20"  # Temperature error for y-axis
y2_column = "TD_ERR_19"  # Temperature error for y-axis
y3_column = "TD_ERR_20"  # Temperature error for y-axis
y4_column = "RH_ERR_19"  # Temperature error for y-axis
y5_column = "RH_ERR_20"  # Temperature error for y-axis
y6_column = "PRCP_ERR_19"  # Temperature error for y-axis
y7_column = "PRCP_ERR_20"  # Temperature error for y-axis
y8_column = "tmpc_ranchi"  # Temperature error for y-axis
y9_column = "relh_ranchi"  # Temperature error for y-axis


# Load the NetCDF file (replace with your actual dataset file paths)
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20200303.nc')
ds3 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds4 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
ds5 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20190421.nc')
ds6 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20200303.nc')
ds7 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
ds8 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
ds9 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20190421.nc')
ds10 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20200303.nc')
gpm1 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20190421.nc')
gpm2 = xr.open_dataset(r'/media/lab/My Passport/hail/gpm/gpm_20200303.nc')
#########################
######################
# Select the data customizing
ds1 = ds1.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1))#.isel(time=18)
ds2 = ds2.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61))#.isel(time=16)
ds3 = ds3.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1))#.isel(time=18)
ds4 = ds4.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61))#.isel(time=16)
ds5 = ds5.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1))#.isel(time=18)
ds6 = ds6.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61))#.isel(time=16)
ds7 = ds7.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1))#.isel(time=18)
ds8 = ds8.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61))#.isel(time=16)
ds9 = ds9.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1))#.isel(time=18)
ds10 = ds10.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61))#.isel(time=16)
gpm1 = gpm1.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1))#.isel(time=18)
gpm2 = gpm2.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61))#######relative humidity
gpm1 =gpm1['precipitation'].isel(time=22).mean(['lat','lon']).squeeze()
gpm2 =gpm2['precipitation'].isel(time=22).mean(['lat','lon']).squeeze()
rh21 = ds1['rh2'].mean(dim=['lat','lon']).squeeze()
rh22 = ds2['rh2'].mean(dim=['lat','lon']).squeeze()
rh23 = ds3['rh2'].mean(dim=['lat','lon']).squeeze()
rh24 = ds4['rh2'].mean(dim=['lat','lon']).squeeze()
rh25 = ds5['rh2'].mean(dim=['lat','lon']).squeeze()
rh26 = ds6['rh2'].mean(dim=['lat','lon']).squeeze()
rh27 = ds7['rh2'].mean(dim=['lat','lon']).squeeze()
rh28 = ds8['rh2'].mean(dim=['lat','lon']).squeeze() 
rh29 = ds9['rh2'].mean(dim=['lat','lon']).squeeze()
rh210 = ds10['rh2'].mean(dim=['lat','lon']).squeeze()

##################2m temperature
t21 = ds1['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t22 = ds2['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t23 = ds3['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t24 = ds4['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t25 = ds5['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t26 = ds6['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t27 = ds7['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t28 = ds8['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t29 = ds9['t2'].mean(dim=['lat','lon']).squeeze() -273.16
t210 = ds10['t2'].mean(dim=['lat','lon']).squeeze() - 273.16 

#############ground heat fluex
##################potential temperature
lcl1 = ds1['lcl'].mean(dim=['lat','lon']).squeeze()
lcl2 = ds2['lcl'].mean(dim=['lat','lon']).squeeze()
lcl3 = ds3['lcl'].mean(dim=['lat','lon']).squeeze()
lcl4 = ds4['lcl'].mean(dim=['lat','lon']).squeeze()
lcl5 = ds5['lcl'].mean(dim=['lat','lon']).squeeze()
lcl6 = ds6['lcl'].mean(dim=['lat','lon']).squeeze()
lcl7 = ds7['lcl'].mean(dim=['lat','lon']).squeeze()
lcl8 = ds8['lcl'].mean(dim=['lat','lon']).squeeze()
lcl9 = ds9['lcl'].mean(dim=['lat','lon']).squeeze()
lcl10 = ds10['lcl'].mean(dim=['lat','lon']).squeeze() 

#############################
hfx1 = ds1['hfx'].mean(dim=['lat','lon']).squeeze()
hfx2 = ds2['hfx'].mean(dim=['lat','lon']).squeeze()
hfx3 = ds3['hfx'].mean(dim=['lat','lon']).squeeze()
hfx4 = ds4['hfx'].mean(dim=['lat','lon']).squeeze()
hfx5 = ds5['hfx'].mean(dim=['lat','lon']).squeeze()
hfx6 = ds6['hfx'].mean(dim=['lat','lon']).squeeze()
hfx7 = ds7['hfx'].mean(dim=['lat','lon']).squeeze()
hfx8 = ds8['hfx'].mean(dim=['lat','lon']).squeeze()
hfx9 = ds9['hfx'].mean(dim=['lat','lon']).squeeze()
hfx10 = ds10['hfx'].mean(dim=['lat','lon']).squeeze() 


###############latent heat
lh1 = ds1['lh'].mean(dim=['lat','lon']).squeeze()
lh2 = ds2['lh'].mean(dim=['lat','lon']).squeeze()
lh3 = ds3['lh'].mean(dim=['lat','lon']).squeeze()
lh4 = ds4['lh'].mean(dim=['lat','lon']).squeeze()
lh5 = ds5['lh'].mean(dim=['lat','lon']).squeeze()
lh6 = ds6['lh'].mean(dim=['lat','lon']).squeeze()
lh7 = ds7['lh'].mean(dim=['lat','lon']).squeeze()
lh8 = ds8['lh'].mean(dim=['lat','lon']).squeeze()
lh9 = ds9['lh'].mean(dim=['lat','lon']).squeeze()
lh10 = ds10['lh'].mean(dim=['lat','lon']).squeeze() 

###########boundary layer
##################potential temperature
pblh1 = ds1['pblh'].mean(dim=['lat','lon']).squeeze()
pblh2 = ds2['pblh'].mean(dim=['lat','lon']).squeeze()
pblh3 = ds3['pblh'].mean(dim=['lat','lon']).squeeze()
pblh4 = ds4['pblh'].mean(dim=['lat','lon']).squeeze()
pblh5 = ds5['pblh'].mean(dim=['lat','lon']).squeeze()
pblh6 = ds6['pblh'].mean(dim=['lat','lon']).squeeze()
pblh7 = ds7['pblh'].mean(dim=['lat','lon']).squeeze()
pblh8 = ds8['pblh'].mean(dim=['lat','lon']).squeeze()
pblh9 = ds9['pblh'].mean(dim=['lat','lon']).squeeze()
pblh10 = ds10['pblh'].mean(dim=['lat','lon']).squeeze() 

#########  Mcape
mcape1 = ds1['mcape'].mean(dim=['lat','lon']).squeeze()
mcape2 = ds2['mcape'].mean(dim=['lat','lon']).squeeze()
mcape3 = ds3['mcape'].mean(dim=['lat','lon']).squeeze()
mcape4 = ds4['mcape'].mean(dim=['lat','lon']).squeeze()
mcape5 = ds5['mcape'].mean(dim=['lat','lon']).squeeze()
mcape6 = ds6['mcape'].mean(dim=['lat','lon']).squeeze()
mcape7 = ds7['mcape'].mean(dim=['lat','lon']).squeeze()
mcape8 = ds8['mcape'].mean(dim=['lat','lon']).squeeze()
mcape9 = ds9['mcape'].mean(dim=['lat','lon']).squeeze()
mcape10 = ds10['mcape'].mean(dim=['lat','lon']).squeeze()
############## maximum cin
mcin1 = ds1['mcin'].mean(dim=['lat','lon']).squeeze()
mcin2 = ds2['mcin'].mean(dim=['lat','lon']).squeeze()
mcin3 = ds3['mcin'].mean(dim=['lat','lon']).squeeze()
mcin4 = ds4['mcin'].mean(dim=['lat','lon']).squeeze()
mcin5 = ds5['mcin'].mean(dim=['lat','lon']).squeeze()
mcin6 = ds6['mcin'].mean(dim=['lat','lon']).squeeze()
mcin7 = ds7['mcin'].mean(dim=['lat','lon']).squeeze()
mcin8 = ds8['mcin'].mean(dim=['lat','lon']).squeeze()
mcin9 = ds9['mcin'].mean(dim=['lat','lon']).squeeze()
mcin10 = ds10['mcin'].mean(dim=['lat','lon']).squeeze() 
 
tt = np.arange(0, 24.1, 0.5)
##############################2020/03/03########2 nd figure
fig = plt.figure(figsize=(21, 16))
gs = gridspec.GridSpec(3, 3, width_ratios=[1, 1, 1], wspace=0.3, hspace=0.36)  # Adjusted to 3 columns
# mpl.rcParams['figure.facecolor'] = 'white'
# fig.patch.set_facecolor('lightblue')  # Set background color for the entire figure
ax1 = fig.add_subplot(gs[0, 1])  # First column
# ax1.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax1.plot(tt, rh21.values, color='b', linewidth=2, label='Ferrier')  # Example plot on top axis
ax1.plot(tt, rh23.values, color='r', linewidth=2, label='Milbrandt')  # Example plot on top axis
ax1.plot(tt, rh25.values, color='g', linewidth=2, label='Thompson')  # Example plot on top axis
ax1.plot(tt, rh27.values, color='y', linewidth=2, label='Morrison')  # Example plot on top axis
ax1.plot(tt, rh29.values, color='k', linewidth=2, label='Wsm6')  # Example plot on top axis
ax1.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax1.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax1.set_ylabel('2m RH (%)', fontweight='bold', fontsize=22)
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax1.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax1.invert_yaxis()  # Invert y-axis
# ax1.legend(fontsize=10)
# ax1.legend(fontsize=30, loc='lower center', bbox_to_anchor=(1.5, 0.3))

ax1.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax1.set_title('(b)  ', fontweight='bold', fontsize=18)
# ax1.set_xticklabels([])
ax1.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax1.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
# ax1.set_xlim([])
ax1.set_yticks(np.arange(40, 75.1, 5))  # Set ticks on the top x-axis
ax1.set_ylim([40, 75])  # Adjust top axis limits to match top axis data range
ax1.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax1.tick_params(axis='x', rotation=0) # Rotate y-axis labels (if needed)
################
ax2 = fig.add_subplot(gs[0, 0])  # First column
# ax2.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax2.plot(tt, t21.values, color='b', linewidth=2)  # Example plot on top axis
ax2.plot(tt, t23.values, color='r', linewidth=2)  # Example plot on top axis
ax2.plot(tt, t25.values, color='g', linewidth=2)  # Example plot on top axis
ax2.plot(tt, t27.values, color='y', linewidth=2)  # Example plot on top axis
ax2.plot(tt, t29.values, color='k', linewidth=2)  # Example plot on top axis
ax2.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax2.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax2.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax2.invert_yaxis()  # Invert y-axis
ax2.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax2.set_title('(a)  ', fontweight='bold', fontsize=18)
ax2.set_ylabel('2m Temp (°C)', fontweight='bold', fontsize=22)
# ax2.set_xticklabels([])
ax2.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax2.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax2.set_yticks(np.arange(24, 36.1, 2))  # Set ticks on the top x-axis
ax2.set_ylim([26, 36])  # Adjust top axis limits to match top axis data range
# ax2.set_yticklabels([])
ax2.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax2.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax3 = fig.add_subplot(gs[0, 2])  # First column
# ax3.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax3.plot(tt, lcl1.values, color='b', linewidth=2)  # Example plot on top axis
ax3.plot(tt, lcl3.values, color='r', linewidth=2)  # Example plot on top axis
ax3.plot(tt, lcl5.values, color='g', linewidth=2)  # Example plot on top axis
ax3.plot(tt, lcl7.values, color='y', linewidth=2)  # Example plot on top axis
ax3.plot(tt, lcl9.values, color='k', linewidth=2)  # Example plot on top axis
ax3.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax3.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax3.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax3.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax3.invert_yaxis()  # Invert y-axis
ax3.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax3.set_title('(c)  ', fontweight='bold', fontsize=18)
ax3.set_ylabel('lcl (m)', fontweight='bold', fontsize=22)
# ax3.set_xticklabels([])
ax3.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax3.set_xlim([0, 24.1])  # Adjust top axis limits to match top axis data range
ax3.set_yticks(np.arange(750, 2500.1, 250))  # Set ticks on the top x-axis
ax3.set_ylim([750, 2700])  # Adjust top axis limits to match top axis data range
# ax3.set_yticklabels([])
ax3.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax3.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax8 = fig.add_subplot(gs[1, 1])  # First column
# ax8.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax8.plot(tt, hfx1.values, color='b', linewidth=2)  # Example plot on top axis
ax8.plot(tt, hfx3.values, color='r', linewidth=2)  # Example plot on top axis
ax8.plot(tt, hfx5.values, color='g', linewidth=2)  # Example plot on top axis
ax8.plot(tt, hfx7.values, color='y', linewidth=2)  # Example plot on top axis
ax8.plot(tt, hfx9.values, color='k', linewidth=2)  # Example plot on top axis
ax8.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax8.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax8.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax8.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax8.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax8.invert_yaxis()  # Invert y-axis
ax8.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax8.set_title('(e)  ', fontweight='bold', fontsize=18)
ax8.set_ylabel('sensible Heat flux (W m-2)', fontweight='bold', fontsize=22)
# ax8.set_xticklabels([])
ax8.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax8.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax8.set_yticks(np.arange(0, 300.1, 50))  # Set ticks on the top x-axis
ax8.set_ylim([0, 300])  # Adjust top axis limits to match top axis data range
ax8.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax8.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################################
ax4 = fig.add_subplot(gs[1, 2])  # First column
# ax4.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax4.plot(tt, lh1.values, color='b', linewidth=2)  # Example plot on top axis
ax4.plot(tt, lh3.values, color='r', linewidth=2)  # Example plot on top axis
ax4.plot(tt, lh5.values, color='g', linewidth=2)  # Example plot on top axis
ax4.plot(tt, lh7.values, color='y', linewidth=2)  # Example plot on top axis
ax4.plot(tt, lh9.values, color='k', linewidth=2)  # Example plot on top axis
ax4.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax4.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax4.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax4.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax4.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax4.invert_yaxis()  # Invert y-axis
ax4.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax4.set_title('(f)  ', fontweight='bold', fontsize=18)
ax4.set_ylabel('Latent Heat flux (W m-2)', fontweight='bold', fontsize=22)
# ax4.set_xticklabels([])
ax4.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax4.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax4.set_yticks(np.arange(0, 250.1, 50))  # Set ticks on the top x-axis
ax4.set_ylim([0, 250])  # Adjust top axis limits to match top axis data range
ax4.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax4.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax5 = fig.add_subplot(gs[1, 0])  # First column
# ax5.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax5.plot(tt, pblh1.values, color='b', linewidth=2)  # Example plot on top axis
ax5.plot(tt, pblh3.values, color='r', linewidth=2)  # Example plot on top axis
ax5.plot(tt, pblh5.values, color='g', linewidth=2)  # Example plot on top axis
ax5.plot(tt, pblh7.values, color='y', linewidth=2)  # Example plot on top axis
ax5.plot(tt, pblh9.values, color='k', linewidth=2)  # Example plot on top axis
ax5.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax5.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax5.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax5.tick_params(axis='y', rotation=90)  # Rotate y-axis labels if needed
ax5.invert_yaxis()  # Invert y-axis
ax5.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax5.set_title('(d)  ', fontweight='bold', fontsize=18)
ax5.set_ylabel('PBL height (m)', fontweight='bold', fontsize=22)
# ax5.set_xticklabels([])
ax5.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax5.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax5.set_yticks(np.arange(0, 2500.1, 500))  # Set ticks on the top x-axis
ax5.set_ylim([0, 2500])  # Adjust top axis limits to match top axis data range
# ax5.set_yticklabels([])
ax5.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax5.tick_params(axis='y', rotation=45) # Rotate y-axis labels (if needed)
################
ax6 = fig.add_subplot(gs[2, 0])  # First column
# ax6.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax6.plot(tt, mcape1.values, color='b', linewidth=2)  # Example plot on top axis
ax6.plot(tt, mcape3.values, color='r', linewidth=2)  # Example plot on top axis
ax6.plot(tt, mcape5.values, color='g', linewidth=2)  # Example plot on top axis
ax6.plot(tt, mcape7.values, color='y', linewidth=2)  # Example plot on top axis
ax6.plot(tt, mcape9.values, color='k', linewidth=2)  # Example plot on top axis
ax6.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax6.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax6.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax6.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax6.invert_yaxis()  # Invert y-axis
ax6.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax6.set_title('(g)  ', fontweight='bold', fontsize=18)
ax6.set_ylabel('MCAPE (J/kg)', fontweight='bold', fontsize=22)
# ax6.set_xticklabels([])
ax6.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax6.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax6.set_yticks(np.arange(0, 2500.1, 500))  # Set ticks on the top x-axis
ax6.set_ylim([0, 2200])  # Adjust top axis limits to match top axis data range
# ax6.set_yticklabels([])
ax6.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax6.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax7 = fig.add_subplot(gs[2, 1])  # First column
# ax7.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax7.plot(tt, mcin1.values, color='b', linewidth=2)  # Example plot on top axis
ax7.plot(tt, mcin3.values, color='r', linewidth=2)  # Example plot on top axis
ax7.plot(tt, mcin5.values, color='g', linewidth=2)  # Example plot on top axis
ax7.plot(tt, mcin7.values, color='y', linewidth=2)  # Example plot on top axis
ax7.plot(tt, mcin9.values, color='k', linewidth=2)  # Example plot on top axis
ax7.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax7.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax7.set_ylabel('MCIN (J/kg)', fontweight='bold', fontsize=22)
ax7.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax7.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax7.invert_yaxis()  # Invert y-axis
ax7.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax7.set_title('(h)  ', fontweight='bold', fontsize=18)
# ax7.set_xticklabels([])
ax7.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax7.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax7.set_yticks(np.arange(0, 500.1, 100))  # Set ticks on the top x-axis
ax7.set_ylim([0, 460])  # Adjust top axis limits to match top axis data range
ax7.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax7.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

fig.legend(loc='upper left', bbox_to_anchor=(0.65, 0.25), fontsize=19, ncol=2)

# plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.35, color='gray')
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 24,
    'ytick.major.size': 24,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})
plt.tight_layout()
plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/case1_RH_T2m_lfc_etc_diff_schemes.png', dpi=500, bbox_inches='tight')

plt.show()

################# case2 2020/03/03 

tt = np.arange(0, 24.1, 0.5)
##############################2020/03/03########2 nd figure
fig = plt.figure(figsize=(21, 16))
gs = gridspec.GridSpec(3, 3, width_ratios=[1, 1, 1], wspace=0.3, hspace=0.36)  # Adjusted to 3 columns
# mpl.rcParams['figure.facecolor'] = 'white'
# fig.patch.set_facecolor('lightblue')  # Set background color for the entire figure
ax1 = fig.add_subplot(gs[0, 1])  # First column
# ax1.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
pcm1 = ax1.plot(df1[x_column], df1[y9_column], color='maroon', linestyle='-', linewidth=2, label='METAR data')
ax1.plot(tt, rh22.values, color='b', linewidth=2, label='Ferrier')  # Example plot on top axis
ax1.plot(tt, rh24.values, color='r', linewidth=2, label='Milbrandt')  # Example plot on top axis
ax1.plot(tt, rh26.values, color='g', linewidth=2, label='Thompson')  # Example plot on top axis
ax1.plot(tt, rh28.values, color='y', linewidth=2, label='Morrison')  # Example plot on top axis
ax1.plot(tt, rh210.values, color='k', linewidth=2, label='Wsm6')  # Example plot on top axis
ax1.set_ylabel('2m RH (%)', fontweight='bold', fontsize=22)
ax1.axvline(x=7, color='k', linestyle='--', linewidth=1)
ax1.axvline(x=9, color='k', linestyle='--', linewidth=1)
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax1.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax1.invert_yaxis()  # Invert y-axis
# ax1.legend(fontsize=10)
ax1.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax1.set_title('(b)  ', fontweight='bold', fontsize=18)
# ax1.set_xticklabels([])
ax1.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax1.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
# ax1.set_xlim([])
ax1.set_yticks(np.arange(30, 95.1, 5))  # Set ticks on the top x-axis
ax1.set_ylim([30, 95])  # Adjust top axis limits to match top axis data range
ax1.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax1.tick_params(axis='x', rotation=0) # Rotate y-axis labels (if needed)
################
ax2 = fig.add_subplot(gs[0, 0])  # First column
# ax2.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax2.plot(df1[x_column], df1[y8_column], color='maroon', linestyle='-', linewidth=2)
ax2.plot(tt, t22.values, color='b', linewidth=2)  # Example plot on top axis
ax2.plot(tt, t24.values, color='r', linewidth=2)  # Example plot on top axis
ax2.plot(tt, t26.values, color='g', linewidth=2)  # Example plot on top axis
ax2.plot(tt, t28.values, color='y', linewidth=2)  # Example plot on top axis
ax2.plot(tt, t210.values, color='k', linewidth=2)  # Example plot on top axis
ax2.axvline(x=7, color='k', linestyle='--', linewidth=1)
ax2.axvline(x=9, color='k', linestyle='--', linewidth=1)
ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax2.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax2.invert_yaxis()  # Invert y-axis
ax2.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax2.set_title('(a)  ', fontweight='bold', fontsize=18)
ax2.set_ylabel('2m Temp (°C)', fontweight='bold', fontsize=22)
# ax2.set_xticklabels([])
ax2.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax2.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax2.set_yticks(np.arange(16, 34.1, 2))  # Set ticks on the top x-axis
ax2.set_ylim([16, 34])  # Adjust top axis limits to match top axis data range
# ax2.set_yticklabels([])
ax2.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax2.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax3 = fig.add_subplot(gs[0, 2])  # First column
# ax3.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax3.plot(tt, lcl2.values, color='b', linewidth=2)  # Example plot on top axis
ax3.plot(tt, lcl4.values, color='r', linewidth=2)  # Example plot on top axis
ax3.plot(tt, lcl6.values, color='g', linewidth=2)  # Example plot on top axis
ax3.plot(tt, lcl8.values, color='y', linewidth=2)  # Example plot on top axis
ax3.plot(tt, lcl10.values, color='k', linewidth=2)  # Example plot on top axis
ax3.axvline(x=7, color='k', linestyle='--', linewidth=1)
ax3.axvline(x=9, color='k', linestyle='--', linewidth=1)
ax3.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax3.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax3.invert_yaxis()  # Invert y-axis
ax3.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax3.set_title('(c)  ', fontweight='bold', fontsize=18)
ax3.set_ylabel('lcl (m)', fontweight='bold', fontsize=22)
# ax3.set_xticklabels([])
ax3.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax3.set_xlim([0, 24.1])  # Adjust top axis limits to match top axis data range
ax3.set_yticks(np.arange(1000, 2500.1, 250))  # Set ticks on the top x-axis
ax3.set_ylim([1000, 2500])  # Adjust top axis limits to match top axis data range
# ax3.set_yticklabels([])
ax3.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax3.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax8 = fig.add_subplot(gs[1, 1])  # First column
# ax8.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax8.plot(tt, hfx2.values, color='b', linewidth=2)  # Example plot on top axis
ax8.plot(tt, hfx4.values, color='r', linewidth=2)  # Example plot on top axis
ax8.plot(tt, hfx6.values, color='g', linewidth=2)  # Example plot on top axis
ax8.plot(tt, hfx8.values, color='y', linewidth=2)  # Example plot on top axis
ax8.plot(tt, hfx10.values, color='k', linewidth=2)  # Example plot on top axis
ax8.axvline(x=8, color='k', linestyle='--', linewidth=1)
ax8.axvline(x=10, color='k', linestyle='--', linewidth=1)
ax8.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax8.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax8.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax8.invert_yaxis()  # Invert y-axis
ax8.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax8.set_title('(e)  ', fontweight='bold', fontsize=18)
ax8.set_ylabel('sensible Heat flux (W m-2)', fontweight='bold', fontsize=22)
# ax8.set_xticklabels([])
ax8.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax8.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax8.set_yticks(np.arange(0, 300.1, 50))  # Set ticks on the top x-axis
ax8.set_ylim([0, 300])  # Adjust top axis limits to match top axis data range
ax8.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax8.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
#####################
ax4 = fig.add_subplot(gs[1, 2])  # First column
# ax4.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax4.plot(tt, lh2.values, color='b', linewidth=2)  # Example plot on top axis
ax4.plot(tt, lh4.values, color='r', linewidth=2)  # Example plot on top axis
ax4.plot(tt, lh6.values, color='g', linewidth=2)  # Example plot on top axis
ax4.plot(tt, lh8.values, color='y', linewidth=2)  # Example plot on top axis
ax4.plot(tt, lh10.values, color='k', linewidth=2)  # Example plot on top axis
ax4.axvline(x=7, color='k', linestyle='--', linewidth=1)
ax4.axvline(x=9, color='k', linestyle='--', linewidth=1)
ax4.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=22)
ax4.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax4.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax4.invert_yaxis()  # Invert y-axis
ax4.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax4.set_title('(f)  ', fontweight='bold', fontsize=18)
ax4.set_ylabel('Latent Heat flux (W m-2)', fontweight='bold', fontsize=22)
# ax4.set_xticklabels([])
ax4.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax4.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax4.set_yticks(np.arange(0, 250.1, 50))  # Set ticks on the top x-axis
ax4.set_ylim([0, 250])  # Adjust top axis limits to match top axis data range
ax4.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax4.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax5 = fig.add_subplot(gs[1, 0])  # First column
# ax5.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax5.plot(tt, pblh2.values, color='b', linewidth=2)  # Example plot on top axis
ax5.plot(tt, pblh4.values, color='r', linewidth=2)  # Example plot on top axis
ax5.plot(tt, pblh6.values, color='g', linewidth=2)  # Example plot on top axis
ax5.plot(tt, pblh8.values, color='y', linewidth=2)  # Example plot on top axis
ax5.plot(tt, pblh10.values, color='k', linewidth=2)  # Example plot on top axis
ax5.axvline(x=7, color='k', linestyle='--', linewidth=1)
ax5.axvline(x=9, color='k', linestyle='--', linewidth=1)
ax5.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax5.tick_params(axis='y', rotation=90)  # Rotate y-axis labels if needed
ax5.invert_yaxis()  # Invert y-axis
ax5.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax5.set_title('(d)  ', fontweight='bold', fontsize=18)
ax5.set_ylabel('PBL height (m)', fontweight='bold', fontsize=22)
# ax5.set_xticklabels([])
ax5.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax5.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax5.set_yticks(np.arange(0, 3000.1, 500))  # Set ticks on the top x-axis
ax5.set_ylim([0, 3000])  # Adjust top axis limits to match top axis data range
# ax5.set_yticklabels([])
ax5.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax5.tick_params(axis='y', rotation=45) # Rotate y-axis labels (if needed)
################
ax6 = fig.add_subplot(gs[2, 0])  # First column
# ax6.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax6.plot(tt, mcape2.values, color='b', linewidth=2)  # Example plot on top axis
ax6.plot(tt, mcape4.values, color='r', linewidth=2)  # Example plot on top axis
ax6.plot(tt, mcape6.values, color='g', linewidth=2)  # Example plot on top axis
ax6.plot(tt, mcape8.values, color='y', linewidth=2)  # Example plot on top axis
ax6.plot(tt, mcape10.values, color='k', linewidth=2)  # Example plot on top axis
ax6.axvline(x=7, color='k', linestyle='--', linewidth=1)
ax6.axvline(x=9, color='k', linestyle='--', linewidth=1)
ax6.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax6.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax6.invert_yaxis()  # Invert y-axis
ax6.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax6.set_title('(g)  ', fontweight='bold', fontsize=18)
ax6.set_ylabel('MCAPE (J/kg)', fontweight='bold', fontsize=22)
# ax6.set_xticklabels([])
ax6.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax6.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax6.set_yticks(np.arange(0, 1000.1, 200))  # Set ticks on the top x-axis
ax6.set_ylim([0, 1000])  # Adjust top axis limits to match top axis data range
# ax6.set_yticklabels([])
ax6.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax6.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax7 = fig.add_subplot(gs[2, 1])  # First column
# ax7.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax7.plot(tt, mcin2.values, color='b', linewidth=2)  # Example plot on top axis
ax7.plot(tt, mcin4.values, color='r', linewidth=2)  # Example plot on top axis
ax7.plot(tt, mcin6.values, color='g', linewidth=2)  # Example plot on top axis
ax7.plot(tt, mcin8.values, color='y', linewidth=2)  # Example plot on top axis
ax7.plot(tt, mcin10.values, color='k', linewidth=2)  # Example plot on top axis
ax7.axvline(x=7, color='k', linestyle='--', linewidth=1)
ax7.axvline(x=9, color='k', linestyle='--', linewidth=1)
ax7.set_ylabel('MCIN (J/kg)', fontweight='bold', fontsize=22)
ax7.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax7.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax7.invert_yaxis()  # Invert y-axis
ax7.tick_params(axis='both', length=8, width=1.8, labelsize=16)
ax7.set_title('(h)  ', fontweight='bold', fontsize=18)
# ax7.set_xticklabels([])
ax7.set_xticks(np.arange(0, 24.1, 2))  # Set ticks on the top x-axis
ax7.set_xlim([0, 24])  # Adjust top axis limits to match top axis data range
ax7.set_yticks(np.arange(0, 300.1, 50))  # Set ticks on the top x-axis
ax7.set_ylim([0, 300])  # Adjust top axis limits to match top axis data range
ax7.set_xlabel(r'Time (UTC)', fontweight='bold', fontsize=17)
ax7.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

### figure legends customizedly setting position
fig.legend(loc='upper left', bbox_to_anchor=(0.65, 0.25), fontsize=19, ncol=2)



# plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.35, color='gray')
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 24,
    'ytick.labelsize': 24,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 24,
    'ytick.major.size': 24,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})
# plt.tight_layout()
# plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/case2_RH_T2m_lfc_etc_diff_schemes.png', dpi=500, bbox_inches='tight')

plt.show()

