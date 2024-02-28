using Microsoft.AspNetCore.Builder;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using System.Threading.Tasks;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();

app.MapGet("/", async (HttpContext httpContext) =>
{
    var dbContext = httpContext.RequestServices.GetRequiredService<ApplicationDbContext>();
    try
    {
        if (await dbContext.Database.CanConnectAsync())
        {
            return Results.Ok("Successfully connected to the database.");
        }
        else
        {
            return Results.Problem("Unable to connect to the database.");
        }
    }
    catch (Exception ex)
    {
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
