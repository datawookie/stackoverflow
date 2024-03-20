import { createSlice } from "@reduxjs/toolkit"

const initialState = {
  ageGatePassed: true,
}

const appSlice = createSlice({
  name: "app",
  initialState,
  reducers: {
    acceptAgeGate: state => {
      localStorage.setItem("agegate", true)

      state.ageGatePassed = true
    },
    checkAgeGate: state => {
      state.ageGatePassed = localStorage.getItem("agegate") ? true : false
    },
    resetApp(state) {
      state.ageGatePassed = initialState.ageGatePassed
    },
  },
})

export const { acceptAgeGate, checkAgeGate, resetApp } = appSlice.actions

export default appSlice.reducer
