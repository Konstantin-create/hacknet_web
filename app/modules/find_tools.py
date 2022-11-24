import Levenshtein


def approximate_search(header: str, posts: list) -> list:
    """Function for approximate search of similar headers in posts from db"""

    compares = {}
    for post in posts:
        difference = Levenshtein.distance(header, post.header)
        # if difference <= len(header) // 2:
        compares[post.id] = [difference, post]

    value = [el[1] for el in sorted(compares.values(), key=lambda x: x[0])]
    print()
    print(value)
    print()
    return value
