# Expense Tracker

Monthly triggered tools fetching family expense records from google sheet and generate visualizations

## Setting up the environment

1. Make sure the `init.sh` file is executable:

    ```.sh
    sudo chmod +x init.sh
    ```

2. Go to the project folder in command line and run the below command:

    ```.sh
    source ./init.sh
    ```

3. Set up credentials to get access to google sheets

    ```.txt
    GOOGLE_APPLICATION_CREDENTIALS={PATH_TO_CREDENTIAL_JSON_FILE}
    ```

## Project Structure

``` text
/expense-tracker
├── .cmds
│   ├── requirements.txt
│   └── setup.sh
├── resources
|   └── kaiu.ttf
├── scripts
|   ├── clean_data.py
|   ├── fetch_data.py
|   └── visualize_data.py
├── init.sh
└── README.md
```

## Workflow

1. Fetch data from google sheet and generate `expense.json` file as result.

```.sh
python scripts/fetch_data.py
```

2. Clean fetched data, create dataframe, and store it as `cleaned_data.csv`

```.sh
python scripts/clean_data.py
```

3. Generate visualization result using `streamlit` based on the cleaned data.

```.sh
streamlit run scripts/visualize_data.py
```
