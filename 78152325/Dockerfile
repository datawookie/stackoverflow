FROM python:3.11.4-alpine

RUN apk add firefox && \
    pip install selenium==4.18.1

COPY selenium-firefox.py .

ENV MOZ_HEADLESS=1

CMD python3 selenium-firefox.py
