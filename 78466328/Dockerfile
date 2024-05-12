FROM node:latest

WORKDIR /app

RUN npm create vite@latest -y . -- --template react-ts && \
    npm install

EXPOSE 5173
ENTRYPOINT [ "npm", "run", "dev" ]
CMD ["--", "--host"]
