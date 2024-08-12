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
├── scripts
|   └── fetch_data.py
├── init.sh
└── README.md
```
