#!/usr/bin/env python
# coding: utf-8

# In[3]:


# ============================
# OCP vs Time — Single CSV Plotter for Local Notebook
# File expected in the same folder: AS_Eocp.csv
# ============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from IPython.display import FileLink, display

# ----------------------------
# File names
# ----------------------------
csv_name = "AS_Eocp.csv"
out_png = "AS_Eocp_plot.png"
out_svg = "AS_Eocp_plot.svg"

# ----------------------------
# Read CSV
# ----------------------------
df = pd.read_csv(csv_name)

# Clean column names
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Actual columns in uploaded file
# ----------------------------
time_col = "time[min]"
ocp_col  = "E[mV]"

# Check required columns
if time_col not in df.columns or ocp_col not in df.columns:
    raise KeyError(
        f"Expected columns '{time_col}' and '{ocp_col}' not found.\n"
        f"Available columns: {df.columns.tolist()}"
    )

# Keep only needed columns
df = df[[time_col, ocp_col]].copy()
df.columns = ["time", "E"]

# Convert to numeric
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df["E"]    = pd.to_numeric(df["E"], errors="coerce")

# Drop invalid rows
df = df.dropna().reset_index(drop=True)

if df.empty:
    raise ValueError("No valid numeric data found after cleaning the CSV.")

# ----------------------------
# Bright color palette
# ----------------------------
line_color = "#00CFFF"   # bright turquoise/cyan

# ----------------------------
# Plot
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["time"],
    df["E"],
    linestyle="-",
    linewidth=4,
    color=line_color,
    label="AS"
)

# ----------------------------
# Axis labels
# ----------------------------
ax.set_xlabel("Time (min)", fontsize=26, fontweight="bold")
ax.set_ylabel("OCP (mV)", fontsize=26, fontweight="bold")

# ----------------------------
# Axis limits and ticks
# ----------------------------
min_E = df["E"].min()
max_E = df["E"].max()

ax.set_xlim(0, 60)
ax.set_xticks(np.arange(0, 61, 20))

bottom = min(-450, np.floor(min_E / 60) * 60 - 60)
top = max(200, np.ceil(max_E / 60) * 60 + 60)
ax.set_ylim(bottom=bottom, top=top)

y_start = int(np.floor(bottom / 200) * 200)
y_end   = int(np.ceil(top / 200) * 200)
ax.set_yticks(np.arange(y_start, y_end + 1, 200))

# ----------------------------
# Tick styling
# ----------------------------
ax.tick_params(axis="x", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="y", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="x", which="minor", direction="out", length=4, width=3)
ax.tick_params(axis="y", which="minor", direction="out", length=4, width=3)

for tick in ax.get_xticklabels():
    tick.set_fontweight("bold")
for tick in ax.get_yticklabels():
    tick.set_fontweight("bold")

ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

# ----------------------------
# Frame thickness
# ----------------------------
for spine in ax.spines.values():
    spine.set_linewidth(6)

# ----------------------------
# Legend (no box)
# ----------------------------
leg = ax.legend(loc="lower right", fontsize=24, frameon=False)
for text in leg.get_texts():
    text.set_fontweight("bold")

# ----------------------------
# Final layout
# ----------------------------
ax.grid(False)
plt.tight_layout()

# ----------------------------
# Save automatically
# ----------------------------
fig.savefig(out_png, dpi=600, bbox_inches="tight")
fig.savefig(out_svg, bbox_inches="tight")

plt.show()

# ----------------------------
# Download links in notebook
# ----------------------------
print("Download your saved figures:")
display(FileLink(out_png))
display(FileLink(out_svg))


# In[4]:


# ============================
# OCP vs Time — Single CSV Plotter for Local Notebook
# File expected in the same folder: SR400_Eocp.csv
# ============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from IPython.display import FileLink, display

# ----------------------------
# File names
# ----------------------------
csv_name = "SR400_Eocp.csv"
out_png = "SR400_Eocp_plot.png"
out_svg = "SR400_Eocp_plot.svg"

# ----------------------------
# Read CSV
# ----------------------------
df = pd.read_csv(csv_name)

# Clean column names
df.columns = [str(c).strip() for c in df.columns]

# Remove fully empty unnamed columns
df = df.loc[:, ~df.columns.str.contains(r"^Unnamed", case=False)]

# Clean column names again after filtering
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Actual columns in uploaded file
# ----------------------------
time_col = "Time(min)"
ocp_col  = "Potential ,E (mV)"

# Check required columns
if time_col not in df.columns or ocp_col not in df.columns:
    raise KeyError(
        f"Expected columns '{time_col}' and '{ocp_col}' not found.\n"
        f"Available columns: {df.columns.tolist()}"
    )

