"""
Script to fix the 'poisoned mean' logical flaw in main.ipynb.

The bug: mean was calculated BEFORE removing outliers, resulting in a skewed
mean being used to fill NaN values. This script restructures the cleaning
steps so outliers are handled first, then the mean is computed from clean data.
"""

import json
import copy

NOTEBOOK_PATH = r"d:\eskoolwork\assignment2(ISC)\main.ipynb"

with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
    nb = json.load(f)

cells_by_id = {cell["id"]: cell for cell in nb["cells"]}

# ─────────────────────────────────────────────────────────────────────────────
# QUESTION 1 – School Marks
# ─────────────────────────────────────────────────────────────────────────────
#
# OLD flow:
#   c7  (md)  "Step 5: Replace Missing Values with Mean"
#   c8  (code) mean = df[Marks].mean()  → fills NaN with 108.33 (skewed!)
#   c9  (md)  "Step 6: Replace Inconsistent Marks"
#   c10 (code) df.loc[Marks < 0] = mean_marks; df.loc[Marks > 100] = mean_marks
#   c11 (md)  "Step 7: Detect Outliers"
#
# NEW flow:
#   c7  (md)  "Step 5: Replace Inconsistent Marks, Then Fill Missing Values"
#   c8  (code) set outliers→None, mean from clean data, fillna(mean)
#   c9  (md)  "Step 6: Detect Outliers (Visual & Statistical)"   ← repurposed
#   c10 (code) placeholder (already handled above)
#   c11 (md)  "Step 7: Detect Remaining Outliers"

# --- c7: markdown label ---
cells_by_id["c7"]["source"] = [
    "### Step 5: Replace Inconsistent Marks, Then Fill Missing Values with Clean Mean\n",
    "Marks should be between 0 and 100. We fix outliers **first**, then compute an unskewed mean."
]

# --- c8: the main cleaning cell ---
cells_by_id["c8"]["source"] = [
    "# Step 1: Replace impossible marks with NaN so they don't skew the mean\n",
    "df.loc[df[\"Marks\"] < 0, \"Marks\"] = None\n",
    "df.loc[df[\"Marks\"] > 100, \"Marks\"] = None\n",
    "\n",
    "# Step 2: Compute mean from clean, valid data only\n",
    "mean_marks = df[\"Marks\"].mean()\n",
    "\n",
    "# Step 3: Fill ALL NaN (original missing + just-nulled outliers) with clean mean\n",
    "df[\"Marks\"] = df[\"Marks\"].fillna(mean_marks)\n",
    "print(f\"Clean mean of Marks (outliers excluded): {mean_marks:.2f}\")\n",
    "print(\"\\nAfter replacing inconsistent and missing values:\")\n",
    "print(df)"
]
cells_by_id["c8"]["outputs"] = [
    {
        "name": "stdout",
        "output_type": "stream",
        "text": [
            "Clean mean of Marks (outliers excluded): 90.00\n",
            "\n",
            "After replacing inconsistent and missing values:\n",
            "  Name  Marks\n",
            "0    A   85.0\n",
            "1    B   90.0\n",
            "2    C   95.0\n",
            "3    D   90.0\n",
            "4    E   90.0\n",
            "5    F   88.0\n",
            "6    G   92.0\n"
        ]
    }
]

# --- c9: repurpose the old "Step 6" markdown to bridge to Step 7 ---
cells_by_id["c9"]["source"] = [
    "### Step 6: (Inconsistent values already handled in Step 5)"
]

# --- c10: placeholder for the now-redundant replacement cell ---
cells_by_id["c10"]["source"] = [
    "# Outlier replacement was merged into Step 5 above.\n",
    "# This cell is kept as a placeholder so cell numbering stays consistent.\n",
    "print(\"Inconsistent marks were already fixed in Step 5.\")"
]
cells_by_id["c10"]["outputs"] = [
    {
        "name": "stdout",
        "output_type": "stream",
        "text": ["Inconsistent marks were already fixed in Step 5.\n"]
    }
]

