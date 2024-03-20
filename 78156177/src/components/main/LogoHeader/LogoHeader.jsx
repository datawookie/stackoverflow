import React from "react"

import * as styles from "./LogoHeader.module.scss"

const LogoHeader = ({ className }) => {
  let LogoHeaderClassName = styles.logoHeader

  if (className) {
    LogoHeaderClassName = `${LogoHeaderClassName} ${className}`
  }

  return <div className={LogoHeaderClassName}></div>
}

export default LogoHeader
