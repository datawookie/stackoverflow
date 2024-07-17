import puppeteer from 'puppeteer';

async function fetchData() {
  try {
    const url = 'https://lookerstudio.google.com/u/0/reporting/e36054dd-ffc0-4ef4-b8ab-4d10f7ab4cda/page/wmP0D';
    const options = {
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-accelerated-2d-canvas',
        '--no-first-run',
        '--no-zygote',
        '--single-process',
        '--disable-gpu'
      ],
      // Show the browser window.
      headless: false
    };
    const browser = await puppeteer.launch(options);
    const page = await browser.newPage();

    await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36');
    await page.setViewport({width: 1920, height: 1080});
    await page.setRequestInterception(true);
    page.on('request', (req) => {
      if (req.resourceType() === 'stylesheet' || req.resourceType() === 'font' || req.resourceType() === 'image') {
        req.abort();
      } else {
        req.continue();
      }
    });

    // Use networkidle2 rather than networkidle0.
    await page.goto(url, {waitUntil: 'networkidle2'});

    await page.waitForSelector('.table', { timeout: 60000 });

    const text = await page.evaluate(() => {
      return document.body.innerText;
    });

    console.log(text);

    await page.close();
    await browser.close();
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

fetchData();
