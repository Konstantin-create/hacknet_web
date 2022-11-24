import difflib


def _similarity(string1, string2):
    normalized1 = string1.lower()
    normalized2 = string2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()


def approximate_search(header: str, posts: list) -> list:
    """Function for approximate search of similar headers in posts from db"""

    compares = {}
    for post in posts:
        difference = _similarity(header, post.header)
        if len(compares.keys()) <= 10 or (difference >= .6 and len(compares.keys()) > 10):
            compares[post.id] = [difference, post]

    value = [el[1] for el in sorted(compares.values(), key=lambda x: x[0])]
    return value
