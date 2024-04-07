FROM oraclelinux:9

RUN dnf update -y && \
    dnf install -y \
        wget \
        unzip \
        python3.11 \
        python3-pip \
        dbus-x11 \
        gtk3 \
        nss \
        atk \
        at-spi2-atk \
        cups-libs \
        libdrm \
        libxkbcommon \
        libXcomposite \
        libXdamage \
        libXrandr && \
    dnf clean all

RUN wget -q -O chrome-linux64.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chrome-linux64.zip && \
    unzip chrome-linux64.zip && \
    rm chrome-linux64.zip && \
    mv chrome-linux64 /opt/chrome/ && \
    ln -s /opt/chrome/chrome /usr/local/bin/ && \
    wget -q -O chromedriver-linux64.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chromedriver-linux64.zip && \
    unzip -j chromedriver-linux64.zip chromedriver-linux64/chromedriver && \
    rm chromedriver-linux64.zip && \
    mv chromedriver /usr/local/bin/

WORKDIR /bdds

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY bdds.sh .
COPY features ./features

RUN chmod 755 bdds.sh

CMD ["./bdds.sh"]
