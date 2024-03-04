FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

WORKDIR /src
COPY ["PuppeteerProject/PuppeteerProject.csproj", "PuppeteerProject/"]
RUN dotnet restore "PuppeteerProject/PuppeteerProject.csproj"

COPY . .
WORKDIR "/src/PuppeteerProject"
RUN dotnet build "PuppeteerProject.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "PuppeteerProject.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:6.0

RUN apt-get update && \
    apt-get install -y \
        wget \
        gnupg2 \
        apt-transport-https \
        ca-certificates \
        fonts-liberation \
        libappindicator3-1 \
        libasound2 \
        libatk-bridge2.0-0 \
        libatk1.0-0 \
        libcups2 \
        libdbus-1-3 \
        libgdk-pixbuf2.0-0 \
        libnspr4 \
        libnss3 \
        libx11-xcb1 \
        libxcomposite1 \
        libxdamage1 \
        libxrandr2 \
        xdg-utils \
        libgbm1 \
        libxcb-dri3-0 \
        libxss1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=publish /app/publish .
EXPOSE 8000

CMD ["dotnet", "PuppeteerProject.dll"]
