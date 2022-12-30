from flask import redirect


def page_not_found(e):
    """Function of 404 page"""

    return redirect('/not-found')
