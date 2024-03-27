import { readFileSync } from 'fs'
import path from 'path'
import { gql } from 'graphql-tag'
import { createYoga } from 'graphql-yoga'
import { createServer } from 'http'
import { makeExecutableSchema } from '@graphql-tools/schema'
import { resolvers } from './resolvers'

const typeDefs = gql(
  readFileSync(path.resolve(__dirname, './schema.graphql'), {
    encoding: 'utf-8',
  })
)

function startYogaServer() {
  const schema = makeExecutableSchema({ typeDefs, resolvers })
  const yoga = createYoga({ schema })
  const server = createServer(yoga)
  server.listen(4000, () => {
    console.info('Server is running on http://localhost:4000/graphql')
  })
}

startYogaServer()
