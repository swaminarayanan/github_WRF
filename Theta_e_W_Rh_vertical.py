import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Load the NetCDF file (replace with your actual dataset file paths)
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_ferrier_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_ferrier_20200303.nc')
ds3 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_milbrandt_20190421.nc')
ds4 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_milbrandt_20200303.nc')
ds5 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_morrison_20190421.nc')
ds6 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_morrison_20200303.nc')
ds7 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_thompson_20190421.nc')
ds8 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_thompson_20190421.nc')
ds9 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_wsm6_20190421.nc')
ds10 = xr.open_dataset(r'/media/lab/My Passport/hail/data/derived_variables/theta_e_wsm6_20200303.nc')
####################
# Load the NetCDF file (replace with your actual dataset file paths)
dsa = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20190421.nc')
dsb = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20200303.nc')
dsc = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
dsd = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
dse = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20190421.nc')
dsf = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20200303.nc')
dsg = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
dsh = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
dsi = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20190421.nc')
dsj = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20200303.nc')
#################################

# Select the data customizing
ds1 = ds1.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
ds2 = ds2.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
ds3 = ds3.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
ds4 = ds4.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
ds5 = ds5.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
ds6 = ds6.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
ds7 = ds7.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
ds8 = ds8.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
ds9 = ds9.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
ds10 = ds10.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
#######################
dsa = dsa.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
dsb = dsb.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
dsc = dsc.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
dsd = dsd.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
dse = dse.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
dsf = dsf.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
dsg = dsg.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
dsh = dsh.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)
dsi = dsi.sel(lat=slice(20.9, 21.6), lon=slice(86.3, 87.1)).isel(time=18)
dsj = dsj.sel(lat=slice(22.8, 23.5), lon=slice(84.8, 85.61)).isel(time=16)

theta1 = ds1['theta_e1'].isel(lat=6, lon=43).squeeze() #- 273.16
theta2 = ds2['theta_e2'].isel(lat=15, lon=2).squeeze() #- 273.16
theta3 = ds3['theta_e1'].isel(lat=19, lon=40).squeeze() #- 273.16
theta4 = ds4['theta_e2'].isel(lat=26, lon=5).squeeze() #- 273.16
theta5 = ds5['theta_e1'].isel(lat=13, lon=43).squeeze() #- 273.16
theta6 = ds6['theta_e2'].isel(lat=17, lon=6).squeeze() #- 273.16
theta7 = ds7['theta_e1'].isel(lat=21, lon=30).squeeze() #- 273.16
theta8 = ds8['theta_e1'].isel(lat=28, lon=42).squeeze() #- 273.16
theta9 = ds9['theta_e1'].isel(lat=5, lon=42).squeeze() #- 273.16
theta10 = ds10['theta_e2'].isel(lat=18, lon=0).squeeze() #- 273.16 
###################vertical velocity 
# W1 = dsa['w'].isel(lat=3, lon=30).squeeze() #- 273.16
# W2 = dsb['w'].isel(lat=15, lon=25).squeeze() #- 273.16
# W3 = dsc['w'].isel(lat=20, lon=32).squeeze() #- 273.16
# W4 = dsd['w'].isel(lat=10, lon=10).squeeze() #- 273.16
# W5 = dse['w'].isel(lat=1, lon=23).squeeze() #- 273.16
# W6 = dsf['w'].isel(lat=0, lon=10).squeeze() #- 273.16
# W7 = dsg['w'].isel(lat=7, lon=26).squeeze() #- 273.16
# W8 = dsh['w'].isel(lat=2, lon=41).squeeze() #- 273.16
# W9 = dsi['w'].isel(lat=10, lon=37).squeeze() #- 273.16
# W10 = dsj['w'].isel(lat=29, lon=15).squeeze() #- 273.16 

