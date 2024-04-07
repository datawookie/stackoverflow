from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from behave import given, when, then


@given("I have a web browser")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")

    context.browser = webdriver.Chrome(options=chrome_options)


@when('I navigate to "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@then("I can see the Google search page")
def step_impl(context):
    assert "Google" in context.browser.title
    context.browser.quit()
