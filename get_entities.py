#!/usr/bin/env python3
import requests, json

entities = []
API_URL = 'https://api.newrelic.com/graphql'
headers = { 'Api-Key': 'YOUR_API_KEY' }

nextCursor = "null"
while True:
    print('Next cursor:', nextCursor)
    query = """
    {
      actor {
        entitySearch(queryBuilder: {domain: APM, type: APPLICATION}) {
          query
          results(cursor: NEXT_CURSOR) {
            nextCursor
            entities {
              accountId
              guid
              name
            }
          }
        }
      }
    }
    """.replace('NEXT_CURSOR', nextCursor)

    response = requests.post(API_URL, headers = headers, json = { 'query': query })
    results = response.json()['data']['actor']['entitySearch']['results']
    entities += results['entities']
    if not results['nextCursor']: break
    nextCursor = f"\"{results['nextCursor']}\""

with open('entities.json', 'w') as entities_file:
    entities_file.write(json.dumps(entities))
