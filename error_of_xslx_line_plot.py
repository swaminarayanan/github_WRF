import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
import pandas as pd

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Circle

# Read the Excel file
file_path = "/home/lab/Desktop/Narayanswamy/work_scripts/2019_03_15_hail.xlsx"  # Replace with the path to your Excel file
sheet_name1 = "Sheet3"    # 20190315 Replace with the sheet name if necessary
sheet_name2 = "Sheet2"    # 20200303 Replace with the sheet name if necessary

# Load the data into a pandas DataFrame
df1 = pd.read_excel(file_path, sheet_name=sheet_name1)
df2 = pd.read_excel(file_path, sheet_name=sheet_name2)

# # Check the DataFrame structure
# print(df1.head())  # Displays the first few rows of the DataFrame
# print(df2.head())  # Displays the first few rows of the DataFrame
# print(df1.head())
# print(df1.columns)
# print(df1.info())

# # Plotting
# df1[x_column] = "A"  # Replace with the column name for x-axis
# y_column = "B"  # Replace with the column name for y-axis

# plt.figure(figsize=(10, 6))  # Set figure size
# plt.plot(df1[x_column], df1[y_column], marker='o', label=y_column)  # Line plot with markers

# # Customize the plot
# plt.title("Line Plot of Excel Data", fontsize=16)
# plt.xlabel(df1[x_column], fontsize=14)
# plt.ylabel(y_column, fontsize=14)
# plt.grid(True, linestyle='--', alpha=0.6)  # Add grid lines
# plt.legend(fontsize=12)
# plt.tight_layout()  # Adjust layout for better visualization

# # Show the plot
# plt.show()

# Specify the correct column names
x_column = "SNO"  # Serial number for x-axis
y_column = "T_ERR_19"  # Temperature error for y-axis
y1_column = "T_ERR_20"  # Temperature error for y-axis
y2_column = "TD_ERR_19"  # Temperature error for y-axis
y3_column = "TD_ERR_20"  # Temperature error for y-axis
y4_column = "RH_ERR_19"  # Temperature error for y-axis
y5_column = "RH_ERR_20"  # Temperature error for y-axis
y6_column = "PRCP_ERR_19"  # Temperature error for y-axis
y7_column = "PRCP_ERR_20"  # Temperature error for y-axis

# plt.figure(figsize=(10, 6))  # Set figure size
# plt.plot(df1[x_column], df1[y_column], color='red', linestyle=(0, (5, 10)), linewidth=1, label='case 1 model')  # Line plot with markers
# plt.plot(df1[x_column], df1[y1_column], marker='D', color='r', label=y1_column)  # Line plot with markers

# # Customize the plot
# plt.title("Line Plot of Excel Data", fontsize=16)
# plt.xlabel('time', fontsize=14)
# plt.ylabel('error rate', fontsize=14)
# plt.grid(True, linestyle='--', alpha=0.6)  # Add grid lines
# plt.legend(fontsize=12)
# plt.tight_layout()  # Adjust layout for better visualization

# # Show the plot
# plt.show()

fig = plt.figure(figsize=(12, 12))
gs = gridspec.GridSpec(4, 1, width_ratios=[2], hspace=0.55, wspace=0.12)

ax4 = fig.add_subplot(gs[0, 0])
pcm4 = ax4.plot(df1[x_column], df1[y6_column], color='red', linestyle=(0, (5, 10)), linewidth=1, label='case 1')
pcm4 = ax4.plot(df1[x_column], df1[y7_column], color='k', linestyle=(0, (5, 10)), linewidth=1, label='case 2')
for x, y in zip(df1[x_column], df1[y6_column]):
    ax4.text(x, y, '1', fontsize=8, ha='center', va='center', color='red')
for x, y in zip(df1[x_column], df1[y7_column]):
    ax4.text(x, y, '2', fontsize=8, ha='center', va='center', color='k')
# dtFmt = mdates.DateFormatter('%H')
# ax1.xaxis.set_major_formatter(dtFmt)
ax4.set_xticks(np.arange(0, 24.1, 3))
ax4.set_xlim([0, 24])
# ax4.set_xlabel('time', fontsize=18)
ax4.set_ylabel('error rate', fontsize=18)
ax4.legend()
ax4.tick_params(axis='both', length=5, width=1.2)
ax4.tick_params(axis='both', labelsize=16)


# First subplot: ax1
ax1 = fig.add_subplot(gs[1, 0])
pcm1 = ax1.plot(df1[x_column], df1[y_column], color='red', linestyle=(0, (5, 10)), linewidth=1, label='case 1')
pcm1 = ax1.plot(df1[x_column], df1[y1_column], color='k', linestyle=(0, (5, 10)), linewidth=1, label='case 2')
for x, y in zip(df1[x_column], df1[y_column]):
    ax1.text(x, y, '1', fontsize=8, ha='center', va='center', color='red')
