"""
Interactive Nernst potential calculator (input() version).

Asks the user for intra-/extracellular concentrations, ion valence, and temperature,
then prints the Nernst equilibrium potential in mV.
"""

from core import nernst_potential


def main():
    print("=== Nernst Potential Calculator (Interactive) ===")
    print("This program computes the Nernst equilibrium potential (in mV).")
    print()

    conc_out_str = input("Enter extracellular concentration [out] (mM): ")
    conc_in_str = input("Enter intracellular concentration [in] (mM): ")
    z_str = input("Enter ion valence z (e.g., 1 for K+/Na+, -1 for Cl-): ")
    temp_str = input("Enter temperature (°C, press Enter for 37°C): ")

    try:
        conc_out = float(conc_out_str)
        conc_in = float(conc_in_str)
        z = int(z_str) if z_str.strip() else 1
        temperature_c = float(temp_str) if temp_str.strip() else 37.0

        E_mV = nernst_potential(conc_out, conc_in, z=z, temperature_c=temperature_c)
        print()
        print(f"Nernst potential: {E_mV:.2f} mV")
    except ValueError as e:
        print()
        print("Error:", e)
        print("Please make sure you enter valid numeric values.")


if __name__ == "__main__":
    main()
