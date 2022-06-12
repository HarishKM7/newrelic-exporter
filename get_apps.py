#!/usr/bin/env python3
import requests, json

apps = []
params = { 'page': 1 }
APPS_URL = 'https://api.newrelic.com/v2/applications.json'
headers = { 'Api-Key': 'YOUR_API_KEY' }

while True:
    print(f'Getting apps page {params["page"]}...')
    response = requests.get(APPS_URL, headers = headers, params = params)
    applications = response.json()['applications']
    print(f'Got {len(applications)} apps')
    if not applications: break
    apps += applications
    params["page"] += 1

with open('applications.json', 'w') as apps_file:
    apps_file.write(json.dumps(apps))
