import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

EXCEL_PATH = "DEoutput_all_12122024.xlsx"
SHEET = "DEoutput"

ALPHA = 0.05
LOG2FC_CUTOFF = 1.0  

# 1) Load with two header rows 
df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET, header=[0, 1])

# These are your comparison blocks in the file:
blocks = [
    "WT_4dpi_vs_uninjured",
    "KO_4dpi_vs_uninjured",
    "KO_vs_WT_uninjured",
    "KO_vs_WT_4dpi",
    "Interaction",
]

gene_col = ("Pid", "Gene")  # where gene names live in your file

def volcano(block):
    lfc = df[(block, "logFC")]
    padj = df[(block, "adj.P.Val")]

    tmp = pd.DataFrame({"logFC": lfc, "padj": padj}).dropna()
    tmp["neglog10_padj"] = -np.log10(tmp["padj"].clip(lower=1e-300))

    sig = (tmp["padj"] < ALPHA) & (tmp["logFC"].abs() >= LOG2FC_CUTOFF)

    plt.figure(figsize=(6, 5))
    plt.scatter(tmp.loc[~sig, "logFC"], tmp.loc[~sig, "neglog10_padj"], s=10, alpha=0.4)
    plt.scatter(tmp.loc[sig, "logFC"], tmp.loc[sig, "neglog10_padj"], s=12, alpha=0.7)

    plt.axvline(+LOG2FC_CUTOFF, linestyle="--", linewidth=1)
    plt.axvline(-LOG2FC_CUTOFF, linestyle="--", linewidth=1)
    plt.axhline(-np.log10(ALPHA), linestyle="--", linewidth=1)

    plt.title(f"Volcano: {block}")
    plt.xlabel("log2 Fold Change (logFC)")
    plt.ylabel("-log10(adj.P.Val)")
    plt.tight_layout()
    plt.show()

# 2) Summary: number of significant proteins per block
sig_counts = {}
for b in blocks:
    lfc = df[(b, "logFC")]
    padj = df[(b, "adj.P.Val")]
    sig_counts[b] = int(((padj < ALPHA) & (lfc.abs() >= LOG2FC_CUTOFF)).sum())

print("Significant proteins per comparison:")
for k, v in sig_counts.items():
    print(f"{k}: {v}")

# Bar plot of counts
plt.figure(figsize=(8, 4))
plt.bar(list(sig_counts.keys()), list(sig_counts.values()))
plt.xticks(rotation=45, ha="right")
plt.ylabel(f"# significant (adj.P.Val<{ALPHA}, |logFC|>={LOG2FC_CUTOFF})")
plt.title("Significant proteins per comparison")
plt.tight_layout()
plt.show()

# 3) Volcano plots
for b in blocks:
    volcano(b)

# 4) Top hits bar plot for one comparison 
b = "WT_4dpi_vs_uninjured"
tmp = pd.DataFrame({
    "Gene": df[gene_col],
    "logFC": df[(b, "logFC")],
    "padj": df[(b, "adj.P.Val")]
}).dropna()

hits = tmp[(tmp["padj"] < ALPHA) & (tmp["logFC"].abs() >= LOG2FC_CUTOFF)].copy()
top10 = hits.reindex(hits["logFC"].abs().sort_values(ascending=False).index).head(10)

plt.figure(figsize=(10, 4))
plt.bar(top10["Gene"].astype(str), top10["logFC"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("logFC")
plt.title(f"Top 10 hits by |logFC|: {b}")
plt.tight_layout()
plt.show()
