# Day 08 – Proteomics Analysis (Python Assignment)

This project uses a real proteomics differential-expression dataset (`DEoutput_all_12122024.xlsx`) to demonstrate data analysis with **Pandas**, **NumPy**, and **Matplotlib**.

## What the Script Does
- Loads the Excel file (two header rows with comparison blocks).
- Extracts `logFC` (log2 fold change) and `adj.P.Val` (FDR-corrected p-value).
- Counts how many proteins are significantly changed in each comparison.
- Plots:
  - A bar chart of significant protein counts.
  - Volcano plots for each comparison.
  - A bar plot of the top 10 strongest protein changes.

## Meaning of the Graphs
- **Bar plot:** shows how many proteins change significantly between conditions.
- **Volcano plots:** highlight proteins with large fold changes and strong statistical significance.
- **Top-10 bar plot:** shows proteins with the largest response in a selected comparison.

## How to Run
From the `day08` folder:
python3 proteomics_analysis.py

Required packages:
python3 -m pip install pandas numpy matplotlib openpyxl

