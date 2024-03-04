using System;
using System.Threading.Tasks;
using PuppeteerSharp;

class Program
{
    static async Task Main(string[] args)
    {
        await new BrowserFetcher().DownloadAsync();
        var browser = await Puppeteer.LaunchAsync(new LaunchOptions
        {
            Headless = true,
            Args = new string[] { "--no-sandbox", "--disable-setuid-sandbox" }
        });

        Console.WriteLine("Browser launched successfully.");

        await browser.CloseAsync();
    }
}
