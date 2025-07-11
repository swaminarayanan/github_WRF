import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Load the NetCDF file (replace with your actual dataset file paths)
ds1 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20190421.nc')
ds2 = xr.open_dataset(r'/media/lab/My Passport/hail/data/ferrier_20200303.nc')
ds3 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20190421.nc')
ds4 = xr.open_dataset(r'/media/lab/My Passport/hail/data/milbrandt_20200303.nc')
ds5 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
ds6 = xr.open_dataset(r'/media/lab/My Passport/hail/data/thompson_20190421.nc')
ds7 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20190421.nc')
ds8 = xr.open_dataset(r'/media/lab/My Passport/hail/data/morrison_20200303.nc')
ds9 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20190421.nc')
ds10 = xr.open_dataset(r'/media/lab/My Passport/hail/data/wsm6_20200303.nc')

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
#######vertival velocity
w1 = ds1['w'].mean(dim=['lat']).squeeze()
w2 = ds2['w'].mean(dim=['lat']).squeeze()
w3 = ds3['w'].mean(dim=['lat']).squeeze()
w4 = ds4['w'].mean(dim=['lat']).squeeze()
w5 = ds5['w'].mean(dim=['lat']).squeeze()
w6 = ds6['w'].mean(dim=['lat']).squeeze()
w7 = ds7['w'].mean(dim=['lat']).squeeze()
w8 = ds8['w'].mean(dim=['lat']).squeeze()
w9 = ds9['w'].mean(dim=['lat']).squeeze()
w10 = ds10['w'].mean(dim=['lat']).squeeze()
##################potential temperature
theta1 = ds1['theta'].mean(dim=['lat']).squeeze() - 273.16
theta2 = ds2['theta'].mean(dim=['lat']).squeeze() -273.16
theta3 = ds3['theta'].mean(dim=['lat']).squeeze() -273.16
theta4 = ds4['theta'].mean(dim=['lat']).squeeze() -273.16
theta5 = ds5['theta'].mean(dim=['lat']).squeeze() -273.16
theta6 = ds6['theta'].mean(dim=['lat']).squeeze() -273.16
theta7 = ds7['theta'].mean(dim=['lat']).squeeze() -273.16
theta8 = ds8['theta'].mean(dim=['lat']).squeeze() -273.16
theta9 = ds9['theta'].mean(dim=['lat']).squeeze() -273.16
theta10 = ds10['theta'].mean(dim=['lat']).squeeze() - 273.16 
###########water vapour mixing ratio
qvapor1 = ds1['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor2 = ds2['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor3 = ds3['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor4 = ds4['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor5 = ds5['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor6 = ds6['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor7 = ds7['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor8 = ds8['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor9 = ds9['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
qvapor10 = ds10['qvapor'].mean(dim=['lat']).squeeze() / 1*1.0e+03
k = np.arange(-3, 3.1, 0.5)
l = np.arange(-1, 1.51, 0.25)


fig = plt.figure(figsize=(20, 16))
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], hspace=0.16, wspace=0.12)
#########################
ax1 = fig.add_subplot(gs[0, 0]) 
w_wind1 = ax1.contourf(w1['lon'], w1['lev'], w1, cmap='Spectral', 
                                  levels=k, extend='both')

# Plot Temperature using contour (line contours with labels)
th1 = ax1.contour(theta1['lon'], theta1['lev'], theta1, colors='k', linewidths=2, 
                          levels=np.linspace(theta1.min(), theta1.max(), 10))
ax1.clabel(th1, inline=True, fontsize=15, fmt='%2.1f')

qvap1 = ax1.contour(qvapor1['lon'], qvapor1['lev'], qvapor1, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor1.min(), qvapor1.max(), 10))
ax1.clabel(qvap1, inline=True, fontsize=15, fmt='%2.1f')
# Axis and ticks formatting
ax1.set_yticks(np.arange(100, 1000.1, 100))
ax1.set_ylim([100, 1000])
ax1.set_xticks(np.arange(86.3, 87.2, 0.1))
ax1.set_xlim([86.3, 87.1])
# ax2.set_yticklabels([])
ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax1.invert_yaxis()
ax1.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax1.set_title('(a) Ferrier', fontweight='bold', fontsize=16)
# ax1.set_xlabel('Longitude', fontweight='bold', fontsize=20)
ax1.set_ylabel('pressure level (hpa)', fontweight='bold', fontsize=20)
ax1.set_xticklabels([])


####################
ax2 = fig.add_subplot(gs[0, 1]) 
w_wind2 = ax2.contourf(w3['lon'], w3['lev'], w3, cmap='Spectral', 
                                  levels=k ,extend='both')

# Plot Temperature using contour (line contours with labels)
th2 = ax2.contour(theta3['lon'], theta3['lev'], theta3, colors='k', linewidths=2, 
                          levels=np.linspace(theta3.min(), theta3.max(), 10))
ax2.clabel(th2, inline=True, fontsize=15, fmt='%2.1f')

qvap2 = ax2.contour(qvapor3['lon'], qvapor3['lev'], qvapor3, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor3.min(), qvapor3.max(), 10))
ax2.clabel(qvap2, inline=True, fontsize=15, fmt='%2.1f')
ax2.set_yticks(np.arange(100, 1000.1, 100))
ax2.set_ylim([100, 1000])
ax2.set_xticks(np.arange(86.3, 87.2, 0.1))
ax2.set_xlim([86.3, 87.1])
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax2.invert_yaxis()
ax2.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax2.set_title('(b) Milbrandt', fontweight='bold', fontsize=16)
ax2.set_xticklabels([])
ax2.set_yticklabels([])
# ax2.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax2.set_ylabel('pressure level (hpa)', fontweight='bold', fontsize=20)
######################
ax3 = fig.add_subplot(gs[0, 2]) 
w_wind3 = ax3.contourf(w5['lon'], w5['lev'], w5, cmap='Spectral', 
                                  levels=k ,extend='both')

# Plot Temperature using contour (line contours with labels)
th3 = ax3.contour(theta5['lon'], theta5['lev'], theta5, colors='k', linewidths=2, 
                          levels=np.linspace(theta5.min(), theta5.max(), 10))
ax3.clabel(th3, inline=True, fontsize=15, fmt='%2.1f')

qvap3 = ax3.contour(qvapor5['lon'], qvapor5['lev'], qvapor5, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor5.min(), qvapor5.max(), 10))
ax3.clabel(qvap3, inline=True, fontsize=15, fmt='%2.1f')
ax3.set_yticks(np.arange(100, 1000.1, 100))
ax3.set_ylim([100, 1000])
ax3.set_xticks(np.arange(86.3, 87.2, 0.1))
ax3.set_xlim([86.3, 87.1])
ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax3.invert_yaxis()
ax3.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax3.set_title('(c) Thompson', fontweight='bold', fontsize=16)
# ax3.set_xticklabels([])
ax3.set_yticklabels([])
# ax3.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax3.set_ylabel('pressure level (hpa)', fontweight='bold', fontsize=20)
#########################
ax4 = fig.add_subplot(gs[1, 0]) 
w_wind4 = ax4.contourf(w7['lon'], w7['lev'], w7, cmap='Spectral', 
                                  levels=k ,extend='both')