###################vertical velocity 
W1 = dsa['w'].isel(lat=slice(1, 8), lon=slice(26, 36)).mean(['lat', 'lon']).squeeze()#isel(lat=3, lon=30).squeeze() #- 273.16
W2 = dsb['w'].isel(lat=slice(14, 17), lon=slice(24, 27)).mean(['lat', 'lon']).squeeze()#.isel(lat=15, lon=25).squeeze() #- 273.16
W3 = dsc['w'].isel(lat=slice(17, 23), lon=slice(29, 35)).mean(['lat', 'lon']).squeeze()#.isel(lat=20, lon=32).squeeze() #- 273.16
W4 = dsd['w'].isel(lat=slice(11, 13), lon=slice(9, 12)).mean(['lat', 'lon']).squeeze()#.isel(lat=10, lon=10).squeeze() #- 273.16
W5 = dse['w'].isel(lat=slice(1, 8), lon=slice(20, 25)).mean(['lat', 'lon']).squeeze()#.isel(lat=1, lon=23).squeeze() #- 273.16
W6 = dsf['w'].isel(lat=slice(0, 2), lon=slice(9, 14)).mean(['lat', 'lon']).squeeze()#.isel(lat=0, lon=10).squeeze() #- 273.16
W7 = dsg['w'].isel(lat=slice(4, 11), lon=slice(22, 30)).mean(['lat', 'lon']).squeeze()#.isel(lat=7, lon=26).squeeze() #- 273.16
W8 = dsh['w'].isel(lat=slice(1, 6), lon=slice(36, 48)).mean(['lat', 'lon']).squeeze()#.isel(lat=2, lon=41).squeeze() #- 273.16
W9 = dsi['w'].isel(lat=slice(4, 14), lon=slice(33, 40)).mean(['lat', 'lon']).squeeze()#.isel(lat=10, lon=37).squeeze() #- 273.16
W10 = dsj['w'].isel(lat=slice(27, 28), lon=slice(13, 16)).mean(['lat', 'lon']).squeeze()#.isel(lat=29, lon=15).squeeze() #- 273.16 
################# Relative humidity
RH1 = dsa['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH2 = dsb['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH3 = dsc['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH4 = dsd['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH5 = dse['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH6 = dsf['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH7 = dsg['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH8 = dsh['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH9 = dsi['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16
RH10 = dsj['rh'].isel(lat=slice(0, 40), lon=slice(0, 40)).mean(['lat', 'lon']).squeeze() #- 273.16 

k = np.arange(310, 340.1, 5)

fig = plt.figure(figsize=(18, 16))
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], hspace=0.25, wspace=0.12)

ax1 = fig.add_subplot(gs[0, 0])  # First column
# ax1.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax1.plot(theta1.values, theta1['lev'], color='b', linewidth=2, label='Ferrier')  # Example plot on top axis
ax1.plot(theta3.values, theta3['lev'], color='r', linewidth=2, label='Milbrandt')  # Example plot on top axis
ax1.plot(theta5.values, theta5['lev'], color='g', linewidth=2, label='Thompson')  # Example plot on top axis
ax1.plot(theta7.values, theta7['lev'], color='y', linewidth=2, label='Morrison')  # Example plot on top axis
ax1.plot(theta9.values, theta9['lev'], color='k', linewidth=2, label='Wsm6')  # Example plot on top axis
ax1.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=16)
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax1.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax1.invert_yaxis()  # Invert y-axis
ax1.legend(fontsize=10)
ax1.set_title('(a)  ', fontweight='bold', fontsize=18)
ax1.tick_params(axis='both', length=8, width=1.8, labelsize=14)
ax1.set_xticks(np.arange(325, 370.1, 5))  # Set ticks on the top x-axis
ax1.set_xlim([325, 370])  # Adjust top axis limits to match top axis data range
# ax1.set_xlim([])
ax1.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax1.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax1.set_xlabel(r'Theta_e (k)', fontweight='bold', fontsize=14)
ax1.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
################
ax2 = fig.add_subplot(gs[0, 1])  # First column
# ax2.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax2.plot(W1.values, W1['lev'], color='b', linewidth=2)  # Example plot on top axis
ax2.plot(W3.values, W3['lev'], color='r', linewidth=2)  # Example plot on top axis
ax2.plot(W5.values, W5['lev'], color='g', linewidth=2)  # Example plot on top axis
ax2.plot(W7.values, W7['lev'], color='y', linewidth=2)  # Example plot on top axis
ax2.plot(W9.values, W9['lev'], color='k', linewidth=2)  # Example plot on top axis
# ax2.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=16)
ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax2.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax2.invert_yaxis()  # Invert y-axis
ax2.legend(fontsize=10)
ax2.set_title('(b)  ', fontweight='bold', fontsize=18)
ax2.tick_params(axis='both', length=8, width=1.8, labelsize=14)
ax2.set_xticks(np.arange(-3, 9.1, 1))  # Set ticks on the top x-axis
ax2.set_xlim([-3, 9])  # Adjust top axis limits to match top axis data range
# # ax2.set_xlim([])
ax2.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax2.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax2.set_yticklabels([])
ax2.set_xlabel(r'W (m/s)', fontweight='bold', fontsize=14)
ax2.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

###################
ax3 = fig.add_subplot(gs[0, 2])  # First column
# ax3.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax3.plot(RH1.values, RH1['lev'], color='b', linewidth=2)  # Example plot on top axis
ax3.plot(RH3.values, RH3['lev'], color='r', linewidth=2)  # Example plot on top axis
ax3.plot(RH5.values, RH5['lev'], color='g', linewidth=2)  # Example plot on top axis
ax3.plot(RH7.values, RH7['lev'], color='y', linewidth=2)  # Example plot on top axis
ax3.plot(RH9.values, RH9['lev'], color='k', linewidth=2)  # Example plot on top axis
# ax3.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=16)
ax3.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax3.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax3.invert_yaxis()  # Invert y-axis
ax3.legend(fontsize=10)

ax3.set_title('(c)  ', fontweight='bold', fontsize=18)
ax3.tick_params(axis='both', length=8, width=1.8, labelsize=14)
ax3.set_xticks(np.arange(0, 100.1, 20))  # Set ticks on the top x-axis
ax3.set_xlim([0, 100])  # Adjust top axis limits to match top axis data range
# ax3.set_xlim([])
ax3.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax3.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax3.set_yticklabels([])
ax3.set_xlabel(r'RH (%)', fontweight='bold', fontsize=14)
ax3.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

ax4 = fig.add_subplot(gs[1, 0])  # First column
# ax4.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax4.plot(theta2.values, theta2['lev'], color='b', linewidth=2)  # Example plot on top axis
ax4.plot(theta4.values, theta4['lev'], color='r', linewidth=2)  # Example plot on top axis
ax4.plot(theta6.values, theta6['lev'], color='g', linewidth=2)  # Example plot on top axis
ax4.plot(theta8.values, theta8['lev'], color='y', linewidth=2)  # Example plot on top axis
ax4.plot(theta10.values, theta10['lev'], color='k', linewidth=2)  # Example plot on top axis
ax4.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax4.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax4.invert_yaxis()  # Invert y-axis
ax4.tick_params(axis='both', length=8, width=1.8, labelsize=14)
ax4.set_title('(d)  ', fontweight='bold', fontsize=18)

ax4.set_xticks(np.arange(315, 370.1, 5))  # Set ticks on the top x-axis
ax4.set_xlim([315, 370])  # Adjust top axis limits to match top axis data range
ax4.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax4.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
# ax4.set_yticklabels([])
ax4.set_xlabel(r'Theta_e (k)', fontweight='bold', fontsize=14)
ax4.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)
ax4.set_ylabel('Pressure (hPa)', fontweight='bold', fontsize=16)

################################
ax5 = fig.add_subplot(gs[1, 1])  # First column
# ax5.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax5.plot(W2.values, W2['lev'], color='b', linewidth=2)  # Example plot on top axis
ax5.plot(W4.values, W4['lev'], color='r', linewidth=2)  # Example plot on top axis
ax5.plot(W6.values, W6['lev'], color='g', linewidth=2)  # Example plot on top axis
ax5.plot(W8.values, W8['lev'], color='y', linewidth=2)  # Example plot on top axis
ax5.plot(W10.values, W10['lev'], color='k', linewidth=2)  # Example plot on top axis
ax5.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax5.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax5.invert_yaxis()  # Invert y-axis
ax5.tick_params(axis='both', length=8, width=1.8, labelsize=14)
ax5.set_title('(e)  ', fontweight='bold', fontsize=18)

ax5.set_xticks(np.arange(-1.5, 4.1, 0.5))  # Set ticks on the top x-axis
ax5.set_xlim([-1.5, 4.1])  # Adjust top axis limits to match top axis data range
ax5.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax5.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax5.set_yticklabels([])
ax5.set_xlabel(r'W (m/s)', fontweight='bold', fontsize=14)
ax5.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)

