FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env
EXPOSE 80
EXPOSE 443
EXPOSE 5555

WORKDIR /app
COPY . .

RUN dotnet restore "BitflySelenium/BitflySelenium.csproj"
RUN dotnet build "BitflySelenium/BitflySelenium.csproj" -c Release -o build

FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=build-env /app .

ENTRYPOINT ["dotnet", "build/BitflySelenium.dll"]
