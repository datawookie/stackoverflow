
import { useState } from 'react'
import reactLogo from '../assets/react.svg'
import viteLogo from '/vite.svg'
import './HomePage.module.css'

export default function HomePage() {
  const [count, setCount] = useState(0)

    return (
      <>
        <p>The APP URL is: {import.meta.env.VITE_APP_URL}.</p>
      </>);
}
