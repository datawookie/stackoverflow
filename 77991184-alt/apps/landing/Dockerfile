
FROM node:18.17.0-alpine as base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

RUN apk add --no-cache libc6-compat
RUN apk update

# BUILDER -----------------------------------------------------------------------------------------

FROM base AS builder

WORKDIR /app

RUN pnpm add -g turbo
COPY . .
RUN turbo prune landing --docker

COPY ./package.json ./pnpm-lock.yaml ./pnpm-workspace.yaml /app/
COPY ./apps/landing /app/apps/landing

# RUN npm install -g pnpm
RUN pnpm install --frozen-lockfile

WORKDIR /app/apps/landing
RUN pnpm run build

# INSTALLER ---------------------------------------------------------------------------------------

# FROM base AS installer

# WORKDIR /app

CMD /bin/sh -c "sleep 600"



# # Build the project


# # Stage 2: Run the application
# FROM node:18.17.0-alpine

# WORKDIR /app

# COPY --from=builder /app/apps/landing/.next ./.next
# COPY --from=builder /app/apps/landing/public ./public
# COPY --from=builder /app/apps/landing/package.json ./package.json

# RUN npm install -g pnpm
# RUN pnpm install next

# EXPOSE 3000

# # CMD ["pnpm", "start"]
# # CMD node server.js
# CMD node /app/.next/standalone/apps/landing/server.js
