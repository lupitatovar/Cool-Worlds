import numpy as np
import astropy
from astropy import constants as ac
from astropy import units as u

def h_tidal(p,r,e):
    '''
    The equation that calculates the amount of heat imparted to the planet by tidal sources.
    '''
    #k2 is the degree2 love muber that describes how a planet responds to the tide raised on it by its primary
    #(0=rigid, 1.5= fluid); typically assumed to be 0.3 for studies of terrestrial and icy worlds

    k2 = 0.3

    # omega is the orbital period
    omega = (2*np.pi) / ((p*u.day).to(u.second))

    # Q is a quality factor; assumed to be 100 for tidal dissipation studies of moons in our SS
    Q = 100.

    h_tidal = (21/2) * ((k2 * (omega**5) * ((r*ac.R_earth)**5) * (e**2))/(ac.G * Q))
    return h_tidal


def h_radio(r,m):
    '''
    Equation that calculates the amount of heat imparted to the planet by radiogenic sources. Users can set which mantle assumptions to make.
    '''
    h = 1.59 * 10** -11 *u.W*u.kg**-1
    
    def Earth_Mantle(r,m):
        '''
        Equation that defines what mantle assumptions we are making in order to calculate the radiogenic heating component.
        It depends on the radius and mass of the planet. Here we assume an Earth-like mantle.
        '''
        volume = 0.84 * (4/3) * np.pi * (r*ac.R_earth)**3
        rho = 4000 * (u.kg*u.m**-3)#m*ac.M_earth / volume
        Mantle = 0.84 * (4/3) * np.pi * (r*ac.R_earth)**3 * rho
        return Mantle
    
    radio = h * Earth_Mantle(r,m)
    return radio


def h_total(p,r,e,m):
    '''
    Equation that calculates the total internal heating of a planet

    References
    --------------
    Quick et al. (2020)

    Parameters
    ----------
    p : float
        The period of the planet
    r : float
        The radius of the planet
    e : float
        The eccentricity of the planet
    m : float
        The mass of the planet
    Mantle: float
        The type of Mantle that is being assummed

    Returns
    -------
    total : 1-d array
    '''

    total = h_tidal(p,r,e) + h_radio(r,m)
    return (total)
