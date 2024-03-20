import React from "react"
import { Provider } from "react-redux"
import { useStaticQuery, graphql } from "gatsby"

import { store } from "../../../store/store"

import Header from "@components/layout/Header"
import Footer from "@components/layout/Footer"
import AgeGate from "@components/main/AgeGate"

import * as styles from "./Layout.module.scss"

const Layout = ({ isHomePage, children }) => {
   const {
    wpAcfAgeGateSettings,
  } = useStaticQuery(graphql`
    query LayoutQuery {
      wpAcfAgeGateSettings {
        acfAgeGate {
          acfShowAgeGate
        }
      }
    }
  `)

  //    const {
  //   wp: {
  //     generalSettings: { title },
  //   },
  // } = useStaticQuery(graphql`
  //   query LayoutQuery {
  //     wp {
  //       generalSettings {
  //         title
  //         description
  //       }
  //     }
  //   }
  // `)

  return (
    <Provider store={store}>
      <div className={styles.layout} data-is-root-path={isHomePage}>
        <Header isHomePage />
        <h1>{JSON.stringify(wpAcfAgeGateSettings)}</h1>
        <main>{children}</main>

        <Footer />
      </div>

      <AgeGate />
    </Provider>
  )
}

export default Layout
