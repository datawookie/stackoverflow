FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y \
        xvfb \
        libgl1 \
        libxcb-xinerama0 \
        libxkbcommon-x11-0 \
        libxcb1 \
        libx11-xcb1 \
        libxcb-icccm4 \
        libxcb-image0 \
        libxcb-keysyms1 \
        libxcb-render-util0 \
        libxcb-shape0 \
        libdbus-1-3 && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

ENV QT_QPA_PLATFORM=xcb

ENV DISPLAY=:99

# For debugging.
#
ENV QT_DEBUG_PLUGINS=1
ENV QT_DEBUG_COMPONENT=1

CMD Xvfb :99 -screen 0 1024x768x24 -ac +extension GLX +render -noreset & \
    python app.py
