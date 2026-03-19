import { useEffect, useState } from "react"
import api from "../api/api"
import "../styles/app.css"

export default function Tasks(){

  const [tasks,setTasks] = useState([])
  const [title,setTitle] = useState("")
  const [description,setDescription] = useState("")

  const [editingId,setEditingId] = useState(null)
  const [editingTitle,setEditingTitle] = useState("")
  const [editingDescription,setEditingDescription] = useState("")

  const token = localStorage.getItem("token")

  async function loadTasks(){
    const res = await api.get("/tasks", {
      headers: { Authorization: `Bearer ${token}` }
    })
    setTasks(res.data)
  }

  async function createTask(){
    if(!title) return

    await api.post("/tasks",
      { title, description },
      { headers: { Authorization: `Bearer ${token}` } }
    )

    setTitle("")
    setDescription("")
    loadTasks()
  }

  async function deleteTask(id){
    await api.delete(`/tasks/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    loadTasks()
  }

  async function toggleTask(task){
    await api.put(`/tasks/${task.id}`,
      { completed: !task.completed },
      { headers: { Authorization: `Bearer ${token}` } }
    )

    loadTasks()
  }

  function startEdit(task){
    setEditingId(task.id)
    setEditingTitle(task.title)
    setEditingDescription(task.description || "")
  }

  async function saveEdit(id){
    await api.put(`/tasks/${id}`,
      {
        title: editingTitle,
        description: editingDescription
      },
      { headers: { Authorization: `Bearer ${token}` } }
    )

    setEditingId(null)
    loadTasks()
  }

  useEffect(()=>{
    loadTasks()
  },[])

  return(
    <div className="page">
      <div className="container">

        <h1 id="title">Tasks</h1>

        {/* criar task */}
        <div className="card form-group" style={{marginBottom:"20px"}}>

          <input
            className="input"
            placeholder="Título"
            value={title}
            onChange={e => setTitle(e.target.value)}
          />
          
          <input
            className="input"
            placeholder="Descrição"
            value={description}
            onChange={e => setDescription(e.target.value)}
          />
          
          <button className="button" onClick={createTask}>
            Adicionar
          </button>

        </div>

        {/* lista */}
        <div className="grid">
          {tasks.map(task => (

            <div
              key={task.id}
              className={`task-card ${task.completed ? "completed" : ""}`}
              onClick={() => toggleTask(task)}
            >

              <div className="task-left">
                <div className={`check ${task.completed ? "active" : ""}`}></div>

                <div className="task-text">

                  {editingId === task.id ? (
                    <>
                      <input
                        className="input"
                        value={editingTitle}
                        onChange={e => setEditingTitle(e.target.value)}
                      />

                      <input
                        className="input"
                        value={editingDescription}
                        onChange={e => setEditingDescription(e.target.value)}
                      />
                    </>
                  ) : (
                    <>
                      <span className="task-title">{task.title}</span>
                      <span className="task-desc">{task.description}</span>
                    </>
                  )}

                </div>
              </div>

              <div className="actions" onClick={(e)=> e.stopPropagation()}>

                {editingId === task.id ? (
                  <button
                    className="button-secondary"
                    onClick={() => saveEdit(task.id)}
                  >
                    Salvar
                  </button>
                ) : (
                  <button
                    className="button-secondary"
                    onClick={() => startEdit(task)}
                  >
                    Editar
                  </button>
                )}

                <button
                  className="button-danger"
                  onClick={() => deleteTask(task.id)}
                >
                  Deletar
                </button>

              </div>

            </div>

          ))}
        </div>

      </div>
    </div>
  )
}