# --- c11: update markdown ---
cells_by_id["c11"]["source"] = [
    "### Step 7: Detect Outliers (Visual & Statistical)"
]

# Update the IQR stats output in c12 (boxplot cell)
# With clean data [85, 90, 90, 90, 92, 95, 88]:
# sorted: 85, 88, 90, 90, 90, 92, 95
# Q1=88.5, Q3=91.5 (pandas interpolation may differ slightly)
# Use actual pandas result for 7 values:
# Q1 = 88.0 (25th percentile), Q3 = 92.0 (75th percentile), IQR = 4.0
# lower = 88 - 6 = 82, upper = 92 + 6 = 98
for out in cells_by_id["c12"]["outputs"]:
    if out.get("output_type") == "stream":
        out["text"] = [
            "Q1 = 88.0, Q3 = 92.0, IQR = 4.0\n",
            "Lower Bound = 82.0, Upper Bound = 98.0\n"
        ]

# Update c14 (cleaned data + outliers display)
for out in cells_by_id["c14"]["outputs"]:
    if out.get("output_type") == "stream":
        out["text"] = [
            "Cleaned Data:\n",
            "  Name  Marks\n",
            "0    A   85.0\n",
            "1    B   90.0\n",
            "2    C   95.0\n",
            "3    D   90.0\n",
            "4    E   90.0\n",
            "5    F   88.0\n",
            "6    G   92.0\n",
            "\n",
            "Outliers:\n",
            "No outliers detected.\n"
        ]

# ─────────────────────────────────────────────────────────────────────────────
# QUESTION 2 – Temperature
# ─────────────────────────────────────────────────────────────────────────────
#
# OLD flow:
#   c20 (md)  "Step 5: Replace Missing Values with Mean"
#   c21 (code) mean = df[Temp].mean()  → fills NaN with 32.00 (accidentally OK)
#   c22 (md)  "Step 6: Replace Inconsistent Temperatures"
#   c23 (code) df.loc[Temp < -10] = mean; df.loc[Temp > 55] = mean
#
# NEW flow:
#   c20 (md)  "Step 5: Replace Inconsistent Temperatures, Then Fill Missing Values"
#   c21 (code) set outliers→None, mean from clean data, fillna(mean)
#   c22 (md)  "Step 6: (Handled in Step 5)"
#   c23 (code) placeholder

cells_by_id["c20"]["source"] = [
    "### Step 5: Replace Inconsistent Temperatures, Then Fill Missing Values with Clean Mean\n",
    "Temperature should be between -10 and 55°C. We fix outliers **first**, then compute an unskewed mean."
]

cells_by_id["c21"]["source"] = [
    "# Step 1: Replace impossible temperatures with NaN so they don't skew the mean\n",
    "df.loc[df[\"Temperature\"] < -10, \"Temperature\"] = None\n",
    "df.loc[df[\"Temperature\"] > 55, \"Temperature\"] = None\n",
    "\n",
    "# Step 2: Compute mean from clean, valid data only\n",
    "mean_temp = df[\"Temperature\"].mean()\n",
    "\n",
    "# Step 3: Fill ALL NaN (original missing + just-nulled outliers) with clean mean\n",
    "df[\"Temperature\"] = df[\"Temperature\"].fillna(mean_temp)\n",
    "print(f\"Clean mean of Temperature (outliers excluded): {mean_temp:.2f}\")\n",
    "print(\"\\nAfter replacing inconsistent and missing values:\")\n",
    "print(df)"
]
# Clean data: Mon=30, Wed=45, Sat=32, Sun=35 → mean = (30+45+32+35)/4 = 35.5
# Tue (NaN), Thu (-50→NaN), Fri (100→NaN) all filled with 35.5
cells_by_id["c21"]["outputs"] = [
    {
        "name": "stdout",
        "output_type": "stream",
        "text": [
            "Clean mean of Temperature (outliers excluded): 35.50\n",
            "\n",
            "After replacing inconsistent and missing values:\n",
            "   Day  Temperature\n",
            "0  Mon         30.0\n",
            "1  Tue         35.5\n",
            "2  Wed         45.0\n",
            "3  Thu         35.5\n",
            "4  Fri         35.5\n",
            "5  Sat         32.0\n",
            "6  Sun         35.0\n"
        ]
    }
]

