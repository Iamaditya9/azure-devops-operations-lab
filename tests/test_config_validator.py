from app.services.config_validator import missing_variables, validate_environment


def test_all_required_variables_are_detected():
    env = {
        "APP_ENV": "dev",
        "AZURE_SUBSCRIPTION_ID": "subscription",
        "AZURE_RESOURCE_GROUP": "rg-demo",
    }
    assert missing_variables(env) == []
    assert all(validate_environment(env).values())


def test_missing_variables_are_reported():
    env = {"APP_ENV": "dev"}
    assert set(missing_variables(env)) == {
        "AZURE_SUBSCRIPTION_ID",
        "AZURE_RESOURCE_GROUP",
    }
