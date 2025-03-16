import numpy as np
import matplotlib.pyplot as plt

def w0w1CDM(z, w0, w1):
    return w0 + w1*z
def w_CPL(z, w0, w1):
    return w0 + w1*z/(1+z)
def w_logCDM(z, w0, w1):
    w0 + w1*(np.log(2+z)/(1+z) - np.log(2))
def w_sinCDM(z, w0, w1):
    w0 + w1*(np.sin(1+z)/(1+z) - np.sin(1))
    

trial_z = np.linspace(-0.99, 10, 1000)
plt.figure()
plt.scatter(trial_z, w0w1CDM(trial_z, -1, 0), label="LCDM")
plt.scatter(trial_z, w0w1CDM(trial_z, -0.75, 0), label = "wCDM")
plt.scatter(trial_z, w0w1CDM(trial_z, -0.5, -3.7), label = "w0w1CDM")
plt.scatter(trial_z, w0w1CDM(trial_z, -0.78, -0.68), label = "w0w1CDM + H0")
plt.scatter(trial_z, w_logCDM(trial_z, -0.76, 4.6), label="logarithmic")
plt.scatter(trial_z, w_sinCDM(trial_z, -0.76, 1.8), label = "oscillatory")
plt.scatter(trial_z, w_sinCDM(trial_z, -1, 2.7), label = "Msin")
plt.scatter(trial_z, w_CPL(trial_z, -0.66, -2.2), label = "CPL")
plt.ylabel("w")
plt.xlabel("z")
plt.legend()
plt.savefig("w-redshift-relation.png")
plt.show()