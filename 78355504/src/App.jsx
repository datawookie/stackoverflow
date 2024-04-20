// import { useState } from 'react'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
import HomePage from './pages/HomePage.jsx'
import RootLayout from './pages/Root.jsx'

function App() {
  // const [count, setCount] = useState(0)
  const router = createBrowserRouter([
    {
      path: '/',
      element: <RootLayout />,
      children: [
        { path: '/', element: <HomePage /> },
      ]
    }
  ])

  return (<RouterProvider router={router} ></RouterProvider>
  )
}

export default App
