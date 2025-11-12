import numpy as np

def nernst_potential_mv(out_conc, in_conc, z=1, temp_c=37.0):
    """
    Calculate Nernst equilibrium potential (in mV)
    E = (R * T / (z * F)) * ln([out]/[in]) * 1000
    """
    R = 8.314  # gas constant (J/mol*K)
    F = 96485  # Faraday constant (C/mol)
    T = temp_c + 273.15  # convert to Kelvin
    return (R * T / (z * F)) * np.log(out_conc / in_conc) * 1000