# Keep only needed columns
df = df[[time_col, ocp_col]].copy()
df.columns = ["time", "E"]

# ----------------------------
# Convert to numeric
# ----------------------------
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df["E"]    = pd.to_numeric(df["E"], errors="coerce")

# Drop invalid rows
df = df.dropna().reset_index(drop=True)

# Safety check
if df.empty:
    raise ValueError("No valid numeric data found after cleaning the CSV.")

# ----------------------------
# Distinct color palette
# ----------------------------
line_color = "#FF8C00"   # bright amber-orange

# ----------------------------
# Plot
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["time"],
    df["E"],
    linestyle="-",
    linewidth=4,
    color=line_color,
    label="SR400"
)

# ----------------------------
# Axis labels
# ----------------------------
ax.set_xlabel("Time (min)", fontsize=26, fontweight="bold")
ax.set_ylabel("OCP (mV)", fontsize=26, fontweight="bold")

# ----------------------------
# Axis limits and ticks
# ----------------------------
min_E = df["E"].min()
max_E = df["E"].max()

# X-axis
ax.set_xlim(0, 60)
ax.set_xticks(np.arange(0, 61, 20))

# Y-axis
bottom = min(-450, np.floor(min_E / 60) * 60 - 60)
top = max(200, np.ceil(max_E / 60) * 60 + 60)
ax.set_ylim(bottom=bottom, top=top)

# Y ticks every 200 mV
y_start = int(np.floor(bottom / 200) * 200)
y_end   = int(np.ceil(top / 200) * 200)
ax.set_yticks(np.arange(y_start, y_end + 1, 200))

# ----------------------------
# Tick styling
# ----------------------------
ax.tick_params(axis="x", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="y", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="x", which="minor", direction="out", length=4, width=3)
ax.tick_params(axis="y", which="minor", direction="out", length=4, width=3)

for tick in ax.get_xticklabels():
    tick.set_fontweight("bold")
for tick in ax.get_yticklabels():
    tick.set_fontweight("bold")

ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

# ----------------------------
# Frame thickness
# ----------------------------
for spine in ax.spines.values():
    spine.set_linewidth(6)

# ----------------------------
# Legend (no box)
# ----------------------------
leg = ax.legend(loc="lower right", fontsize=24, frameon=False)
for text in leg.get_texts():
    text.set_fontweight("bold")

# ----------------------------
# Final layout
# ----------------------------
ax.grid(False)
plt.tight_layout()

# ----------------------------
# Save automatically
# ----------------------------
fig.savefig(out_png, dpi=600, bbox_inches="tight")
fig.savefig(out_svg, bbox_inches="tight")

plt.show()

# ----------------------------
# Download links in notebook
# ----------------------------
print("Download your saved figures:")
display(FileLink(out_png))
display(FileLink(out_svg))


# In[9]:


# ============================
# OCP vs Time — Single CSV Plotter for Local Notebook
# File expected in the same folder: S450.csv
# ============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from IPython.display import FileLink, display

# ----------------------------
# File names
# ----------------------------
csv_name = "S450.csv"
out_png = "S450_OCP_plot.png"
out_svg = "S450_OCP_plot.svg"

# ----------------------------
# Read CSV
# ----------------------------
df = pd.read_csv(csv_name)

# Clean column names
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Actual columns in uploaded file
# ----------------------------
time_col = "time[min]"
ocp_col  = "E[mV]"

# Check required columns
if time_col not in df.columns or ocp_col not in df.columns:
    raise KeyError(
        f"Expected columns '{time_col}' and '{ocp_col}' not found.\n"
        f"Available columns: {df.columns.tolist()}"
    )

# Keep only needed columns
df = df[[time_col, ocp_col]].copy()
df.columns = ["time", "E"]

# Convert to numeric
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df["E"]    = pd.to_numeric(df["E"], errors="coerce")

# Drop invalid rows
df = df.dropna().reset_index(drop=True)

if df.empty:
    raise ValueError("No valid numeric data found after cleaning the CSV.")

# ----------------------------
# Bright distinct color palette
# ----------------------------
line_color = "#7CFC00"   # vivid lime green

# ----------------------------
# Plot
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["time"],
    df["E"],
    linestyle="-",
    linewidth=4,
    color=line_color,
    label="S450"
)

# ----------------------------
# Axis labels
# ----------------------------
ax.set_xlabel("Time (min)", fontsize=26, fontweight="bold")
ax.set_ylabel("OCP (mV)", fontsize=26, fontweight="bold")

