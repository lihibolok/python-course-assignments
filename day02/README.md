# Day 02 – Nernst Potential Calculator

## Description  
This program calculates the Nernst equilibrium potential (mV) for an ion based on its intra- and extracellular concentrations, valence, and temperature.  
It demonstrates the use of three different input mechanisms in Python: interactive input, command-line arguments, and a simple GUI.

---

## Files
- **core.py** – Core function implementing the Nernst equation.  
- **interactive.py** – Interactive version using `input()` for user input.  
- **cli.py** – Command-line version using `argparse` for direct parameter passing.  
- **gui.py** – GUI version built with `tkinter`.  
- **README.md** – Documentation of the assignment and process.

---

## Process  
I first implemented the Nernst equation in a reusable function inside `core.py`, then created three different interfaces that all use the same core logic.  
Each version demonstrates a distinct way of handling user input in Python while ensuring consistency of computation.

---

## Use of AI Assistance  
I used ChatGPT (GPT-5) to help plan and structure the project, ensuring I understood the Nernst equation and how to apply it programmatically.  

**Prompts summary:**  
- I explained that I wanted to build a Nernst potential calculator based on the equation  
  E = (RT / (zF)) * ln([out]/[in]) * 1000, and asked for help structuring the code cleanly and modularly.

- I asked how to separate the project into a core computation file and three interfaces (interactive, CLI using `argparse`, and GUI using Tkinter) that all reuse the same function.

