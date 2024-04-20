import { Outlet } from 'react-router-dom'
import MainNavigation from '../components/navigations/MainNavigation.jsx'
// import classes from './Root.module.css'

function Root(){
    return (
    <>
      <MainNavigation />
      {/* <main className={classes.content}> */}
      <main className="flex text-center bg-red-50">
        <Outlet />
      </main>
    </>
)
}

export default Root
