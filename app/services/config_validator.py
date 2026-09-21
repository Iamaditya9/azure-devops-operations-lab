import os

REQUIRED_VARS = ("APP_ENV", "AZURE_SUBSCRIPTION_ID", "AZURE_RESOURCE_GROUP")


def validate_environment(environ=None):
    source = environ if environ is not None else os.environ
    return {name: bool(source.get(name)) for name in REQUIRED_VARS}


def missing_variables(environ=None):
    result = validate_environment(environ)
    return [name for name, present in result.items() if not present]