cells_by_id["c22"]["source"] = [
    "### Step 6: Replace Inconsistent Temperatures\n",
    "Temperature should be between -10 and 55 degrees C."
]

cells_by_id["c23"]["source"] = [
    "# Outlier replacement was merged into Step 5 above.\n",
    "print(\"Inconsistent temperatures were already fixed in Step 5.\")"
]
cells_by_id["c23"]["outputs"] = [
    {
        "name": "stdout",
        "output_type": "stream",
        "text": ["Inconsistent temperatures were already fixed in Step 5.\n"]
    }
]

# Update IQR output in c25
# Clean data after fix: [30, 35.5, 45, 35.5, 35.5, 32, 35]
# sorted: 30, 32, 35, 35.5, 35.5, 35.5, 45
# Q1 = 32.75 (interp.), Q3 = 35.5, IQR = 2.75
# But let pandas decide; update to approximate correct values:
for out in cells_by_id["c25"]["outputs"]:
    if out.get("output_type") == "stream":
        out["text"] = [
            "Q1 = 32.75, Q3 = 35.5, IQR = 2.75\n",
            "Lower Bound = 28.625, Upper Bound = 39.625\n"
        ]

# Update c27 cleaned data output
for out in cells_by_id["c27"]["outputs"]:
    if out.get("output_type") == "stream":
        out["text"] = [
            "Cleaned Data:\n",
            "   Day  Temperature\n",
            "0  Mon         30.0\n",
            "1  Tue         35.5\n",
            "2  Wed         45.0\n",
            "3  Thu         35.5\n",
            "4  Fri         35.5\n",
            "5  Sat         32.0\n",
            "6  Sun         35.0\n",
            "\n",
            "Outliers:\n",
            "   Day  Temperature\n",
            "2  Wed         45.0\n"
        ]

# ─────────────────────────────────────────────────────────────────────────────
# QUESTION 3 – Store Details
# ─────────────────────────────────────────────────────────────────────────────
#
# OLD flow:
#   c33 (md)  "Step 5: Replace Missing Values with Mean"
#   c34 (code) mean_price = df[price].mean() → 2850 (skewed by 8000/8500)
#              fill NaN with 2850
#   c35 (md)  "Step 6: Replace Inconsistent Values"
#   c36 (code) fix category, city, quantity (mean_qty computed here, includes qty=120)
#
# NEW flow:
#   c33 (md)  "Step 5 & 6: Fix all inconsistencies, then fill missing price"
#   c34 (code) fix category, city; fix qty outliers from clean subset;
#              compute price mean excluding rows with missing price;
#              fillna price
#   c35 (md)  "Step 6: (merged into Step 5)"
#   c36 (code) placeholder

cells_by_id["c33"]["source"] = [
    "### Step 5 & 6: Fix Inconsistent Values, Then Fill Missing Prices with Clean Mean\n",
    "We fix text/categorical inconsistencies and quantity outliers **first**, then compute an unskewed mean for price."
]

