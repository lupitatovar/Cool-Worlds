import numpy as np
import astropy
from astropy import constants as ac
from astropy import units as u

'The equation below calculates surface temperatures. If used cite Quick et al., 2023 (in prep)'

def T_eff(L,A,em,a):

    #Earth like values: A=0.3 ; em = 0.85
    #Europa-like value: A = 0.55 ; em=0.9
    #Enceladus-like values: A = 0.81 ; em =1
    temp = ((L*ac.L_sun * (1-A)) / (16 * np.pi * ac.sigma_sb * em * (a*ac.au)**2)) ** (1/4)
    return temp