# Plot Temperature using contour (line contours with labels)
th4 = ax4.contour(theta7['lon'], theta7['lev'], theta7, colors='k', linewidths=2, 
                          levels=np.linspace(theta7.min(), theta7.max(), 10))
ax4.clabel(th4, inline=True, fontsize=15, fmt='%2.1f')

qvap4 = ax4.contour(qvapor7['lon'], qvapor7['lev'], qvapor7, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor7.min(), qvapor7.max(), 10))
ax4.clabel(qvap4, inline=True, fontsize=15, fmt='%2.1f')
ax4.set_yticks(np.arange(100, 1000.1, 100))
ax4.set_ylim([100, 1000])
ax4.set_xticks(np.arange(86.3, 87.2, 0.1))
ax4.set_xlim([86.3, 87.1])
ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax4.invert_yaxis()
ax4.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax4.set_title('(d) Morrison', fontweight='bold', fontsize=16)
ax4.set_xlabel('Longitude', fontweight='bold', fontsize=20)
ax4.set_ylabel('pressure level (hpa)', fontweight='bold', fontsize=20)
########################
ax5 = fig.add_subplot(gs[1, 1]) 
w_wind5 = ax5.contourf(w9['lon'], w9['lev'], w9, cmap='Spectral', 
                                  levels=k ,extend='both')

# Plot Temperature using contour (line contours with labels)
th5 = ax5.contour(theta9['lon'], theta9['lev'], theta9, colors='k', linewidths=2, 
                          levels=np.linspace(theta9.min(), theta9.max(), 10))
ax5.clabel(th5, inline=True, fontsize=15, fmt='%2.1f')

