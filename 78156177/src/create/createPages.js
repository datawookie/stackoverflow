const path = require(`path`)

/**
 * Create Pages
 * @description This function creates all the individual blog pages in this site.
 * @param {Array} pages
 * @param {Object} gatsbyUtilities
 */
module.exports = async ({ pages, gatsbyUtilities }) =>
  Promise.all(
    pages.map(({ previous, page, next }) => {
      // createPage is an action passed to createPages
      // See https://www.gatsbyjs.com/docs/actions#createPage for more info
      gatsbyUtilities.actions.createPage({
        // Use the WordPress uri as the Gatsby page path
        // This is a good idea so that internal links and menus work 👍
        path: page.uri,

        // use the blog post template as the page component
        component: path.resolve(`./src/templates/page.js`),

        // `context` is available in the template as a prop and
        // as a variable in GraphQL.
        context: {
          // we need to add the post id here
          // so our blog post template knows which blog post
          // the current page is (when you open it in a browser)
          id: page.id,

          // We also use the next and previous id's to query them and add links!
          previousPostId: previous ? previous.id : null,
          nextPostId: next ? next.id : null,
        },
      })
    }),
  )
