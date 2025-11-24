# MasterMind – Python Game (Day 05 Assignment)

This project implements a simple version of the classic **MasterMind** logic game.

The computer generates a **4-digit number**, all digits different, and you try to guess it.
After each guess:

- `*` means: correct digit in the correct position  
- `+` means: correct digit in the wrong position  

Example:

Secret: 2153 (hidden)
Guess: 2715 → *++

---

## Installation

This project requires **only Python**.  
No external dependencies.

Tested with Python **3.10+**.

---

## How to Run the Game

In the terminal:

python mastermind.py

You will be asked to enter guesses until you find the correct 4-digit number.

---

## Running the Tests

Tests are written using `pytest`.

Install pytest if needed:

pip install pytest

Run the tests:

pytest -q