qvap5 = ax5.contour(qvapor9['lon'], qvapor9['lev'], qvapor9, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor9.min(), qvapor9.max(), 10))
ax5.clabel(qvap5, inline=True, fontsize=15, fmt='%2.1f')
ax5.set_yticks(np.arange(100, 1000.1, 100))
ax5.set_ylim([100, 1000])
ax5.set_xticks(np.arange(86.3, 87.2, 0.1))
ax5.set_xlim([86.3, 87.1])
ax5.set_yticklabels([])
ax5.invert_yaxis()
ax5.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax5.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax5.set_title('(e) WSM6', fontweight='bold', fontsize=16)
ax5.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax5.set_ylabel('pressure level (hpa)', fontweight='bold', fontsize=20)

cbar1 = plt.colorbar(w_wind5, ax=[ax1, ax2, ax3, ax4, ax5], orientation='horizontal',extend='both', shrink=0.7)
cbar1.set_label('Vertical Velocity (m/s)', fontweight='bold', fontsize=12)
cbar1.ax.tick_params(labelsize=20)  # Set tick label size
cbar1.ax.yaxis.set_tick_params(rotation=45)  # Rotate y-axis labels if needed
cbar1.ax.set_position([0.25, 0.16, 0.5, 0.1])  # [x, y, width, height](L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 16,
    'ytick.major.size': 16,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})
plt.tight_layout()
plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/case1_W_theta_qvapor_vertical_crs_section.png', dpi=500, bbox_inches='tight')

plt.show()

#############
##################################
fig = plt.figure(figsize=(20, 16))
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], hspace=0.16, wspace=0.12)
#########################
ax1 = fig.add_subplot(gs[0, 0]) 
w_wind1 = ax1.contourf(w2['lon'], w2['lev'], w2, cmap='Spectral', 
                                  levels=l ,extend='both')

# Plot Temperature using contour (line contours with labels)
th1 = ax1.contour(theta2['lon'], theta2['lev'], theta2, colors='k', linewidths=2, 
                          levels=np.linspace(theta2.min(), theta2.max(), 10))
ax1.clabel(th1, inline=True, fontsize=15, fmt='%2.1f')

qvap1 = ax1.contour(qvapor2['lon'], qvapor2['lev'], qvapor2, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor2.min(), qvapor2.max(), 10))
ax1.clabel(qvap1, inline=True, fontsize=15, fmt='%2.1f')
# Axis and ticks formatting
ax1.set_yticks(np.arange(100, 1000.1, 100))
ax1.set_ylim([100, 950])
ax1.set_xticks(np.arange(84.8, 85.61, 0.1))
ax1.set_xlim([84.8, 85.6])
ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax1.invert_yaxis()
ax1.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax1.set_title('(a) Ferrier', fontweight='bold', fontsize=16)
# ax1.set_xlabel('Longitude', fontweight='bold', fontsize=20)
ax1.set_ylabel('pressure level (hpa)', fontweight='bold', fontsize=20)
ax1.set_xticklabels([])

####################
ax2 = fig.add_subplot(gs[0, 1]) 
w_wind2 = ax2.contourf(w4['lon'], w4['lev'], w4, cmap='Spectral', 
                                  levels=l ,extend='both')

# Plot Temperature using contour (line contours with labels)
th2 = ax2.contour(theta4['lon'], theta4['lev'], theta4, colors='k', linewidths=2, 
                          levels=np.linspace(theta4.min(), theta4.max(), 10))
ax2.clabel(th2, inline=True, fontsize=15, fmt='%2.1f')

qvap2 = ax2.contour(qvapor4['lon'], qvapor4['lev'], qvapor4, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor4.min(), qvapor4.max(), 10))
ax2.clabel(qvap2, inline=True, fontsize=15, fmt='%2.1f')
ax2.set_yticks(np.arange(100, 1000.1, 100))
ax2.set_ylim([100, 950])
ax2.set_xticks(np.arange(84.8, 85.61, 0.1))
ax2.set_xlim([84.8, 85.6])
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax2.invert_yaxis()
ax2.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax2.set_title('(b) Milbrandt', fontweight='bold', fontsize=16)
ax2.set_xticklabels([])
ax2.set_yticklabels([])
######################
ax3 = fig.add_subplot(gs[0, 2]) 
w_wind3 = ax3.contourf(w6['lon'], w6['lev'], w6, cmap='Spectral', 
                                  levels=l ,extend='both')

# Plot Temperature using contour (line contours with labels)
th3 = ax3.contour(theta6['lon'], theta6['lev'], theta6, colors='k', linewidths=2, 
                          levels=np.linspace(theta6.min(), theta6.max(), 10))
ax3.clabel(th3, inline=True, fontsize=15, fmt='%2.1f')