# ----------------------------
# Axis limits and ticks
# ----------------------------
min_E = df["E"].min()
max_E = df["E"].max()

ax.set_xlim(0, 60)
ax.set_xticks(np.arange(0, 61, 20))

bottom = min(-450, np.floor(min_E / 60) * 60 - 60)
top = max(200, np.ceil(max_E / 60) * 60 + 60)
ax.set_ylim(bottom=bottom, top=top)

y_start = int(np.floor(bottom / 200) * 200)
y_end   = int(np.ceil(top / 200) * 200)
ax.set_yticks(np.arange(y_start, y_end + 1, 200))

# ----------------------------
# Tick styling
# ----------------------------
ax.tick_params(axis="x", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="y", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="x", which="minor", direction="out", length=4, width=3)
ax.tick_params(axis="y", which="minor", direction="out", length=4, width=3)

for tick in ax.get_xticklabels():
    tick.set_fontweight("bold")
for tick in ax.get_yticklabels():
    tick.set_fontweight("bold")

ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

# ----------------------------
# Frame thickness
# ----------------------------
for spine in ax.spines.values():
    spine.set_linewidth(6)

# ----------------------------
# Legend (no box)
# ----------------------------
leg = ax.legend(loc="lower right", fontsize=24, frameon=False)
for text in leg.get_texts():
    text.set_fontweight("bold")

# ----------------------------
# Final layout
# ----------------------------
ax.grid(False)
plt.tight_layout()

# ----------------------------
# Save automatically
# ----------------------------
fig.savefig(out_png, dpi=600, bbox_inches="tight")
fig.savefig(out_svg, bbox_inches="tight")

plt.show()

# ----------------------------
# Download links in notebook
# ----------------------------
print("Download your saved figures:")
display(FileLink(out_png))
display(FileLink(out_svg))


# In[10]:


# ============================
# OCP vs Time — Single CSV Plotter for Local Notebook
# File expected in the same folder: SR500_Eocp.csv
# ============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from IPython.display import FileLink, display

# ----------------------------
# File names
# ----------------------------
csv_name = "SR500_Eocp.csv"
out_png = "SR500_OCP_plot.png"
out_svg = "SR500_OCP_plot.svg"

# ----------------------------
# Read CSV
# ----------------------------
df = pd.read_csv(csv_name)

# Clean initial column names
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Handle CSV where true headers are in first row
# ----------------------------
if "time[min]" not in df.columns or "E[mV]" not in df.columns:
    first_row = df.iloc[0].astype(str).str.strip().tolist()
    if "time[min]" in first_row and "E[mV]" in first_row:
        df.columns = first_row
        df = df.iloc[1:].reset_index(drop=True)

# Clean column names again after possible reassignment
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Actual columns in uploaded file
# ----------------------------
time_col = "time[min]"
ocp_col  = "E[mV]"

# Check required columns
if time_col not in df.columns or ocp_col not in df.columns:
    raise KeyError(
        f"Expected columns '{time_col}' and '{ocp_col}' not found.\n"
        f"Available columns: {df.columns.tolist()}"
    )

# Keep only needed columns
df = df[[time_col, ocp_col]].copy()
df.columns = ["time", "E"]

# ----------------------------
# Convert to numeric
# ----------------------------
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df["E"]    = pd.to_numeric(df["E"], errors="coerce")

# Drop invalid rows
df = df.dropna().reset_index(drop=True)

if df.empty:
    raise ValueError("No valid numeric data found after cleaning the CSV.")

# ----------------------------
# Bright distinct color palette
# ----------------------------
line_color = "#2563EB"   # bright royal blue

# ----------------------------
# Plot
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["time"],
    df["E"],
    linestyle="-",
    linewidth=4,
    color=line_color,
    label="SR500"
)

# ----------------------------
# Axis labels
# ----------------------------
ax.set_xlabel("Time (min)", fontsize=26, fontweight="bold")
ax.set_ylabel("OCP (mV)", fontsize=26, fontweight="bold")

# ----------------------------
# Axis limits and ticks
# ----------------------------
min_E = df["E"].min()
max_E = df["E"].max()

ax.set_xlim(0, 60)
ax.set_xticks(np.arange(0, 61, 20))

bottom = min(-450, np.floor(min_E / 60) * 60 - 60)
top = max(200, np.ceil(max_E / 60) * 60 + 60)
ax.set_ylim(bottom=bottom, top=top)

y_start = int(np.floor(bottom / 200) * 200)
y_end   = int(np.ceil(top / 200) * 200)
ax.set_yticks(np.arange(y_start, y_end + 1, 200))

