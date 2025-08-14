# Nifty 50 Sector Analysis

This project calculates the 1-year returns of Nifty 50 companies, groups them by sector, and shows the top and bottom performing sectors.

## Features
- Downloads stock data using **yfinance**
- Calculates 1-year % returns for each stock
- Groups by sector and finds average returns
- Saves results to CSV
- Creates a bar chart of sector performance

## Files
- `main.py` – Python code for the project
- `stock_returns.csv` – 1-year returns for each stock
- `sector_performance.csv` – Average return per sector
- `sector_chart.png` – Visual bar chart

## How to Run
1. Install the required packages:
   ```bash
   pip install yfinance pandas matplotlib
