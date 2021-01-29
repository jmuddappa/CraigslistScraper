import os

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'minneapolis'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["hnp", "ram", "ank", "wsh", "dak", "csw"]


## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.

#CRAIGSLIST_HOUSING_SECTION = 'zip'

FURNITURE_QUERIES = [
    {"section": "zip", "query":"wood", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"wood*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"lumber", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"sink", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"sink*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"faucet*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"faucet", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"plywood", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"panel*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"panel", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"shower", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"window*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"window", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"door", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"pvc", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"cabinet*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"stool*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"table", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"table*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"chair*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"bed", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"heater", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"microwave", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"dishes", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"houseware", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"pan", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"pan*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"knives", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"cutlery", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"shelves", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"lamp*", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"light", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"lamp", "slack_channel":"#housing", "min_price": None, "max_price": 1},
    {"section": "zip", "query":"shelf", "slack_channel":"#housing", "min_price": None, "max_price": 1},
]

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 5 * 600 # 5 minutes


# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = YOUR_TOKEN


# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
