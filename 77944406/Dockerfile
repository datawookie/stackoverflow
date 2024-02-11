FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
        apt-utils \
        portaudio19-dev \
        python3-dev \
        gcc \
        wget

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . /app

# Get some sample audio.
RUN wget -q https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav

CMD ["python3", "audio.py"]
