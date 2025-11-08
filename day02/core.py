"""
Core logic for the Nernst potential calculator.

This module provides a function to compute the Nernst equilibrium potential (in mV)
for an ion given its intra-/extracellular concentrations, valence, and temperature.
"""

import math


def nernst_potential(
    conc_out_mM: float,
    conc_in_mM: float,
    z: int = 1,
    temperature_c: float = 37.0,
) -> float:
    """
    Calculate the Nernst equilibrium potential (in millivolts, mV).

    Parameters
    ----------
    conc_out_mM : float
        Extracellular concentration of the ion (in mM).
    conc_in_mM : float
        Intracellular concentration of the ion (in mM).
    z : int, optional
        Valence (charge) of the ion.
        Examples: +1 for K+, Na+; -1 for Cl-. Default is +1.
    temperature_c : float, optional
        Temperature in degrees Celsius. Default is 37°C.

    Returns
    -------
    float
        Nernst potential in millivolts (mV).

    Notes
    -----
    Formula:
        E = (R * T / (z * F)) * ln([out] / [in]) * 1000

    Where:
        R = 8.314 J/(mol·K)
        F = 96485 C/mol
        T = temperature in Kelvin
    """
    if conc_in_mM <= 0 or conc_out_mM <= 0:
        raise ValueError("Concentrations must be positive.")

    R = 8.314  # J/(mol·K)
    F = 96485  # C/mol
    T = temperature_c + 273.15  # Kelvin

    ratio = conc_out_mM / conc_in_mM
    E_volts = (R * T / (z * F)) * math.log(ratio)
    E_mV = E_volts * 1000.0
    return E_mV
