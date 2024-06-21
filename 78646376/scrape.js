const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36');
  
  await page.goto('https://www.reddit.com/r/javascript/');
  
  await page.waitForSelector('h1');

  const data = await page.evaluate(() => {
    // Get all articles on page.
    //
    // ! Without pagination there will just be the top three articles.
    //
    const articles = Array.from(document.querySelectorAll('article'));
    // Extract content from each article.
    //
    // ! You can get some text but it's just a summary of the article, not full content.
    //
    const content = articles.map(article => {
        return {
            title: article.querySelector('a').innerText
        }
    });

    return content;
  });
  
  console.log(data);
  
  await browser.close();
})();