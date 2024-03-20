module.exports = {
  /**
   * This function queries Gatsby's GraphQL server and asks for
   * All WordPress blog posts. If there are any GraphQL error it throws an error
   * Otherwise it will return the posts 🙌
   *
   * We're passing in the utilities we got from createPages.
   * So see https://www.gatsbyjs.com/docs/node-apis/#createPages for more info!
   */
  getPosts: async ({ graphql, reporter }) => {
    const graphqlResult = await graphql(`
      query WpPosts {
        allWpPost(sort: { date: DESC }) {
          edges {
            previous {
              id
            }
            post: node {
              id
              uri
              slug
            }
            next {
              id
            }
          }
        }
      }
    `)

    if (graphqlResult.errors) {
      reporter.panicOnBuild(
        `There was an error loading your posts`,
        graphqlResult.errors,
      )
      return
    }

    return graphqlResult.data.allWpPost.edges
  },
}
