import { chromium } from 'playwright';

async function launchChrome() {
  // Launch a Chromium browser
  const browser = await chromium.launch({
    headless: false, // Set to false to see the browser UI
  });

  // Create a new page
  const page = await browser.newPage();

  // Navigate to a URL
  await page.goto('https://example.com');

  // The browser will stay open until manually closed
  // Uncomment the lines below to automatically close the browser after 30 seconds
  // setTimeout(async () => {
  //   await browser.close();
  // }, 30000);
}

launchChrome().catch(err => {
  console.error(err);
  process.exit(1);
});
