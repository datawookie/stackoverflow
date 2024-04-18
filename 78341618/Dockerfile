# FROM python:3.11.7-windowsservercore-1809 as python_image

# FROM mcr.microsoft.com/powershell:nanoserver-1809
# USER ContainerAdministrator
# SHELL ["pwsh", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

# # Copying python from python image
# COPY --from=python_image C:\\Python C:\\Python

# # Updating PATH env variable
# RUN $env:PATH = 'C:\Python;C:\Python\Scripts;{0}' -f $env:PATH ; \
#     [Environment]::SetEnvironmentVariable('PATH', $env:PATH, [EnvironmentVariableTarget]::Machine)

FROM python:3.11.7

# Just checking the python and pip versions
RUN python --version && \
    pip --version

RUN pip install python-pptx
CMD  ["python", "-c", "import pptx"]
