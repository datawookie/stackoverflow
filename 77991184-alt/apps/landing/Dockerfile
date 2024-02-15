# Stage 1: Building the code
FROM node:18.17.0-alpine as builder

WORKDIR /app

# Copy the relevant files to the container
COPY ./package.json ./pnpm-lock.yaml ./pnpm-workspace.yaml /app/
COPY ./apps/landing /app/apps/landing

# Install dependencies
RUN npm install -g pnpm
RUN pnpm install --frozen-lockfile

# Build the project
WORKDIR /app/apps/landing
RUN pnpm run build

# Stage 2: Run the application
FROM node:18.17.0-alpine

WORKDIR /app

COPY --from=builder /app/apps/landing/.next ./.next
COPY --from=builder /app/apps/landing/public ./public
COPY --from=builder /app/apps/landing/package.json ./package.json

RUN npm install -g pnpm
RUN pnpm install next

EXPOSE 3000

# CMD ["pnpm", "start"]
# CMD node server.js
CMD node /app/.next/standalone/apps/landing/server.js
