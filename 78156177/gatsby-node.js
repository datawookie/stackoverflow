// const { getPosts } = require("./src/api/post")
// const { getPages } = require("./src/api/page")
// const createPostPages = require("./src/create/createPostPages")
// const createPostArchive = require("./src/create/createPostArchive")
// const createPages = require("./src/create/createPages")

// This is a simple debugging tool
// dd() will prettily dump to the terminal and kill the process
// const { dd } = require(`dumper.js`)

/**
 * exports.createPages is a built-in Gatsby Node API.
 * It's purpose is to allow you to create pages for your site! 💡
 *
 * See https://www.gatsbyjs.com/docs/node-apis/#createPages for more info.
 */
exports.createPages = async gatsbyUtilities => {
  const posts = await getPosts(gatsbyUtilities)
  const pages = await getPages(gatsbyUtilities)

  // If there are no posts in WordPress, don't do anything
  if (!posts.length) {
    return
  }

  // If there are posts, create pages for them
  await createPostPages({ posts, gatsbyUtilities })

  // And a paginated archive
  await createPostArchive({ posts, gatsbyUtilities })

  // If there are no pages in WordPress, don't do anything
  if (!pages.length) {
    return
  }

  // If there are posts, create pages for them
  await createPages({ pages, gatsbyUtilities })
}