for x, y in zip(df1[x_column], df1[y1_column]):
    ax1.text(x, y, '2', fontsize=8, ha='center', va='center', color='k')
# dtFmt = mdates.DateFormatter('%H')
# ax1.xaxis.set_major_formatter(dtFmt)
ax1.set_xticks(np.arange(0, 24.1, 3))
ax1.set_xlim([0, 24])
# ax1.set_xlabel('time', fontsize=18)
ax1.legend(loc='upper left')
ax1.set_ylabel('error rate', fontsize=18)
ax1.tick_params(axis='both', length=5, width=1.2)
ax1.tick_params(axis='both', labelsize=16)

# ax1.set_yticks(np.arange(21, 25.1, 1))
# ax1.set_xlim([])
# # ax1.set_ylim([21, 25.1])
# ax1.set_xticks(np.arange(0, 24 + 1, 3))  # Ensure to include the last tick (24)

# Set x-axis limits to cover 24 hours

# # Modify the X-tick labels to show longitude with "E"
# ax1.set_xticklabels([f'{tick:.0f}°E' for tick in np.arange(82, 88.61, 1)], fontsize=10, fontweight='bold')

# # Modify the Y-tick labels to show latitude with "N"
# ax1.set_yticklabels([f'{tick:.0f}°N' for tick in np.arange(21, 25.1, 1)], fontsize=10, fontweight='bold')

# Second subplot: ax2
ax2 = fig.add_subplot(gs[2, 0])
pcm2 = ax2.plot(df1[x_column], df1[y2_column], color='red', linestyle=(0, (5, 10)), linewidth=1, label='case 1')
pcm2 = ax2.plot(df1[x_column], df1[y3_column], color='k', linestyle=(0, (5, 10)), linewidth=1, label='case 2')
for x, y in zip(df1[x_column], df1[y2_column]):
    ax2.text(x, y, '1', fontsize=8, ha='center', va='center', color='red')
for x, y in zip(df1[x_column], df1[y3_column]):
    ax2.text(x, y, '2', fontsize=8, ha='center', va='center', color='k')
ax2.set_xticks(np.arange(0, 24.1, 3))
ax2.set_xlim([0, 24])
# ax2.set_xlabel('time', fontsize=18)
ax2.legend()
ax2.set_ylabel('error rate', fontsize=18)
ax2.tick_params(axis='both', length=5, width=1.2)
ax2.tick_params(axis='both', labelsize=16)

# dtFmt = mdates.DateFormatter('%H')
# ax2.xaxis.set_major_formatter(dtFmt)

ax3 = fig.add_subplot(gs[3, 0])
pcm3 = ax3.plot(df1[x_column], df1[y4_column], color='red', linestyle=(0, (5, 10)), linewidth=1, label='case 1')
pcm3 = ax3.plot(df1[x_column], df1[y5_column], color='k', linestyle=(0, (5, 10)), linewidth=1, label='case 2')
for x, y in zip(df1[x_column], df1[y4_column]):
    ax3.text(x, y, '1', fontsize=8, ha='center', va='center', color='red')
for x, y in zip(df1[x_column], df1[y5_column]):
    ax3.text(x, y, '2', fontsize=8, ha='center', va='center', color='k')
ax3.set_xticks(np.arange(0, 24.1, 3))
ax3.set_xlim([0, 24])
ax3.legend()
ax3.set_xlabel('time', fontsize=18)
ax3.set_ylabel('error rate', fontsize=18)
ax3.tick_params(axis='both', length=5, width=1.2)
ax3.tick_params(axis='both', labelsize=16)

ax1.set_title('(b) temperature error', fontsize=18, fontweight='bold')
ax2.set_title('(c) dew point temp_error', fontsize=18, fontweight='bold')
ax3.set_title('(d) relative humidity error', fontsize=18, fontweight='bold')
ax4.set_title('(a) precipitation error', fontsize=18, fontweight='bold')
plt.rcParams.update({
    "font.weight": "bold",          # Set the default font weight to bold
    "axes.labelweight": "bold",     # Axis label font weight
    'xtick.labelsize': 15,          # X-axis tick label size
    'ytick.labelsize': 15,          # Y-axis tick label size
    "axes.linewidth": 2,            # Line width for the axes
    "patch.linewidth": 2,           # Line width for patches (e.g., circles, rectangles)
    'xtick.major.size': 19,         # Major tick size for X-axis
    'ytick.major.size': 19,         # Major tick size for Y-axis
    'xtick.major.width': 2,         # Major tick width for X-axis
    'ytick.major.width': 2,         # Major tick width for Y-axis
    'axes.titlesize': 16,           # Font size for subplot (ax1, ax2) titles
    'axes.titleweight': 'bold',     # Font weight for subplot titles
    'figure.titlesize': 16,         # Font size for the overall figure title (suptitle)
    'figure.titleweight': 'bold',   # Font weight for the overall figure title
})

plt.show()
 