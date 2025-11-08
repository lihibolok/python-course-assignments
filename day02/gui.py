"""
GUI-based Nernst potential calculator using Tkinter.

Provides a small window where the user can enter:
- [out] (mM)
- [in] (mM)
- z (valence)
- Temperature (°C)

and see the resulting Nernst potential in mV.
"""

import tkinter as tk
from core import nernst_potential


def calculate():
    try:
        conc_out = float(entry_out.get())
        conc_in = float(entry_in.get())
        z_text = entry_z.get().strip()
        temp_text = entry_temp.get().strip()

        z = int(z_text) if z_text else 1
        temperature_c = float(temp_text) if temp_text else 37.0

        E_mV = nernst_potential(conc_out, conc_in, z=z, temperature_c=temperature_c)
        label_result.config(text=f"Nernst potential: {E_mV:.2f} mV")
    except ValueError as e:
        label_result.config(text=f"Error: {e}")


# Create main window
root = tk.Tk()
root.title("Nernst Potential Calculator")

# Layout
tk.Label(root, text="Extracellular [out] (mM):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_out = tk.Entry(root, width=15)
entry_out.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Intracellular [in] (mM):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_in = tk.Entry(root, width=15)
entry_in.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Ion valence z:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_z = tk.Entry(root, width=15)
entry_z.insert(0, "1")  # default
entry_z.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Temperature (°C):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_temp = tk.Entry(root, width=15)
entry_temp.insert(0, "37.0")  # default
entry_temp.grid(row=3, column=1, padx=5, pady=5)

btn = tk.Button(root, text="Calculate", command=calculate)
btn.grid(row=4, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Nernst potential: ", fg="blue")
label_result.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
