# -----------------------------------
# NIFTY 50 SECTOR ANALYSIS PROJECT
# -----------------------------------

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Nifty 50 tickers and sectors
tickers = [
    "ADANIPORTS.NS", "ASIANPAINT.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS",
    "BAJAJFINSV.NS", "BHARTIARTL.NS", "BPCL.NS", "BRITANNIA.NS", "CIPLA.NS",
    "COALINDIA.NS", "DIVISLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS",
    "HCLTECH.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS", "HINDALCO.NS",
    "HINDUNILVR.NS", "ICICIBANK.NS", "INDUSINDBK.NS", "INFY.NS", "ITC.NS",
    "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS", "M&M.NS", "MARUTI.NS",
    "NESTLEIND.NS", "NTPC.NS", "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS",
    "SBILIFE.NS", "SBIN.NS", "SHREECEM.NS", "SUNPHARMA.NS", "TATACONSUM.NS",
    "TATAMOTORS.NS", "TATASTEEL.NS", "TCS.NS", "TECHM.NS", "TITAN.NS",
    "ULTRACEMCO.NS", "UPL.NS", "WIPRO.NS"
]

sector_map = {
    "ADANIPORTS.NS": "Transport", "ASIANPAINT.NS": "Consumer", "AXISBANK.NS": "Financials",
    "BAJAJ-AUTO.NS": "Automobile", "BAJFINANCE.NS": "Financials", "BAJAJFINSV.NS": "Financials",
    "BHARTIARTL.NS": "Telecom", "BPCL.NS": "Energy", "BRITANNIA.NS": "Consumer", "CIPLA.NS": "Pharma",
    "COALINDIA.NS": "Energy", "DIVISLAB.NS": "Pharma", "DRREDDY.NS": "Pharma", "EICHERMOT.NS": "Automobile",
    "GRASIM.NS": "Materials", "HCLTECH.NS": "IT", "HDFCBANK.NS": "Financials", "HDFCLIFE.NS": "Financials",
    "HEROMOTOCO.NS": "Automobile", "HINDALCO.NS": "Metals", "HINDUNILVR.NS": "Consumer", "ICICIBANK.NS": "Financials",
    "INDUSINDBK.NS": "Financials", "INFY.NS": "IT", "ITC.NS": "Consumer", "JSWSTEEL.NS": "Metals",
    "KOTAKBANK.NS": "Financials", "LT.NS": "Construction", "M&M.NS": "Automobile", "MARUTI.NS": "Automobile",
    "NESTLEIND.NS": "Consumer", "NTPC.NS": "Energy", "ONGC.NS": "Energy", "POWERGRID.NS": "Energy",
    "RELIANCE.NS": "Energy", "SBILIFE.NS": "Financials", "SBIN.NS": "Financials", "SHREECEM.NS": "Materials",
    "SUNPHARMA.NS": "Pharma", "TATACONSUM.NS": "Consumer", "TATAMOTORS.NS": "Automobile", "TATASTEEL.NS": "Metals",
    "TCS.NS": "IT", "TECHM.NS": "IT", "TITAN.NS": "Consumer", "ULTRACEMCO.NS": "Materials",
    "UPL.NS": "Materials", "WIPRO.NS": "IT"
}

# Step 2: Download 1-year daily close prices
print("Downloading stock data... please wait...")
data_multi = yf.download(tickers, period="1y", auto_adjust=True)

# Step 3: Get only the 'Close' prices for all tickers
close_prices = data_multi["Close"]

# Step 4: Calculate 1-year returns
returns = (close_prices.iloc[-1] / close_prices.iloc[0] - 1) * 100
returns_df = returns.reset_index()
returns_df.columns = ["Ticker", "Return (%)"]

# Step 5: Add sectors
returns_df["Sector"] = returns_df["Ticker"].map(sector_map)

# Step 6: Group by sector for average performance
sector_perf = returns_df.groupby("Sector")["Return (%)"].mean().sort_values(ascending=False)

# Step 7: Save data to Excel
with pd.ExcelWriter("nifty_sector_returns.xlsx") as writer:
    returns_df.to_excel(writer, sheet_name="Stock Returns", index=False)
    sector_perf.to_excel(writer, sheet_name="Sector Performance")

print("\nData saved to nifty_sector_returns.xlsx")

# Step 8: Plot and save chart
plt.figure(figsize=(10,6))
sector_perf.plot(kind="bar", color="skyblue", edgecolor="black")
plt.ylabel("Average 1-Year Return (%)")
plt.title("Nifty Sector Performance - Last 1 Year")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("sector_chart.png")
print("Chart saved as sector_chart.png")

print("\n--- Top Performing Sectors ---")
print(sector_perf.head())

print("\n--- Bottom Performing Sectors ---")
print(sector_perf.tail())
