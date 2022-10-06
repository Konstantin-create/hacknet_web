import os
import json
from collections import Counter
from datetime import datetime, timedelta


def request_handler(ip: str, url: str) -> None:
    """Function to get user request and save this in local storage"""

    request = {'ip': ip, 'time_stamp': datetime.utcnow().strftime("%Y:%m:%d-%H:%M:%S"), 'url': url}
    print(request)
    add_request_to_list(request)


# Uniq visitors
def get_visitors_list() -> list:
    """Function to get visitors list from local file"""

    if os.path.exists('app/data/visits/uniq.json'):
        try:
            return json.load(open('app/data/visits/uniq.json', 'r'))
        except:
            return []
    return []


def add_visitor_to_list(visitor: dict) -> bool:
    """Function to add visitor to list in local file"""

    visitors = get_visitors_list()
    visitors.append(visitor)
    try:
        json.dump(visitors, open('app/data/visits/uniq.json', 'w'), indent=4)
        return False
    except Exception as e:
        return False


def get_day_users_statistics() -> list:
    """Function to get visits statistics by 24 hours"""

    pass


def get_month_users_statistics() -> list:
    """Function to get visits statistics by 1 month"""

    pass


# Requests
def get_requests_list() -> list:
    """Function to get list of requests"""

    if os.path.exists('app/data/visits/requests.json'):
        try:
            return json.load(open('app/data/visits/requests.json', 'r'))
        except Exception as e:
            return []
    return []


def add_request_to_list(request: dict) -> bool:
    """Function to add request to local storage"""

    requests = get_requests_list()
    requests.append(request)
    try:
        json.dump(requests, open('app/data/visits/requests.json', 'w'), indent=4)
        return False
    except:
        return False


def generate_requests_data() -> dict:
    """Function to generate requests data from local storage"""

    data_src = get_requests_list()
    data = []
    out = {'requests': {'total': 0, 'per_day': 0, 'per_month': 0}}
    for el in data_src:
        time_stamp = datetime.strptime(el['time_stamp'], '%Y:%m:%d-%H:%M:%S')
        time_delta = (datetime.utcnow() - time_stamp)
        if time_delta <= timedelta(hours=24):
            out['requests']['per_day'] += 1
        elif time_delta <= timedelta(days=31):
            out['requests']['per_month'] += 1
        out['requests']['total'] += 1

    return out


def generate_pages_data() -> list:
    """Function to generate the most visitable pages data"""

    data_src = get_requests_list()
    _data = dict(Counter([el['url'] for el in data_src]))
    total = 5 if 5 < len(_data) else len(_data)
    out = []
    for i in range(total):
        out.append([list(_data.keys())[i], _data[list(_data.keys())[i]]])

    return out

