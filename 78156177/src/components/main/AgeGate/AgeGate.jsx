import React, { useState, useEffect, useRef } from "react"
import { useSelector, useDispatch } from "react-redux"
import { motion, AnimatePresence } from "framer-motion"
import { lock, clearBodyLocks, unlock } from "tua-body-scroll-lock"

import { acceptAgeGate, checkAgeGate } from "@store/appSlice"

import LogoHeader from "@components/main/LogoHeader"

import { modal } from "./variants"

import * as styles from "./AgeGate.module.scss"

const AgeGate = () => {
  const modalRef = useRef(null)
  const dispatch = useDispatch()
  const [isOver18, setIsOver18] = useState(null)
  const ageGatePassed = useSelector(state => state.app.ageGatePassed)

  const accept = canAccept => {
    if (canAccept) {
      dispatch(acceptAgeGate())
    }

    setIsOver18(canAccept)
  }

  useEffect(() => {
    dispatch(checkAgeGate())
  }, [dispatch])

  useEffect(() => {
    ageGatePassed ? unlock(modalRef.current) : lock(modalRef.current)

    return () => clearBodyLocks()
  }, [ageGatePassed])

  return (
    <AnimatePresence>
      {!ageGatePassed && (
        <motion.div
          ref={modalRef}
          className={styles.ageGate}
          key="agegate"
          variants={modal}
          initial="hide"
          exit="hide"
          animate={!ageGatePassed && "show"}
        >
          <LogoHeader />

          <div className={styles.inner}>
            <div className={styles.island}>
              <div className={styles.text}>
                <h3>Are you over 18?</h3>
              </div>

              <div className={styles.tabGroup}>
                <button
                  className={`${styles.tab} ${isOver18 ? styles.active : isOver18 === false ? styles.inActive : ""}`}
                  onClick={() => accept(true)}
                >
                  Yes
                </button>
                <button
                  className={`${styles.tab} ${isOver18 === false ? styles.active : isOver18 ? styles.inActive : ""}`}
                  onClick={() => accept(false)}
                >
                  No
                </button>
              </div>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}

export default AgeGate
