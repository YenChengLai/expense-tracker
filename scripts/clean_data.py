"""
Clean and Visualize Data
"""
import json
import pandas as pd

FILE_PATH: str = "expense.json"

"""
Read data fetched from Google Sheet record and clean it to generate dataframe
"""
def clean_and_transform_data(file_path: str) -> None:

    with open(file_path, "r", encoding="UTF-8") as f:
        data = json.load(f)

    df = pd.DataFrame(
        data, columns=["Date", "Amount / Cost", "Desc", "For Whom", "Category"]
    )

    # Data cleaning (adjust as needed)
    df["Amount / Cost"] = (
        df["Amount / Cost"]
        .astype(str)
        .str.replace("NT$", "")
        .str.replace(",", "")
        .str.strip()
    )
    df["Amount / Cost"] = pd.to_numeric(df["Amount / Cost"])
    # Categorize expenses/income
    df["Type"] = df["Amount / Cost"].apply(lambda x: "Income" if x < 0 else "Expense")
    df["Amount / Cost"] = abs(df["Amount / Cost"])

    # Data transformation
    df["Date"] = pd.to_datetime(df["Date"])  # Convert 'Date' column to datetime
    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year
    df["Day"] = df["Date"].dt.day
    df = df.drop("Date", axis=1)

    df.to_csv('cleaned_data.csv', index=False)


clean_and_transform_data(FILE_PATH)
