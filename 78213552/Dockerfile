FROM node:20

RUN apt-get update && \
    apt-get -q -y install \
        git \
        gcc \
        libleptonica-dev \
        libtesseract-dev \
        tesseract-ocr \
        tesseract-ocr-hin \
        tesseract-ocr-ara \
        tesseract-ocr-fra \
        tesseract-ocr-fin \
        tesseract-ocr-jpn \
        tesseract-ocr-pol \
        tesseract-ocr-spa \
        tesseract-ocr-rus \
        tesseract-ocr-ita \
        tesseract-ocr-por \
        tesseract-ocr-kor \
        tesseract-ocr-ces \
        tesseract-ocr-dan \
        tesseract-ocr-deu \
        tesseract-ocr-nld \
        tesseract-ocr-swe \
        tesseract-ocr-tur

COPY app.js .
COPY package.json .
COPY .env .

RUN npm install

EXPOSE 3000

CMD node app.js
