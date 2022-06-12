#!/usr/bin/env python3
import json, os, time
from get_metrics import get_metrics

entities = []
with open('entities.json', 'r') as entities_file:
    entities = json.loads(entities_file.read())

def get_metrics_wrapper(metric, query):
    for entity in entities:
        if os.path.isfile(f'metrics/{entity["name"]}/{metric}.json'):
            print(f'Skipping app {entities.index(entity)+1} of {len(entities)}: {entity["name"]}')
            continue

        print(f'Querying app {entities.index(entity)+1} of {len(entities)}: {entity["name"]}')

        retry = True
        retry_count = 5

        while retry and retry_count > 0:
            try:
                get_metrics(entity, metric, query.replace('ENTITY_GUID', entity['guid']))
                retry = False
            except TypeError:
                print('Error occurred. Retrying...')
                retry_count -= 1
                time.sleep(5)
                retry = True
