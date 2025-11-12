import argparse
from nernst_logic import nernst_potential_mv

def main():
    parser = argparse.ArgumentParser(description="Compute Nernst equilibrium potential (mV).")
    parser.add_argument("--out", type=float, required=True, help="Extracellular [out] (mM)")
    parser.add_argument("--inside", type=float, required=True, help="Intracellular [in] (mM)")
    parser.add_argument("--z", type=int, default=1, help="Ion valence (e.g., 1 for K+, -1 for Cl-)")
    parser.add_argument("--temp", type=float, default=37.0, help="Temperature (°C)")
    args = parser.parse_args()

    result = nernst_potential_mv(args.out, args.inside, args.z, args.temp)
    print(f"Nernst potential: {result:.2f} mV")

if __name__ == "__main__":
    main()
