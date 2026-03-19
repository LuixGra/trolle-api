import { Link } from "react-router-dom"

export default function Navbar(){

  function logout(){
    localStorage.removeItem("token")
    window.location.href = "/"
  }

  return(
    <div style={{
      display:"flex",
      justifyContent:"space-between",
      alignItems:"center",
      padding:"15px 30px",
      background:"#111827",
      color:"white"
    }}>

      <div style={{fontWeight:"bold"}}>
        Trolle
      </div>

      <div style={{display:"flex", gap:"20px"}}>
        <Link style={{color:"white"}} to="/dashboard">Dashboard</Link>
        <Link style={{color:"white"}} to="/tasks">Tasks</Link>
        <button onClick={logout}>Logout</button>
      </div>

    </div>
  )
}