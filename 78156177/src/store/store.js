import { configureStore } from "@reduxjs/toolkit"
import { combineReducers } from "redux"

import appReducer from "./appSlice"

const rootReducer = combineReducers({
  app: appReducer,
})

export const store = configureStore({
  reducer: rootReducer,
  devTools: true,
})
