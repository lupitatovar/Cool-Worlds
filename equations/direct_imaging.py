import numpy as np
import astropy
from astropy import constants as ac
from astropy import units as u

"""
The equations below calculate contrast, position on the sky, and inner working angle (IWA). All of these values are needed
when trying to see if a given target can be observed with direct imaging.

"""

def lambertian (b):
'''
lambertian function, we assume observations are at quadrature (90 degrees) which yield psi ~0.3
'''
    psi = ((np.sin(b)) + (np.pi-b) * np.cos(b)) /(np.pi)
    return psi

def contrast(p,l,Rp,r):
'''
Based on Brown et al., (2005) equation 3
Delta_mag = -2.5log({F_p}/{F_s}) =  -2.5log[p*Phi(beta)({R}\{r})^2]

where r = distance between planet and the star

beta = phase angle (can assume quadrature so 90 degrees)

Phi(beta) = planetary phase function (lambertian)

R = radius of planet

p = geometric albedo of planet (.33 for Earth-like) and


Phi_L(beta) = [(sin(beta) + (pi-beta))* cos(beta)] \ (pi)
l=lambertian ~ 0.3
'''
    dmag = 2.5 * (p*l*(Rp/r)**2)
    return dmag

def theta(a,d):
'''
Now calculating the position of the targets on the sky. This will help test to see if they fall within the IWA
theta = separation (semi-major axis)/distance to star (d)

'''
    angle = a/d
    return angle

def iwa(x,l,D):
'''
IWA = x*lambda (wavelength to observe) / Diameter of mirror
IWA will cut off the longest wavelengths for planets around more distant stars
x is usually 2 or 3 depending on how good of a coronagraph you have (3 is what LUVEx is aiming for)
'''
    IWA = x*l/D
    return IWA
