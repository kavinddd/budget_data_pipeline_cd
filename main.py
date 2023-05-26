import os
import requests
from google.cloud import bigquery

class Config:
    dataset_id = os.environ.get('dataset_id')
    table_name = os.environ.get('table_name')
    url = os.environ.get('url')

def get_data_api(url) -> dict:

    response = requests.get(url)
    result = response.json()

    return result

def main(event, context):

    client = bigquery.Client()
    dataset_ref = client.dataset(Config.dataset_id)

    raw = get_data(Config.url)
    record = [(
        raw['time']['updatedISO'],
        raw['bpi']['THB']['rate_float'],
        raw['bpi']['USD']['rate_float']
    )]

    table_ref = dataset_ref.table(Config.table_name)
    table = client.get_table(table_ref)
    result = client.insert_rows(table, record)
    return result
