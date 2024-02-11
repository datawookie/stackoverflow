FROM ubuntu:latest

RUN apt update -q && \
    apt install -q -y wget net-tools && \
    rm -rf /var/lib/apt/lists/* && \
    wget -O xampp-installer \
        "https://psychz.dl.sourceforge.net/project/xampp/XAMPP Linux/8.2.12/xampp-linux-x64-8.2.12-0-installer.run" && \
    chmod 755 xampp-installer && \
    ./xampp-installer

EXPOSE 80 3306

CMD /opt/lampp/lampp start && tail -f /opt/lampp/logs/error_log