# ----------------------------
# Tick styling
# ----------------------------
ax.tick_params(axis="x", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="y", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="x", which="minor", direction="out", length=4, width=3)
ax.tick_params(axis="y", which="minor", direction="out", length=4, width=3)

for tick in ax.get_xticklabels():
    tick.set_fontweight("bold")
for tick in ax.get_yticklabels():
    tick.set_fontweight("bold")

ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

# ----------------------------
# Frame thickness
# ----------------------------
for spine in ax.spines.values():
    spine.set_linewidth(6)

# ----------------------------
# Legend (no box)
# ----------------------------
leg = ax.legend(loc="lower right", fontsize=24, frameon=False)
for text in leg.get_texts():
    text.set_fontweight("bold")

# ----------------------------
# Final layout
# ----------------------------
ax.grid(False)
plt.tight_layout()

# ----------------------------
# Save automatically
# ----------------------------
fig.savefig(out_png, dpi=600, bbox_inches="tight")
fig.savefig(out_svg, bbox_inches="tight")

plt.show()

# ----------------------------
# Download links in notebook
# ----------------------------
print("Download your saved figures:")
display(FileLink(out_png))
display(FileLink(out_svg))


# In[11]:


# ============================
# OCP vs Time — Single CSV Plotter for Local Notebook
# File expected in the same folder: SR550_Eocp.csv
# ============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from IPython.display import FileLink, display

# ----------------------------
# File names
# ----------------------------
csv_name = "SR550_Eocp.csv"
out_png = "SR550_OCP_plot.png"
out_svg = "SR550_OCP_plot.svg"

# ----------------------------
# Read CSV
# ----------------------------
df = pd.read_csv(csv_name)

# Clean initial column names
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Handle CSV where true headers are in first row
# ----------------------------
if "time[min]" not in df.columns or "E[mV]" not in df.columns:
    first_row = df.iloc[0].astype(str).str.strip().tolist()
    if "time[min]" in first_row and "E[mV]" in first_row:
        df.columns = first_row
        df = df.iloc[1:].reset_index(drop=True)

# Clean column names again after possible reassignment
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Actual columns in uploaded file
# ----------------------------
time_col = "time[min]"
ocp_col  = "E[mV]"

# Check required columns
if time_col not in df.columns or ocp_col not in df.columns:
    raise KeyError(
        f"Expected columns '{time_col}' and '{ocp_col}' not found.\n"
        f"Available columns: {df.columns.tolist()}"
    )

# Keep only needed columns
df = df[[time_col, ocp_col]].copy()
df.columns = ["time", "E"]

# ----------------------------
# Convert to numeric
# ----------------------------
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df["E"]    = pd.to_numeric(df["E"], errors="coerce")

# Drop invalid rows
df = df.dropna().reset_index(drop=True)

if df.empty:
    raise ValueError("No valid numeric data found after cleaning the CSV.")

# ----------------------------
# Bright distinct color palette
# ----------------------------
line_color = "#FF5A5F"   # bright coral red

# ----------------------------
# Plot
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["time"],
    df["E"],
    linestyle="-",
    linewidth=4,
    color=line_color,
    label="SR550"
)

# ----------------------------
# Axis labels
# ----------------------------
ax.set_xlabel("Time (min)", fontsize=26, fontweight="bold")
ax.set_ylabel("OCP (mV)", fontsize=26, fontweight="bold")

# ----------------------------
# Axis limits and ticks
# ----------------------------
min_E = df["E"].min()
max_E = df["E"].max()

ax.set_xlim(0, 60)
ax.set_xticks(np.arange(0, 61, 20))

bottom = min(-450, np.floor(min_E / 60) * 60 - 60)
top = max(200, np.ceil(max_E / 60) * 60 + 60)
ax.set_ylim(bottom=bottom, top=top)

y_start = int(np.floor(bottom / 200) * 200)
y_end   = int(np.ceil(top / 200) * 200)
ax.set_yticks(np.arange(y_start, y_end + 1, 200))

# ----------------------------
# Tick styling
# ----------------------------
ax.tick_params(axis="x", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="y", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="x", which="minor", direction="out", length=4, width=3)
ax.tick_params(axis="y", which="minor", direction="out", length=4, width=3)

for tick in ax.get_xticklabels():
    tick.set_fontweight("bold")
for tick in ax.get_yticklabels():
    tick.set_fontweight("bold")

ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

# ----------------------------
# Frame thickness
# ----------------------------
for spine in ax.spines.values():
    spine.set_linewidth(6)

# ----------------------------
# Legend (no box)
# ----------------------------
leg = ax.legend(loc="lower right", fontsize=24, frameon=False)
for text in leg.get_texts():
    text.set_fontweight("bold")

