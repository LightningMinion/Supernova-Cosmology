import numpy as np
import matplotlib.pyplot as plt
import corner
import pylab as pl
import pandas as pd
%pylab inline
zmax = 3
zmin = -1

trial_z = np.linspace(zmin, zmax, 1000)
trial_z2 = np.linspace(-0.99, zmax, 1000)

plt.figure()
w_lcdm_vals = trial_z*0 - 1
w_wcdm_vals = trial_z*0 -0.75
w_w0w1cdm_vals = -0.5 -3.7*trial_z
w_w0w1cdmH0_vals = -0.68*trial_z - 0.76
w_logcdm_vals = -0.76 + 4.6*(np.log(2+trial_z2)/(1+trial_z2) - np.log(2))
w_CPLcdm_vals = -0.66 -2.2*trial_z2/(1+trial_z2)
w_sincdm_vals = -0.76 + 1.8*(np.sin(1+trial_z)/(1+trial_z) - np.sin(1))
w_Msincdm_vals = -1 + 2.7*(np.sin(1+trial_z)/(1+trial_z) - np.sin(1))
plt.plot(trial_z, w_lcdm_vals, label="LCDM", color = "blue")
plt.plot(trial_z, w_wcdm_vals, label = "wCDM", color = "cyan")
plt.plot(trial_z, w_w0w1cdm_vals, label = "w0w1CDM", color = "green")
plt.plot(trial_z, w_w0w1cdmH0_vals, label = "w0w1CDM + H0", color = "lime")
plt.plot(trial_z, w_logcdm_vals, label="logarithmic", color = "grey")
plt.plot(trial_z, w_sincdm_vals, label = "oscillatory", color = "red")
plt.plot(trial_z, w_Msincdm_vals, label = "Msin", color = "pink")
plt.plot(trial_z, w_CPLcdm_vals, label = "CPL", color = "orange")
plt.axhline(0, linestyle = "--", color = "black")
plt.axvline(0, linestyle = "dotted", color = "black")
plt.text(2, 0.1, "attractive")
plt.text(2, -0.2, "repulsive")
plt.text(-0.01, 0.8, "future")
plt.text(0.25, 0.8, "past")
plt.ylabel("w")
plt.xlabel("z")
plt.legend()
plt.xlim(zmax, zmin)
plt.ylim(-4, 1)
plt.savefig("w-redshift-relation.png")
plt.show()

# MCMC chain samples
samples = np.loadtxt('COM_CosmoParams_fullGrid_R2.00/base/WMAP/base_WMAP_1.txt')

# load the column names for the samples
column_names_raw = np.loadtxt('data/COM_CosmoParams_fullGrid_R2.00/base/WMAP/base_WMAP.paramnames', dtype=np.str, usecols=[0])
column_names = [x.replace("b'",'').replace("'",'') for x in column_names_raw]

# make a data frame with column names and samples
samples1 = pd.DataFrame(samples[:,2:], columns=column_names) # first two columns are not important