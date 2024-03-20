/**
 * External Link Check
 * @param {String} link
 * @returns Bool
 */

const externalLinkCheck = link => {
  switch (link) {
    case link.match("wpengine"):
    case link.match("mailto"):
    case link.match("http"):
      return true

    default:
      return false
  }
}

export default externalLinkCheck
