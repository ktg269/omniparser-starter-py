# ominiparser/stock_prices_parser.py

import os
import statistics

import pandas

def calculate_latest_closing_price_from_json():
   rows = df.to_dict("closing price")

    latest_closing_price = [r["close"] for r in rows] #>

    avg_grade = statistics.mean(grades)

    return avg_grade #90.64 #"OOPS" 

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    aapl_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_aapl.json")
    goog_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_goog.json")
    msft_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_msft.json")

    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)



print("PARSING SOME STOCK PRICES HERE...")
