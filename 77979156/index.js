const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  console.log(`Browser Executable Path: ${puppeteer.executablePath()}`);

  const page = await browser.newPage();

  const response = await page.goto('https://example.com');

  console.log(`Status Code: ${response.status()}`);

  await browser.close();
})();
