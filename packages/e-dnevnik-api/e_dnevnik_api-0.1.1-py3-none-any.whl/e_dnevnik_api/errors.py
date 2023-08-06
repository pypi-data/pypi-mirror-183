"""This module contains the base exception classes for the e_dnevnik_api package."""

class EDnevnikException(Exception):
    """Base e-Dnevnik exception."""
    pass

class AuthenticationError(EDnevnikException):
    """Authentication error."""
    pass