qvap3 = ax3.contour(qvapor6['lon'], qvapor6['lev'], qvapor6, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor6.min(), qvapor6.max(), 10))
ax3.clabel(qvap3, inline=True, fontsize=15, fmt='%2.1f')
ax3.set_yticks(np.arange(100, 1000.1, 100))
ax3.set_ylim([100, 950])
ax3.set_xticks(np.arange(84.8, 85.61, 0.1))
ax3.set_xlim([84.8, 85.6])
ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax3.invert_yaxis()
ax3.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax3.set_title('(c) Thompson', fontweight='bold', fontsize=16)
# ax3.set_xticklabels([])
ax3.set_yticklabels([])
#########################
ax4 = fig.add_subplot(gs[1, 0]) 
w_wind4 = ax4.contourf(w8['lon'], w8['lev'], w8, cmap='Spectral', 
                                  levels=l ,extend='both')

# Plot Temperature using contour (line contours with labels)
th4 = ax4.contour(theta8['lon'], theta8['lev'], theta8, colors='k', linewidths=2, 
                          levels=np.linspace(theta8.min(), theta8.max(), 10))
ax4.clabel(th4, inline=True, fontsize=15, fmt='%2.1f')

qvap4 = ax4.contour(qvapor8['lon'], qvapor8['lev'], qvapor8, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor8.min(), qvapor8.max(), 10))
ax4.clabel(qvap4, inline=True, fontsize=15, fmt='%2.1f')
ax4.set_yticks(np.arange(100, 1000.1, 100))
ax4.set_ylim([100, 950])
ax4.set_xticks(np.arange(84.8, 85.61, 0.1))
ax4.set_xlim([84.8, 85.6])
ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax4.invert_yaxis()
ax4.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax4.set_title('(d) Morrison', fontweight='bold', fontsize=16)
ax4.set_xlabel('Longitude', fontweight='bold', fontsize=20)
ax4.set_ylabel('pressure level (hpa)', fontweight='bold', fontsize=20)
########################
ax5 = fig.add_subplot(gs[1, 1]) 
w_wind5 = ax5.contourf(w10['lon'], w10['lev'], w10, cmap='Spectral', 
                                  levels=l ,extend='both')

# Plot Temperature using contour (line contours with labels)
th5 = ax5.contour(theta10['lon'], theta10['lev'], theta10, colors='k', linewidths=2, 
                          levels=np.linspace(theta10.min(), theta10.max(), 10))
ax5.clabel(th5, inline=True, fontsize=15, fmt='%2.1f')

qvap5 = ax5.contour(qvapor10['lon'], qvapor10['lev'], qvapor10, colors='b', linewidths=2, 
                          levels=np.linspace(qvapor10.min(), qvapor10.max(), 10))
ax5.clabel(qvap5, inline=True, fontsize=15, fmt='%2.1f')
ax5.set_yticks(np.arange(100, 1000.1, 100))
ax5.set_ylim([100, 950])
ax5.set_xticks(np.arange(84.8, 85.61, 0.1))
ax5.set_xlim([84.8, 85.6])
ax5.set_yticklabels([])
ax5.invert_yaxis()
ax5.tick_params(axis='both', labelrotation=45, labelsize=15, width=1, length=8)  
ax5.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1f}°E'.format(x)))
ax5.set_title('(e) WSM6', fontweight='bold', fontsize=16)
ax5.set_xlabel('Longitude', fontweight='bold', fontsize=20)
# ax5.set_ylabel('pressure level (hpa)', fontweight='bold', fontsize=20)

cbar2 = plt.colorbar(w_wind5, ax=[ax1, ax2, ax3, ax4, ax5], orientation='horizontal',extend='both', shrink=0.7)
cbar2.set_label('Vertical Velocity (m/s)', fontsize=12)
cbar2.ax.tick_params(labelsize=20)  # Set tick label size
cbar2.ax.yaxis.set_tick_params(rotation=45)  # Rotate y-axis labels if needed
cbar2.ax.set_position([0.25, 0.16, 0.5, 0.1]) # (L-R, T-B, CBAR width, cbar length   Adjust the po,sition and size of the colorbar
plt.rcParams.update({
    "font.weight": "bold",
    "axes.labelweight": "bold",
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    "axes.linewidth": 2,
    "patch.linewidth": 2,
    'xtick.major.size': 16,
    'ytick.major.size': 16,
    'xtick.major.width': 2,
    'ytick.major.width': 2,
    'axes.titlesize': 22,  # For axes titles
    'figure.titlesize': 24  # For overall figure title
})
plt.tight_layout()
plt.savefig('/home/lab/Desktop/Narayanswamy/work_fig/case2_W_theta_qvapor_vertical_crs_section.png', dpi=500, bbox_inches='tight')

plt.show()



