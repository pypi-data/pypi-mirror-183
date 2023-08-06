"""
Settings for Linets with 99MINUTOS courier are all namespaced in the LINETS setting.
For example your project's `settings.py` file might look like this:

DJANGO_99MINUTOS = {
    'XCIXMINUTOS': {
        'BASE_URL': '<99MINUTOS_BASE_URL>',
        'CLIENT_ID': '<99MINUTOS_CLIENT_ID>',
        'CLIENT_SECRET': '<99MINUTOS_CLIENT_SECRET>',
        'DELIVERY_TYPE': '<99MINUTOS_DELIVERY_TYPE>',
        'TOKEN': '<99MINUTOS_TOKEN>',
    },
    'SENDER': {
        'FIRST_NAME': '<99MINUTOS_FIRST_NAME>',
        'LAST_NAME': '<99MINUTOS_LAST_NAME>',
        'PHONE': '<99MINUTOS_PHONE>',
        'EMAIL': '<99MINUTOS_EMAIL>',
        'ADDRESS': '<99MINUTOS_ADDRESS>',
        'COUNTRY_CODE': '<99MINUTOS_COUNTRY_CODE>',
        'REFERENCE': '<99MINUTOS_REFERENCE>',
        'ZIPCODE': '<99MINUTOS_ZIPCODE>',
        'COUNTRY_NAME': '<99MINUTOS_COUNTRY_NAME>'
    }
}

This module provides the `api_setting` object, that is used to access
Linets settings, checking for user settings first, then falling
back to the defaults.
"""
from django.conf import settings
from django.test.signals import setting_changed
from django.utils.module_loading import import_string


DEFAULTS = {
    'XCIXMINUTOS': {
        'BASE_URL': '<99MINUTOS_BASE_URL>',
        'CLIENT_ID': '<99MINUTOS_CLIENT_ID>',
        'CLIENT_SECRET': '<99MINUTOS_CLIENT_SECRET>',
        'DELIVERY_TYPE': '<99MINUTOS_DELIVERY_TYPE>',
        'TOKEN': '<99MINUTOS_TOKEN>',
    },
    'SENDER': {
        'FIRST_NAME': '<99MINUTOS_FIRST_NAME>',
        'LAST_NAME': '<99MINUTOS_LAST_NAME>',
        'PHONE': '<99MINUTOS_PHONE>',
        'EMAIL': '<99MINUTOS_EMAIL>',
        'ADDRESS': '<99MINUTOS_ADDRESS>',
        'COUNTRY_CODE': '<99MINUTOS_COUNTRY_CODE>',
        'REFERENCE': '<99MINUTOS_REFERENCE>',
        'ZIPCODE': '<99MINUTOS_ZIPCODE>',
        'COUNTRY_NAME': '<99MINUTOS_COUNTRY_NAME>'
    }
}


# List of settings that may be in string import notation.
IMPORT_STRINGS = [
    'XCIXMINUTOS',
    'SENDER',
]


def perform_import(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    if val is None:
        return None
    elif isinstance(val, str):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    try:
        return import_string(val)
    except ImportError as e:
        msg = "Could not import '%s' for API setting '%s'. %s: %s." % (val, setting_name, e.__class__.__name__, e)
        raise ImportError(msg)


class APISettings:
    """
    A settings object that allows Linets settings to be accessed as
    properties. For example:

        from XCIXminutos.settings import api_settings
        print(api_settings.DJANGO_99MINUTOS)

    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.

    Note:
    This is an internal class that is only compatible with settings namespaced
    under the LINETS name. It is not intended to be used by 3rd-party
    apps, and test helpers like `override_settings` may not work as expected.
    """
    def __init__(self, user_settings=None, defaults=None, import_strings=None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS
        self.import_strings = import_strings or IMPORT_STRINGS
        self._cached_attrs = set()

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'DJANGO_99MINUTOS', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Coerce import strings into classes
        if attr in self.import_strings:
            val = perform_import(val, attr)

        # Cache the result
        self._cached_attrs.add(attr)
        setattr(self, attr, val)
        return val

    def __check_user_settings(self, user_settings):
        return user_settings

    def reload(self):
        for attr in self._cached_attrs:
            delattr(self, attr)
        self._cached_attrs.clear()
        if hasattr(self, '_user_settings'):
            delattr(self, '_user_settings')


api_settings = APISettings(None, DEFAULTS, IMPORT_STRINGS)


def reload_api_settings(*args, **kwargs):
    setting = kwargs['setting']
    if setting == 'DJANGO_99MINUTOS':
        api_settings.reload()


setting_changed.connect(reload_api_settings)
