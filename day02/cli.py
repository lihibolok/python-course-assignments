"""
Command-line Nernst potential calculator.

"""

import argparse
from core import nernst_potential


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compute the Nernst equilibrium potential (in mV) for an ion."
    )
    parser.add_argument(
        "--out",
        type=float,
        required=True,
        help="Extracellular concentration [out] in mM.",
    )
    parser.add_argument(
        "--inside",
        type=float,
        required=True,
        help="Intracellular concentration [in] in mM.",
    )
    parser.add_argument(
        "--z",
        type=int,
        default=1,
        help="Ion valence (default: 1, e.g., for K+ or Na+).",
    )
    parser.add_argument(
        "--temp",
        type=float,
        default=37.0,
        help="Temperature in °C (default: 37).",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        E_mV = nernst_potential(
            conc_out_mM=args.out,
            conc_in_mM=args.inside,
            z=args.z,
            temperature_c=args.temp,
        )
        print(f"Nernst potential: {E_mV:.2f} mV")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
