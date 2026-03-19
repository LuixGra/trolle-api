import { useState } from "react"
import { useNavigate } from "react-router-dom"
import api from "../api/api"
import "../styles/app.css"

export default function Register(){

  const navigate = useNavigate()

  const [email,setEmail] = useState("")
  const [password,setPassword] = useState("")
  const [error,setError] = useState("")

  async function handleRegister(e){
    e.preventDefault()

    setError("")

    try{
      await api.post("/auth/register",{
        email,
        password
      })

      alert("Conta criada!")

      navigate("/")

    }catch(err){
      setError("Erro ao registrar.")
    }
  }

  return(
    <div className="page">
      <div className="container">

        <div className="card">

          <h1 id="title">Registrar</h1>

          {error && (
            <p style={{color:"red", marginBottom:"10px"}}>
              {error}
            </p>
          )}

          <form onSubmit={handleRegister}>

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
              Criar conta
            </button>

          </form>

          <p style={{marginTop:"10px", textAlign:"center"}}>
            Já tem conta?{" "}
            <span className="link" onClick={()=> navigate("/")}>
              Login
            </span>
          </p>

        </div>

      </div>
    </div>
  )
}