#!/usr/bin/env python3
import requests, json
from datetime import datetime

MARCH_EPOCH = 1646073000 # March 1, 2022
LATEST_EPOCH = datetime.now().timestamp() - 86400 # 1 day ago

API_URL = 'https://api.newrelic.com/graphql'
headers = { 'Api-Key': 'YOUR_API_KEY' }

query = """
  {
    actor {
      account(id: ACCOUNT_ID) {
        nrql(query: "NRQL_QUERY") {
          results
        }
      }
    }
  }
"""

def get_metrics(app, metric, nrql_query):
    metrics = []
    app_name = app['name']
    account_id = app['accountId']
    since_epoch = MARCH_EPOCH

    while True:
        since_datetime = datetime.fromtimestamp(since_epoch)
        print(f'Querying since {since_datetime}...')

        new_nrql_query = nrql_query.replace('SINCE_EPOCH', str(since_epoch))
        new_query = query \
            .replace('ACCOUNT_ID', str(account_id)) \
            .replace('NRQL_QUERY', new_nrql_query)

        response = requests.post(API_URL, headers = headers, json = { 'query': new_query })
        results = response.json()['data']['actor']['account']['nrql']['results']

        if not results: break
        metrics += results
        since_epoch = results[-1]['endTimeSeconds'] + 1
        if since_epoch > LATEST_EPOCH: break

    with open(f'metrics/{app_name}/{metric}.json', 'w') as metrics_file:
        metrics_file.write(json.dumps(metrics, indent=2))
