import { Given, Then, After } from '@cucumber/cucumber';
import { Builder, By, until } from 'selenium-webdriver';
import assert from 'assert';
import chrome from 'selenium-webdriver/chrome.js';

let driver;

let options = new chrome.Options();
options.addArguments('--headless');
options.addArguments('--no-sandbox');
options.addArguments('--disable-dev-shm-usage');
options.addArguments('--disable-gpu');
options.addArguments('--disable-extensions');
options.addArguments('--remote-debugging-port=9222');

Given('I am on the example.com page', async function () {
  driver = await new Builder().forBrowser('chrome').setChromeOptions(options).build();
  await driver.get('http://www.example.com');
});

Then('the page has loaded', async function () {
  // Wait for the h1 element to be loaded in the DOM
  let element = await driver.wait(until.elementLocated(By.css('h1')), 10000);
  let text = await element.getText();

  // Verify the h1 text is "Example Domain"
  assert.strictEqual(text, "Example Domain", 'The page did not load correctly.');
});

After(async function () {
  if (driver) {
    await driver.quit();
  }
});
