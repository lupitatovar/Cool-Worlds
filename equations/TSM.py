import numpy as np
import astropy
from astropy import constants as ac
from astropy import units as u

"""
The equation below calculates the transimission spectroscopy metric (TSM). If used cite Kempton et al., 2018
A note: The Kempton et al. TSM metric is based upon the Louie 2008 paper which assumed that planets <1.5Re had
water atmospheres (mu ~18), and that planets above 1.5Re had H/He atmospheres (mu ~2.3). Therefore, if the planet
has no atmosphere at all, TSM does not apply. It would be extremely challenging to detect plumes from the planet.
Since the TSM is based upon absorption of stellar radiation by the atmosphere, very little stellar flux could be
absorbed by a plume. Would need to consider reflected light instead '
mj = magnitude of star in j band
"""
def tsm(sf,Rp,Teq,Mp,Rs,mj):
    #sf = 0.190 (for planets with radii < 1.5 earth radius)
    #sf = 1.26 for planets 1.5<rp<2.75
    tsm_ = sf * ((Rp**3 * Teq) / (Mp * Rs**2)) * 10**(-mj/5)
    return tsm_