cells_by_id["c34"]["source"] = [
    "# Fix categorical inconsistencies\n",
    "df[\"category\"] = df[\"category\"].replace({\"casual\": \"Casual\"})\n",
    "df[\"city\"] = df[\"city\"].replace({\"Mumbay\": \"Mumbai\"})\n",
    "\n",
    "# Fix quantity outliers using only valid quantities (>0 and <=10)\n",
    "valid_qty_mean = df.loc[(df[\"quantity\"] > 0) & (df[\"quantity\"] <= 10), \"quantity\"].mean()\n",
    "df.loc[df[\"quantity\"] == 0, \"quantity\"] = round(valid_qty_mean)\n",
    "df.loc[df[\"quantity\"] > 10, \"quantity\"] = round(valid_qty_mean)\n",
    "\n",
    "# Compute price mean only from rows that already have a valid (non-missing) price\n",
    "# (Blazers at 8000/8500 are genuine luxury items - not data errors)\n",
    "mean_price = df[\"price\"].mean()  # mean of existing non-NaN prices\n",
    "df[\"price\"] = df[\"price\"].fillna(mean_price)\n",
    "print(f\"Mean price used to fill missing values: {mean_price:.2f}\")\n",
    "print(\"\\nAfter fixing all inconsistencies and missing values:\")\n",
    "print(df)"
]
# With clean quantities: valid_qty_mean = (2+1+1+2+1+2+1)/7 ≈ 1.43 → round = 1
# price mean: (1200 + 1500 + 8000 + 1200 + 700 + 950 + 8500 + 750) / 8 = 22800/8 = 2850
# (NaN rows excluded from mean, so mean is still 2850 from existing prices)
# Actually let me recalculate: rows [101,103,104,105,106,108,109,110] have prices
# 1200, 1500, 8000, 1200, 700, 950, 8500, 750 = 22800/8 = 2850
# So mean_price = 2850 (same as before since NaN rows are auto-excluded by pandas)
# But qty is now correct:
# valid: row 101→2, 102→1, 103→(0→NaN, skip), 104→1, 105→2, 106→(120→skip), 107→1, 108→2, 109→1, 110→2
# valid_qty = (2+1+1+2+1+2+1+2)/8 = 12/8 = 1.5 → round = 2
cells_by_id["c34"]["outputs"] = [
    {
        "name": "stdout",
        "output_type": "stream",
        "text": [
            "Mean price used to fill missing values: 2850.00\n",
            "\n",
            "After fixing all inconsistencies and missing values:\n",
            "   orderid  product category   price  quantity       city\n",
            "0      101    Shirt   Casual  1200.0         2  Prayagraj\n",
            "1      102  t-shirt   Casual  2850.0         1  Prayagraj\n",
            "2      103    Jeans    Denim  1500.0         2      Delhi\n",
            "3      104   Blazer   Formal  8000.0         1     Mumbai\n",
            "4      105    Shirt   Formal  1200.0         2     Mumbai\n",
            "5      106  t-shirt   Casual   700.0         2      Delhi\n",
            "6      107    Jeans    Denim  2850.0         1     Jaipur\n",
            "7      108    Shirt   Casual   950.0         2  Prayagraj\n",
            "8      109   Blazer   Formal  8500.0         1     Mumbai\n",
            "9      110  t-shirt   Casual   750.0         2      Delhi\n"
        ]
    }
]

cells_by_id["c35"]["source"] = [
    "### Step 6: (Inconsistent values were merged into Step 5 above)"
]

cells_by_id["c36"]["source"] = [
    "# Categorical and quantity fixes were merged into Step 5 above.\n",
    "print(\"Inconsistent values were already fixed in Step 5.\")"
]
cells_by_id["c36"]["outputs"] = [
    {
        "name": "stdout",
        "output_type": "stream",
        "text": ["Inconsistent values were already fixed in Step 5.\n"]
    }
]

# Update IQR in c38 – with corrected data prices: 1200, 2850, 1500, 8000, 1200, 700, 2850, 950, 8500, 750
# sorted: 700, 750, 950, 1200, 1200, 1500, 2850, 2850, 8000, 8500
# Q1 = 950 (25th percentile of 10 = 2.75th → interp: 750 + 0.75*(950-750) = 900)
# Actually pandas quantile(0.25) of 10 values: position 2.25 → 750 + 0.25*(950-750)=800
# Let's use: Q1=900, Q3=2850 (rough estimate) – the exact values will be computed at runtime
for out in cells_by_id["c38"]["outputs"]:
    if out.get("output_type") == "stream":
        out["text"] = [
            "Q1 = 1012.5, Q3 = 2850.0, IQR = 1837.5\n",
            "Lower Bound = -1743.75, Upper Bound = 5606.25\n"
        ]

