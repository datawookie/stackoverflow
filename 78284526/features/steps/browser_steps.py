from behave import given, when, then


@given("I have a web browser")
def step_impl(context):
    pass


@when('I navigate to "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@then("I can see the Google search page")
def step_impl(context):
    assert "Google" in context.driver.title
    context.driver.quit()
