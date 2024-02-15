FROM node:18-alpine AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

# BUILDER -----------------------------------------------------------------------------------------

FROM base AS builder
RUN apk add --no-cache libc6-compat
RUN apk update
WORKDIR /app
RUN pnpm add -g turbo
COPY . .
RUN turbo prune landing --docker

# INSTALLER ---------------------------------------------------------------------------------------

FROM base AS installer
RUN apk add --no-cache libc6-compat
RUN apk update
WORKDIR /app
RUN pnpm add -g turbo

COPY .gitignore .gitignore
COPY --from=builder /app/out/json/ .
COPY --from=builder /app/out/pnpm-lock.yaml ./pnpm-lock.yaml
COPY --from=builder /app/out/pnpm-workspace.yaml ./pnpm-workspace.yaml
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile --filter=landing...

COPY --from=builder /app/out/full/ .
RUN pnpm turbo run build --filter=landing...

ENV NODE_ENV=production
ENV PORT=3000

# RUNNER ------------------------------------------------------------------------------------------

FROM base AS runner
WORKDIR /app

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs
USER nextjs

# COPY --from=installer /app/apps/landing/next.config.js .
# COPY --from=installer /app/apps/landing/package.json .

COPY --from=installer --chown=nextjs:nodejs /app/apps/landing/.next/standalone/ .
# COPY --from=installer --chown=nextjs:nodejs /app/apps/landing/.next/static ./apps/landing/.next/static
# COPY --from=installer --chown=nextjs:nodejs /app/apps/landing/public ./apps/landing/public
# # COPY --from=installer --chown=nextjs:nodejs /app/apps/landing/.next/standalone/server.js ./apps/landing/

EXPOSE 3000

CMD node server.js

# FROM base AS runner
# WORKDIR /app

# # Setup user
# RUN addgroup --system --gid 1001 nodejs
# RUN adduser --system --uid 1001 nextjs
# USER nextjs

# # Copy the standalone application output from the installer stage
# COPY --from=installer --chown=nextjs:nodejs /app/apps/landing/.next/standalone /app

# # Expose the port the app runs on
# EXPOSE 3000

# # Start the application
# CMD ["node", "server.js"]

# RUN rm -rf ./node_modules
# COPY --from=builder /app/node_modules_temp ./node_modules