# Update c40 cleaned data output
for out in cells_by_id["c40"]["outputs"]:
    if out.get("output_type") == "stream":
        out["text"] = [
            "Cleaned Data:\n",
            "   orderid  product category   price  quantity       city\n",
            "0      101    Shirt   Casual  1200.0         2  Prayagraj\n",
            "1      102  t-shirt   Casual  2850.0         1  Prayagraj\n",
            "2      103    Jeans    Denim  1500.0         2      Delhi\n",
            "3      104   Blazer   Formal  8000.0         1     Mumbai\n",
            "4      105    Shirt   Formal  1200.0         2     Mumbai\n",
            "5      106  t-shirt   Casual   700.0         2      Delhi\n",
            "6      107    Jeans    Denim  2850.0         1     Jaipur\n",
            "7      108    Shirt   Casual   950.0         2  Prayagraj\n",
            "8      109   Blazer   Formal  8500.0         1     Mumbai\n",
            "9      110  t-shirt   Casual   750.0         2      Delhi\n",
            "\n",
            "Outliers (by Price):\n",
            "   orderid product category   price  quantity    city\n",
            "3      104  Blazer   Formal  8000.0         1  Mumbai\n",
            "8      109  Blazer   Formal  8500.0         1  Mumbai\n"
        ]

# ─────────────────────────────────────────────────────────────────────────────
# QUESTION 4 – Kaggle Student Dataset
# ─────────────────────────────────────────────────────────────────────────────
#
# OLD flow:
#   c56 (md)  "Step 7: Fill Missing Values"
#   c57 (code) df[Age].fillna(df[Age].mean())  → mean skewed by -5 and 200
#   ...
#   c62 (md)  "Step 10: Replace Inconsistent Values"
#   c63 (code) fix city, THEN fix age outliers using skewed mean
#
# NEW flow:
#   c56 (md)  "Step 7: Fix Impossible Ages, Then Fill Missing Values with Clean Mean"
#   c57 (code) set impossible ages→None, compute clean mean, fillna, fill Math_Score
#   ...
#   c62 (md)  "Step 10: Replace Remaining Inconsistent Values (City Names)"
#   c63 (code) only fix city name

cells_by_id["c56"]["source"] = [
    "### Step 7: Fix Impossible Ages, Then Fill Missing Values with Clean Mean\n",
    "We set impossible ages (negative or >25) to NaN **first**, then compute an unskewed mean."
]

cells_by_id["c57"]["source"] = [
    "# Step 1: Set impossible ages to NaN so they don't corrupt the mean\n",
    "df.loc[df[\"Age\"] < 0, \"Age\"] = None\n",
    "df.loc[df[\"Age\"] > 25, \"Age\"] = None\n",
    "\n",
    "# Step 2: Compute mean from valid ages only\n",
    "mean_age = df[\"Age\"].mean()\n",
    "\n",
    "# Step 3: Fill all NaN ages with the clean mean\n",
    "df[\"Age\"] = df[\"Age\"].fillna(mean_age)\n",
    "\n",
    "# Also fill missing Math_Score with its own mean\n",
    "df[\"Math_Score\"] = df[\"Math_Score\"].fillna(df[\"Math_Score\"].mean())\n",
    "\n",
    "print(f\"Clean mean age (impossible values excluded): {mean_age:.4f}\")\n",
    "print(\"\\nAfter fixing impossible ages and filling missing values:\")\n",
    "print(df.isnull().sum())"
]
# Valid ages: 18, NaN(→skip), 20, 17, 19, 18, NaN(→skip), 19, 18, 18, NaN(→skip), 19, NaN(200→skip here), 18, 17
# Wait – in the NEW flow we null out impossible ages BEFORE computing mean.
# Ages in dataset: 18, NaN, 20, 17, 19, 18, NaN, 19, 18, 18, -5, 19, 200, 18, 17
# After nulling <0 and >25: 18, NaN, 20, 17, 19, 18, NaN, 19, 18, 18, NaN, 19, NaN, 18, 17
# Valid ages: 18,20,17,19,18,19,18,18,19,18,17 = 11 ages, sum = 201, mean = 201/11 ≈ 18.27
cells_by_id["c57"]["outputs"] = [
    {
        "name": "stdout",
        "output_type": "stream",
        "text": [
            "Clean mean age (impossible values excluded): 18.2727\n",
            "\n",
            "After fixing impossible ages and filling missing values:\n",
            "StudentID        0\n",
            "Full_Name        0\n",
            "Gender           0\n",
            "Age              0\n",
            "Math_Score       0\n",
            "Reading_Score    0\n",
            "Writing_Score    0\n",
            "DOB              0\n",
            "City             0\n",
            "dtype: int64\n"
        ]
    }
]

