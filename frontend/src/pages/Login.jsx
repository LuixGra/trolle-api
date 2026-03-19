import { useState } from "react"
import { useNavigate } from "react-router-dom"
import api from "../api/api"
import "../styles/app.css"

export default function Login(){

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")

  const navigate = useNavigate()

  async function handleLogin(e){
    e.preventDefault()

    try{
      const formData = new URLSearchParams()
      formData.append("username", email)
      formData.append("password", password)

      const res = await api.post("/auth/login", formData)

      localStorage.setItem("token", res.data.access_token)

      navigate("/dashboard")

    }catch(err){
      setError("Email ou senha inválidos")
    }
  }

  return(
    <div className="page">
      <div className="container">
        <div className="card">

          <h1 id="title">Login</h1>

          {error && <p style={{color:"red", marginBottom:"10px"}}>{error}</p>}

          <form onSubmit={handleLogin}>

            <input
              className="input"
              placeholder="Email"
              value={email}
              onChange={(e)=> setEmail(e.target.value)}
            />

            <input
              className="input"
              type="password"
              placeholder="Senha"
              value={password}
              onChange={(e)=> setPassword(e.target.value)}
            />

            <button className="button" type="submit">
              Entrar
            </button>

          </form>

          <p style={{marginTop:"10px", textAlign:"center"}}>
            Não tem conta?{" "}
            <span className="link" onClick={()=> navigate("/register")}>
              Registrar
            </span>
          </p>

        </div>
      </div>
    </div>
  )
}