import React from "react"
import { Link as GatsbyLink } from "gatsby"

import externalLinkCheck from "@helpers/external-link-check"

const Link = ({ children, to, external, ...props }) => {
  const nullCheck = to == null ? "" : to

  if (externalLinkCheck(to) || to == null) {
    return (
      <a target="__blank" href={nullCheck} rel="noopener noreferrer" {...props}>
        {children}
      </a>
    )
  }
  return (
    <GatsbyLink to={nullCheck} {...props}>
      {children}
    </GatsbyLink>
  )
}

export default Link
