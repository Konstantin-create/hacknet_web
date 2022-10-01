import json
import os


def request_handler() -> None:
    """Function to get user request and save this in local storage"""

    pass


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
        json.dump(visitors, open('app/data/visits/uniq.json'))
        return False
    except:
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

    pass


def add_request_to_list(request: dict) -> bool:
    """Function to add request to local storage"""

    pass


def get_day_requests_statistics() -> dict:
    """Function to get requests statistics by 24 hours"""

    pass


def get_month_requests_statistics() -> list:
    """Function to get requests statistics by 1 month"""

    pass
