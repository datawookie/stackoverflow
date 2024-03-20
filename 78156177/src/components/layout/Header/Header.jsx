import React from "react"
import PropTypes from "prop-types"
import { Link, useStaticQuery, graphql } from "gatsby"
import parse from "html-react-parser"

const Header = ({ isHomePage }) => {
  const {
    wp: {
      generalSettings: { title },
    },
  } = useStaticQuery(graphql`
    query HeaderQuery {
      wp {
        generalSettings {
          title
          description
        }
      }
    }
  `)

  return (
    <header className="global-header">
      {isHomePage ? (
        <h1 className="main-heading">
          <Link to="/">{parse(title)}</Link>
        </h1>
      ) : (
        <Link className="header-link-home" to="/">
          {title}
        </Link>
      )}
    </header>
  )
}

Header.defaultProps = {
  isHomePage: false,
}

Header.propTypes = {
  isHomePage: PropTypes.bool,
}

export default Header
