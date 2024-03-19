FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base

WORKDIR /

EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

WORKDIR /app

COPY MyApi.csproj .

RUN dotnet restore ./MyApi.csproj
