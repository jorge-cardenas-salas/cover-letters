import requests
from behave import when, then


# from unittest import mock


@when('The following is posted to the "{endpoint_name}" endpoint')
def step_impl(context, endpoint_name):
    try:
        name = endpoint_name
        api_call = context.text
        requests.put(url=f"http://localhost:8000/{endpoint_name}", json=api_call)
        # requests.post(url=f"http://localhost:8000/{endpoint_name}", json=api_call)
    except Exception as ex:
        print(f"The horror!!! Exception:{str(ex)}")


@then("Dummy Success")
def step_impl(context):
    assert 1 == 1
