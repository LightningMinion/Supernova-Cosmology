import numpy as np
import scipy as scp

def scale_factor(z):
    return 1/(1+z)

z = 0.1
a = scale_factor(z)
H0 = 75
omega_DE = 0.669
omega_M = 1 - omega_DE
c = 299792.458

def Friedmann_eq(z):
    a = scale_factor(z)
    return H0*np.sqrt(omega_M/(a**3) + omega_DE + (1-omega_M-omega_DE)/(a**2))

def integrand(z):
    return c/Friedmann_eq(z)

def co_moving_dist(z_up):
    dist, err = scp.integrate.quad(integrand, 0, z_up)
    return dist

def co_moving_dist_near(z):
    return z*c/H0

rc = co_moving_dist(z)
print(rc)

def flux_model(rc, Lp, z):
    flux = Lp/(4*np.pi*(rc**2)*((1+z)*2))
#then convert this to magnitudes and compare with the data

#use this to find Lp using chi-sq minimisation
def flux_model_near(Lp, z):
    rc = co_moving_dist_near(z)
    flux = Lp/(4*np.pi*(rc)**2*((1+z)**2))
    #convert to mags
    return flux