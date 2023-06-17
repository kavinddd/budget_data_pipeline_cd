# Budget Data Pipeline with CD
A part of practicing using Github Actions deploy a function on Google Cloud Functions to create a cheap and simple data pipeline.

## Requirements
- Create a service account with Cloud Function Admin Role from the service provider allowing Github Action to work with cloud services. (In this case, GCP)
  - Get a key from and encode it with base64.
  - Put a encoded key in Github SECRET. (GCP_CREDENTIAL_KEY: <GCP_CREDENTIAL_KEY>)
- Setting another Github SECRET (GCP_PROJ_NAME: <project_id>)
- Manually create a Cloud PUB/SUB and Cloud scheduler to automate triggering the function. (Every 5 minutes in this case)
- Manually create a table in BigQuery to store a result.

## What does it do exactly?
- A [main](main.py) function call an API to get BTC price and insert it in a bigquery.
- Cloud scheduler will send a message to Cloud PUB/SUB every 5 mins
  - Each time Cloud PUB/SUB get a message, the [main](main.py) function is triggered.
- Everytime there is a commit pushed to this repo, it deploys on Google Cloud Function automatically with Github Actions
  - Packages in requirements.txt will be installed in the environment.
  - Environment variables will be created from [env.yaml](env/env.yaml) which will be used to run a main function.
    - Github SECRET is used for building Github Actions [workflow](.github/workflows/main.yaml)

## Benefits
- A lot cheaper than using Google Cloud Composer.

## Limitations
- This works well only simple data pipelines. (In this case was just retrieving data from API then insert into table)
  - Any data pipelines need dependencies, using orchestration like airflow would still be a better choice.
 
## Result
[Google Sheet](https://docs.google.com/spreadsheets/d/1muJ2vsvR46GNZYG3vVnV8JeiY9rGbfjqQXDjHdkv-GE/edit?usp=sharing)
- The link will be valid until my GCP free trial run out.
