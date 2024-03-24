import { chromium } from 'playwright';

async function launchChrome() {
  const browser = await chromium.launch({
    headless: true,
  });

  const page = await browser.newPage();

  await page.goto('https://example.com');

  const expectedTitle = 'Example Domain';
  const title = await page.title();

  console.log(`Page Title: ${title}`);
  if (title === expectedTitle) {
    console.log('The page was loaded successfully.');
  } else {
    console.error('The page did not load as expected.');
  }

  await browser.close();
}

launchChrome().catch(err => {
  console.error(err);
  process.exit(1);
});
