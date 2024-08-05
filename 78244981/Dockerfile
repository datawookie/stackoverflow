FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
        wget \
        expect \
        libgomp1 \
        libx11-6 && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/NREL/EnergyPlus/releases/download/v24.1.0/EnergyPlus-24.1.0-9d7789a3ac-Linux-Ubuntu22.04-x86_64.sh

COPY install.exp .

RUN chmod +x EnergyPlus-24.1.0-9d7789a3ac-Linux-Ubuntu22.04-x86_64.sh

RUN expect install.exp

CMD EnergyPlus -v
