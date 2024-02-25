import { Builder } from 'selenium-webdriver';
import chrome from 'selenium-webdriver/chrome.js';

import express from "express";

const app = express()
const port = 8080

app.get("/", async (req, res) => {
    console.log("Start the browser.")

    let chromeOptions = new chrome.Options();
    chromeOptions.addArguments('--headless', '--disable-gpu', '--no-sandbox');

    let driver = new Builder()
        .forBrowser('chrome')
        .setChromeOptions(chromeOptions)
        .build();

    console.log("Done!")

    console.log("Open Google.")
    await driver.get("https://google.com");
    console.log("Done!")

    const html = await driver.getPageSource();

    driver.quit();

    res.send(html)
})

app.get("/health", (req, res) => {
    res.send("OK")
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}.`)
})
