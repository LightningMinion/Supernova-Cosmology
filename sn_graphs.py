import numpy as np
import matplotlib.pyplot as plt
sn_z_near, sn_mag_near, sn_mag_err_near =  np.loadtxt("sn_data_nearby.txt", unpack = True, usecols=(1,2,3))
plt.figure(1)
plt.errorbar(sn_z_near, sn_mag_near, yerr=sn_mag_err_near, marker = "x", linestyle = 'None', color = "red", label = "nearby SN")
sn_z_far, sn_mag_far, sn_mag_err_far =  np.loadtxt("sn_data_distant.txt", usecols=(1,2,3), unpack = True)
plt.errorbar(sn_z_far, sn_mag_far, yerr=sn_mag_err_far, marker = "x", linestyle = 'None', color = "blue", label = "distant SN")
plt.xlabel("redshift")
plt.ylabel("effective magnitude")
plt.legend()
plt.title("The effective magnitudes of extragalactic supernovae (SN) as a function of redshift")
plt.show()