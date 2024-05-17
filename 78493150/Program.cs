using System.Text;
using System.Net;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;
using RabbitMQ.Stream.Client;
using RabbitMQ.Stream.Client.Reliable;

class Program
{
    public static async Task Main(string[] args)
    {
         // Use the name of the RabbitMQ service.
        string dnsName = "rabbitmq";
        int port = 5552;

        try
        {
            // Resolve DNS name into IP address.
            IPAddress[] addresses = Dns.GetHostAddresses(dnsName);

            // Add port to get a dull endpoint.
            IPEndPoint endPoint = new IPEndPoint(addresses[0], port);
            Console.WriteLine("Connect to RabbitMQ at {0}.", endPoint);

            var streamSystem = await StreamSystem.Create(
                new StreamSystemConfig()
                {
                    UserName = "guest",
                    Password = "guest",
                    Endpoints = new List<EndPoint>() {endPoint}
                }
            ).ConfigureAwait(false);
        }
        catch (Exception e)
        {
            Console.WriteLine("An error occurred: " + e.Message);
        }

        // Pause to give time to connect to running container.
        await Task.Delay(300000);
    }
}
