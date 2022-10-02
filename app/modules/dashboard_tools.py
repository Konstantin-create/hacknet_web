import os
import json
from datetime import datetime


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
        json.dump(visitors, open('app/data/visits/uniq.json', 'w'))
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
        json.dump(requests, open('app/data/visits/requests.json', 'w'))
        return False
    except:
        return False


def get_day_requests_statistics() -> dict:
    """Function to get requests statistics by 24 hours"""

    pass


def get_month_requests_statistics() -> list:
    """Function to get requests statistics by 1 month"""

    pass
