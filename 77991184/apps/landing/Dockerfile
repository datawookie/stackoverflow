FROM node:18.17.0-alpine as base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

RUN apk add --no-cache libc6-compat
RUN apk update

RUN pnpm add -g turbo

# BUILDER ---------------------------------------------------------------------

FROM base AS builder

WORKDIR /app

COPY . .
RUN turbo prune landing --docker

COPY ./package.json ./pnpm-lock.yaml ./pnpm-workspace.yaml /app/
COPY ./apps/landing /app/apps/landing

RUN pnpm install --frozen-lockfile

WORKDIR /app/apps/landing
RUN pnpm turbo run build

# RUNNER ----------------------------------------------------------------------

FROM base AS runner

WORKDIR /app

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs
USER nextjs

COPY --from=builder /app/apps/landing/.next/standalone /app

CMD node ./apps/landing/server.js