# ----------------------------
# Final layout
# ----------------------------
ax.grid(False)
plt.tight_layout()

# ----------------------------
# Save automatically
# ----------------------------
fig.savefig(out_png, dpi=600, bbox_inches="tight")
fig.savefig(out_svg, bbox_inches="tight")

plt.show()

# ----------------------------
# Download links in notebook
# ----------------------------
print("Download your saved figures:")
display(FileLink(out_png))
display(FileLink(out_svg))


# In[12]:


# ============================
# OCP vs Time — Single CSV Plotter for Local Notebook
# File expected in the same folder: SA1100_Eocp.csv
# ============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from IPython.display import FileLink, display

# ----------------------------
# File names
# ----------------------------
csv_name = "SA1100_Eocp.csv"
out_png = "SA1100_OCP_plot.png"
out_svg = "SA1100_OCP_plot.svg"

# ----------------------------
# Read CSV
# ----------------------------
df = pd.read_csv(csv_name)

# Clean initial column names
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Handle CSV where true headers are in first row
# ----------------------------
if "time[min]" not in df.columns or "E[mV]" not in df.columns:
    first_row = df.iloc[0].astype(str).str.strip().tolist()
    if "time[min]" in first_row and "E[mV]" in first_row:
        df.columns = first_row
        df = df.iloc[1:].reset_index(drop=True)

# Clean column names again after possible reassignment
df.columns = [str(c).strip() for c in df.columns]

# ----------------------------
# Actual columns in uploaded file
# ----------------------------
time_col = "time[min]"
ocp_col  = "E[mV]"

# Check required columns
if time_col not in df.columns or ocp_col not in df.columns:
    raise KeyError(
        f"Expected columns '{time_col}' and '{ocp_col}' not found.\n"
        f"Available columns: {df.columns.tolist()}"
    )

# Keep only needed columns
df = df[[time_col, ocp_col]].copy()
df.columns = ["time", "E"]

# ----------------------------
# Convert to numeric
# ----------------------------
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df["E"]    = pd.to_numeric(df["E"], errors="coerce")

# Drop invalid rows
df = df.dropna().reset_index(drop=True)

if df.empty:
    raise ValueError("No valid numeric data found after cleaning the CSV.")

# ----------------------------
# Bright distinct color palette
# ----------------------------
line_color = "#C026D3"   # bright orchid purple

# ----------------------------
# Plot
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["time"],
    df["E"],
    linestyle="-",
    linewidth=4,
    color=line_color,
    label="SA1100"
)

# ----------------------------
# Axis labels
# ----------------------------
ax.set_xlabel("Time (min)", fontsize=26, fontweight="bold")
ax.set_ylabel("OCP (mV)", fontsize=26, fontweight="bold")

# ----------------------------
# Axis limits and ticks
# ----------------------------
min_E = df["E"].min()
max_E = df["E"].max()

ax.set_xlim(0, 60)
ax.set_xticks(np.arange(0, 61, 20))

bottom = min(-450, np.floor(min_E / 60) * 60 - 60)
top = max(200, np.ceil(max_E / 60) * 60 + 60)
ax.set_ylim(bottom=bottom, top=top)

y_start = int(np.floor(bottom / 200) * 200)
y_end   = int(np.ceil(top / 200) * 200)
ax.set_yticks(np.arange(y_start, y_end + 1, 200))

# ----------------------------
# Tick styling
# ----------------------------
ax.tick_params(axis="x", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="y", which="major", labelsize=24, direction="out", length=8, width=6)
ax.tick_params(axis="x", which="minor", direction="out", length=4, width=3)
ax.tick_params(axis="y", which="minor", direction="out", length=4, width=3)

for tick in ax.get_xticklabels():
    tick.set_fontweight("bold")
for tick in ax.get_yticklabels():
    tick.set_fontweight("bold")

ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

# ----------------------------
# Frame thickness
# ----------------------------
for spine in ax.spines.values():
    spine.set_linewidth(6)

# ----------------------------
# Legend (no box)
# ----------------------------
leg = ax.legend(loc="lower right", fontsize=24, frameon=False)
for text in leg.get_texts():
    text.set_fontweight("bold")

# ----------------------------
# Final layout
# ----------------------------
ax.grid(False)
plt.tight_layout()

# ----------------------------
# Save automatically
# ----------------------------
fig.savefig(out_png, dpi=600, bbox_inches="tight")
fig.savefig(out_svg, bbox_inches="tight")

plt.show()

# ----------------------------
# Download links in notebook
# ----------------------------
print("Download your saved figures:")
display(FileLink(out_png))
display(FileLink(out_svg))


# In[ ]:




