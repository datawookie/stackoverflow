FROM node:21.6.1

RUN apt-get update && apt-get install -y \
    wget --no-install-recommends \
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
        libpango-1.0-0 \
        libcairo2 \
        libxss1 \
        libxkbcommon0 && \
    rm -rf /var/lib/apt/lists/*

COPY package.json .

RUN npm install -g pnpm

RUN pnpm i puppeteer

# RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser && \
#     mkdir -p /home/pptruser/Downloads && \
#     chown -R pptruser:pptruser /home/pptruser && \
#     chown -R pptruser:pptruser /node_modules && \
#     chown -R pptruser:pptruser /package.json && \
#     chown -R pptruser:pptruser /package-lock.json

# RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
#     && mkdir -p /home/pptruser/Downloads /app \
#     && chown -R pptruser:pptruser /home/pptruser \
#     && chown -R pptruser:pptruser /app

WORKDIR /app

COPY index.js /app

# USER pptruser

CMD ["node", "index.js"]
# CMD ["/bin/bash"]
