import yfinance as yf
import pandas as pd

# List of Nifty 50 stock tickers
nifty_50_tickers = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "SBIN.NS", "BAJFINANCE.NS", "HDFC.NS", "BHARTIARTL.NS",
    # Add other tickers as needed
]

# Define a function to calculate pivot points and support/resistance levels
def calculate_pivot_levels(data):
    H = data['High'].iloc[-1]
    L = data['Low'].iloc[-1]
    C = data['Close'].iloc[-1]
    
    P = (H + L + C) / 3
    R1 = 2 * P - L
    S1 = 2 * P - H
    R2 = P + (H - L)
    S2 = P - (H - L)
    R3 = H + 2 * (P - L)
    S3 = L - 2 * (H - P)
    
    return P, R1, S1, R2, S2, R3, S3

# Dataframe to store pivot levels and CMP
pivot_df = pd.DataFrame(columns=[
    'Ticker', 'CMP', 'Pivot', 'R1', 'S1', 'R2', 'S2', 'R3', 'S3'
])

# Fetch data and calculate levels for each stock
for ticker in nifty_50_tickers:
    # Download the data for the past month with daily intervals
    data = yf.download(ticker, period="1mo", interval="1d")
    
    # Check if data is available
    if not data.empty:
        # Calculate pivot points and support/resistance levels
        P, R1, S1, R2, S2, R3, S3 = calculate_pivot_levels(data)
        
        # Fetch the current market price (CMP)
        ticker_info = yf.Ticker(ticker)
        CMP = ticker_info.history(period="1d")['Close'].iloc[-1]
        
        # Append the results to the DataFrame
        pivot_df = pivot_df.append({
            'Ticker': ticker,
            'CMP': CMP,
            'Pivot': P,
            'R1': R1,
            'S1': S1,
            'R2': R2,
            'S2': S2,
            'R3': R3,
            'S3': S3
        }, ignore_index=True)

# Display the pivot levels and CMP for Nifty 50 stocks
print(pivot_df)
