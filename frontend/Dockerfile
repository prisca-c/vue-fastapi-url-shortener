ARG NODE_IMAGE=node:22.7.0-alpine3.20
ARG PORT

FROM $NODE_IMAGE AS base

WORKDIR /app

COPY /frontend/package.json ./
COPY /frontend/pnpm-lock.yaml ./

COPY . .

FROM base AS deps

RUN  corepack enable
RUN  pnpm install --frozen-lockfile

FROM base AS build

COPY --from=deps /app/node_modules ./node_modules

RUN corepack enable
RUN pnpm build

FROM base AS production

COPY --from=build /app/.output ./build

ENV PORT=${FONTEND_PORT}

ENTRYPOINT ["sh", "-c", "NITRO_PORT=${PORT} node build/server/index.mjs"]