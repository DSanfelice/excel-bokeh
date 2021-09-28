import pandas as pd
import json
import csv
from google.oauth2 import service_account
import pygsheets

#Authenticating To A Google Cloud Project With A .JSON Service Account Key
with open('service_account.json') as source:
    info = json.load(source)
credentials = service_account.Credentials.from_service_account_info(info)

#Authenticating With Google Sheets With Pyghseets
client = pygsheets.authorize(service_account_file='service_account.json')

#connect to a specific google sheet
spreadsheet_url = "insert url"