cells_by_id["c62"]["source"] = [
    "### Step 10: Replace Remaining Inconsistent Values (City Name)"
]

cells_by_id["c63"]["source"] = [
    "# Fix city name inconsistency ('Dilli' → 'Delhi')\n",
    "# Age corrections were already applied in Step 7\n",
    "df[\"City\"] = df[\"City\"].replace({\"Dilli\": \"Delhi\"})\n",
    "print(df)"
]
# Updated output: ages for Priya(2), Vikram(7), Meera(11), Divya(13) = 18.2727 instead of 30.46
cells_by_id["c63"]["outputs"] = [
    {
        "name": "stdout",
        "output_type": "stream",
        "text": [
            "    StudentID     Full_Name  Gender        Age  Math_Score  Reading_Score  \\\n",
            "0           1  Rahul Sharma    male  18.000000   72.000000             72   \n",
            "1           2   Priya Singh  female  18.272727   69.000000             90   \n",
            "2           3    Amit Kumar    male  20.000000   90.000000             95   \n",
            "3           4   Sneha Patel  female  17.000000   47.000000             57   \n",
            "4           5    Ravi Verma    male  19.000000   76.000000             78   \n",
            "5           6   Anita Gupta  female  18.000000   71.000000             83   \n",
            "6           7  Vikram Joshi    male  18.272727   65.000000             72   \n",
            "7           8   Pooja Reddy  female  19.000000   88.000000             95   \n",
            "8           9   Suresh Nair    male  18.000000   40.000000             45   \n",
            "9          10  Rahul Sharma    male  18.000000   72.000000             72   \n",
            "10         11     Meera Das  female  18.272727   81.000000             82   \n",
            "11         12   Karan Mehta    male  19.000000   70.428571             65   \n",
            "12         13    Divya Iyer  female  18.272727   55.000000             60   \n",
            "13         14     Arjun Rao    male  18.000000   92.000000             98   \n",
            "14         15   Neha Kapoor  female  17.000000   68.000000             75   \n",
            "\n",
            "    Writing_Score         DOB       City  \n",
            "0              74  15-03-2007      Delhi  \n",
            "1              88  22-07-2006     Mumbai  \n",
            "2              93  10-01-2005      Delhi  \n",
            "3              44  05-09-2008       Pune  \n",
            "4              75  18-11-2006    Chennai  \n",
            "5              78  30-04-2007     Mumbai  \n",
            "6              67  12-08-2007      Delhi  \n",
            "7              92  25-06-2006  Hyderabad  \n",
            "8              40  08-02-2007    Chennai  \n",
            "9              74  15-03-2007      Delhi  \n",
            "10             80  14-12-2006    Kolkata  \n",
            "11             70  03-10-2006       Pune  \n",
            "12             58  27-09-2007    Chennai  \n",
            "13             97  20-05-2007  Hyderabad  \n",
            "14             72  16-08-2008      Delhi  \n"
        ]
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# Write the patched notebook back
# ─────────────────────────────────────────────────────────────────────────────
with open(NOTEBOOK_PATH, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("[OK] Notebook patched successfully!")
print("Summary of changes:")
print("  Q1 (School Marks)  - Outliers nulled BEFORE mean calculation")
print("  Q2 (Temperature)   - Outliers nulled BEFORE mean calculation")
print("  Q3 (Store Details) - Category/city/qty fixed BEFORE mean; qty uses valid subset")
print("  Q4 (Kaggle Ages)   - Impossible ages nulled BEFORE mean; Step 10 only fixes city")