################
ax6 = fig.add_subplot(gs[1, 2])  # First column
# ax6.set_facecolor('lightyellow')  # Set background color for the plot area# mpl.rcParams['figure.facecolor'] = 'lightgray'
ax6.plot(RH2.values, RH2['lev'], color='b', linewidth=2)  # Example plot on top axis
ax6.plot(RH4.values, RH4['lev'], color='r', linewidth=2)  # Example plot on top axis
ax6.plot(RH6.values, RH6['lev'], color='g', linewidth=2)  # Example plot on top axis
ax6.plot(RH8.values, RH8['lev'], color='y', linewidth=2)  # Example plot on top axis
ax6.plot(RH10.values, RH10['lev'], color='k', linewidth=2)  # Example plot on top axis
ax6.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
ax6.tick_params(axis='y', rotation=45)  # Rotate y-axis labels if needed
ax6.invert_yaxis()  # Invert y-axis
ax6.tick_params(axis='both', length=8, width=1.8, labelsize=14)
ax6.set_title('(f)  ', fontweight='bold', fontsize=18)

ax6.set_xticks(np.arange(0, 100.1, 20))  # Set ticks on the top x-axis
ax6.set_xlim([0, 100])  # Adjust top axis limits to match top axis data range
ax6.set_yticks(np.arange(100, 1000.1, 100))  # Set ticks on the top x-axis
ax6.set_ylim([1000, 100])  # Adjust top axis limits to match top axis data range
ax6.set_yticklabels([])
ax6.set_xlabel(r'RH (%)', fontweight='bold', fontsize=14)
ax6.tick_params(axis='x', rotation=45) # Rotate y-axis labels (if needed)


plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 14,
    'ytick.major.size': 14,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})
plt.tight_layout()
plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/Theta_e_vertical_profiles.png', dpi=500, bbox_inches='tight')

plt.show()

# #####################
# data = theta1
# from numpy import unravel_index
# unravel_index(data.argmax(), data.shape)