import pandas as pd
import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials


load_dotenv()  # Load environment variables from .env file


def export(file_name: str, data: str) -> None:
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))


def get_google_sheet_data(spreadsheet_id, sheet_name):
    """Fetches data from a Google Sheet using service account authentication."""

    # Load credentials from environment variable
    creds = Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    )
    service = build("sheets", "v4", credentials=creds)

    # Construct the range
    range_name = f"{sheet_name}!A1:E"

    try:
        # Make a request to retrieve data from the Google Sheets API
        response = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=range_name)
            .execute()
        )

        # Parse the JSON response
        data = response.get("values", [])
        if not data:
            return None

        export(file_name="expense.json", data=data)

        # Convert to Pandas DataFrame
        df = pd.DataFrame(data[1:], columns=data[0])
        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


spreadsheet_id = "SPREAD_SHEET_ID"
sheet_name = "202407 Dad's Spending"

sheet_data = get_google_sheet_data(spreadsheet_id, sheet_name)

if sheet_data is not None:
    print(sheet_data)
else:
    print("Failed to fetch data from Google Sheets API.")
