FROM node:20

# Install ffmpeg
RUN apt-get -y update \
    && apt-get install -y ffmpeg \
    && ffmpeg -version && which ffmpeg

# Set working directory
WORKDIR /usr/src/app

# Copy application files
COPY . .

# Install tools dependencies
# RUN cd tools && npm install --only=production && npm install axios

# Install responder dependencies and TypeScript
WORKDIR /usr/src/app/responder
COPY package*.json .
RUN npm cache clean --force
RUN npm install --only=production && npm install -g typescript

# # Build TypeScript files
# RUN tsc

# # Clean up
# RUN npm prune --production && \
#     npm cache clean --force && \
#     rm -rf /root/.npm /root/.node-gyp /tmp/*

# # Expose port
# EXPOSE 8080

# # Set command to run the application
# CMD ["node", "main.mjs"]
