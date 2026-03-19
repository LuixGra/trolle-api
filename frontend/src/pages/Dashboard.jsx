import { useEffect, useState } from "react"
import api from "../api/api"
import "../styles/app.css"

export default function Dashboard(){

  const [tasks, setTasks] = useState([])

  useEffect(()=>{
    fetchTasks()
  },[])

  async function fetchTasks(){
    try{
      const token = localStorage.getItem("token")

      const res = await api.get("/tasks", {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })

      setTasks(res.data)

    }catch(err){
      console.log("Erro ao buscar tasks")
    }
  }

  const total = tasks.length
  const completed = tasks.filter(t => t.completed).length
  const pending = total - completed

  return(
    <div className="page">

      <div className="container">

        <h1 id="title">Dashboard</h1>

        <div className="dashboard-grid">

          <div className="card stat">
            <h3>Total Tasks</h3>
            <p>{total}</p>
          </div>

          <div className="card stat">
            <h3>Concluídas</h3>
            <p>{completed}</p>
          </div>

          <div className="card stat">
            <h3>Pendentes</h3>
            <p>{pending}</p>
          </div>

        </div>

      </div>

    </div>
  )
}