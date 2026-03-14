"""
generate_data.py
================
Script to generate synthetic, realistic sales data.
Run ONCE before launching the dashboard:
    $ python generate_data.py
"""

import pandas as pd
import numpy as np
from datetime import date

# ── General configuration ─────────────────────────────────────────────────────
SEED = 42
np.random.seed(SEED)

START_DATE = "2024-01-01"
END_DATE   = "2024-12-31"
N_ROWS     = 1_200          # orders during the year

# ── Catalogs ──────────────────────────────────────────────────────────────────
PRODUCTS = {
    # name:  (base_price_usd, cost_ratio)
    "CRM Software":       (1_200, 0.30),
    "IT Consulting":      (3_500, 0.55),
    "Premium Support":    (  450, 0.20),
    "Analytics License":  (  800, 0.35),
    "Training":           (  600, 0.40),
    "Hardware Pack":      (2_200, 0.65),
}

REGIONS = {
    # region: relative sales weight
    "LATAM":          0.35,
    "North America":  0.30,
    "Europe":         0.20,
    "Asia-Pacific":   0.10,
    "Middle East":    0.05,
}

# ── Date generation with seasonality ─────────────────────────────────────────
def seasonal_weights(dates: pd.DatetimeIndex) -> np.ndarray:
    """Higher sales in Q4 (Oct-Dec) and Q2 (Apr-Jun)."""
    month = dates.month
    base  = np.ones(len(dates))
    base  = np.where(month.isin([10, 11, 12]), base * 2.0, base)   # Q4 peak
    base  = np.where(month.isin([ 4,  5,  6]), base * 1.4, base)   # Q2 bump
    base  = np.where(month.isin([ 1,  2     ]), base * 0.7, base)  # slow January
    return base / base.sum()

date_range = pd.date_range(START_DATE, END_DATE)
weights    = seasonal_weights(date_range)
dates      = np.random.choice(date_range, size=N_ROWS, p=weights)

# ── DataFrame assembly ────────────────────────────────────────────────────────
product_names = list(PRODUCTS.keys())
region_names  = list(REGIONS.keys())
region_probs  = list(REGIONS.values())

chosen_products = np.random.choice(product_names, size=N_ROWS)
chosen_regions  = np.random.choice(region_names,  size=N_ROWS, p=region_probs)

rows = []
for i in range(N_ROWS):
    product = chosen_products[i]
    base_price, cost_ratio = PRODUCTS[product]

    # Units sold (1–5, biased toward 1)
    units  = int(np.random.choice([1, 2, 3, 4, 5], p=[0.55, 0.25, 0.10, 0.06, 0.04]))

    # Price with ±15% variation
    factor = np.random.uniform(0.85, 1.15)
    price  = round(base_price * factor, 2)
    sales  = round(price * units, 2)
    cost   = round(sales * cost_ratio * np.random.uniform(0.90, 1.10), 2)

    rows.append({
        "Fecha":      pd.Timestamp(dates[i]).date(),
        "Producto":   product,
        "Región":     chosen_regions[i],
        "Ventas_USD": sales,
        "Unidades":   units,
        "Costo_USD":  cost,
    })

df = pd.DataFrame(rows).sort_values("Fecha").reset_index(drop=True)

# ── Export ────────────────────────────────────────────────────────────────────
output_path = "ventas_demo.csv"
df.to_csv(output_path, index=False)

print(f"✅ File '{output_path}' generated with {len(df):,} rows.")
print(df.head())
print("\nSummary:")
print(f"  Total revenue : ${df['Ventas_USD'].sum():,.0f}")
print(f"  Net profit    : ${(df['Ventas_USD'] - df['Costo_USD']).sum():,.0f}")
print(f"  Orders        : {len(df):,}")