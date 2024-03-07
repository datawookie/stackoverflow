FROM node:18-alpine AS base

WORKDIR /app

FROM base AS deps
RUN apk add --no-cache libc6-compat

COPY package.json .npmrc .

RUN  yarn global add pnpm && pnpm i

# BUILDER ---------------------------------------------------------------------

FROM base AS builder

COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN yarn global add pnpm && pnpm build

# RUNNER ----------------------------------------------------------------------

FROM base AS runner

ENV NODE_ENV=production

RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./standalone
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

CMD ["node", "standalone/server.js"]
