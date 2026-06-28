const BASE = 'http://localhost:8000'

export async function fetchTodos() {
  const res = await fetch(`${BASE}/todos`)
  if (!res.ok) throw new Error('Failed to fetch todos')
  return res.json()
}

export async function updateTodoStatus(id, status) {
  const res = await fetch(`${BASE}/todos/${id}/status`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status }),
  })
  if (!res.ok) throw new Error('Failed to update todo status')
}

export async function deleteTodo(id) {
  const res = await fetch(`${BASE}/todos/${id}`, { method: 'DELETE' })
  if (!res.ok) throw new Error('Failed to delete todo')
}

export async function fetchHabits() {
  const res = await fetch(`${BASE}/habits`)
  if (!res.ok) throw new Error('Failed to fetch habits')
  return res.json()
}

export async function completeHabit(id) {
  const res = await fetch(`${BASE}/habits/${id}/complete`, { method: 'POST' })
  if (!res.ok) throw new Error('Failed to complete habit')
  return res.json()
}
