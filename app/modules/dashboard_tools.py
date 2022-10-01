import json
import os


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
        json.dump(visitors, open('app/data/visitors/uniq.json'))
        return False
    except:
        return False


def get_day_statistics() -> dict:
    """Function to get visits statistics by 24 hours"""

    ...


def get_month_statistics() -> dict:
    """Function to get visits statistics by 1 month"""

    ...
