// Import dependencies from Playwright
import { chromium } from 'playwright';

async function runBrowserTest() {
  // Launch a Chromium browser instance
  const browser = await chromium.launch({
    headless: false // Set to false to see the browser UI
  });

  // Create a new browser page
  const page = await browser.newPage();

  // Navigate to a webpage
  await page.goto('https://example.com');

  // Get the page title and log it
  const title = await page.title();
  console.log(`The page title is: ${title}`);

  // Close the browser
  await browser.close();
}

// Execute the function
runBrowserTest().catch((err) => {
  console.error(err);
  process.exit(1);
});
