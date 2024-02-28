using Microsoft.AspNetCore.Builder;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using System.Threading.Tasks;

var builder = WebApplication.CreateBuilder(args);

// Configure services
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();

// Map a GET endpoint to test database connection
app.MapGet("/", async (HttpContext httpContext) =>
{
    var dbContext = httpContext.RequestServices.GetRequiredService<ApplicationDbContext>();
    try
    {
        // Attempt to connect to the database
        if (await dbContext.Database.CanConnectAsync())
        {
            // Return a successful result if the connection is successful
            return Results.Ok("Successfully connected to the database.");
        }
        else
        {
            // Return a problem result if unable to connect
            return Results.Problem("Unable to connect to the database.");
        }
    }
    catch (Exception ex)
    {
        // Return a problem result if an exception occurs
        return Results.Problem($"An error occurred while connecting to the database: {ex.Message}");
    }
});

await app.RunAsync();

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
    {
    }
}
