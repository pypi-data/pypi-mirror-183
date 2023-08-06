"""This module contains various helper functions used by the e_dnevnik_api package."""

from functools import wraps
from .errors import AuthenticationError

def authentication_required(func):
    """Throw an AuthenticationError if the user is not authenticated."""
    @wraps(func)
    def check_authentication(*args, **kwargs):
        self = args[0]
        if not self.is_authenticated:
            raise AuthenticationError("you must be logged in to perform this action")
        return func(*args, **kwargs)
    return check_authentication
