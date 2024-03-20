module.exports = {
  /**
   * This function queries Gatsby's GraphQL server and asks for
   * All WordPress pages. If there are any GraphQL error it throws an error
   * Otherwise it will return the posts 🙌
   *
   * We're passing in the utilities we got from createPages.
   * So see https://www.gatsbyjs.com/docs/node-apis/#createPages for more info!
   */
  getPages: async ({ graphql, reporter }) => {
    const graphqlResult = await graphql(`
      query WpPages {
        allWpPage(sort: { date: DESC }) {
          edges {
            previous {
              id
            }
            page: node {
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
        `There was an error loading your pages`,
        graphqlResult.errors,
      )
      return
    }

    return graphqlResult.data.allWpPage.edges
  },
}
