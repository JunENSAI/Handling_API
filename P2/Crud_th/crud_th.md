## 1. What is CRUD?

CRUD stands for the four basic operations of persistent storage:

* **C**reate

* **R**ead

* **U**pdate

* **D**elete

---

## 2. Mapping HTTP to CRUD

A REST API maps these operations to specific HTTP Verbs:


| Operation | HTTP Verb | Success Code | Description |
| :--- | :--- | :--- | :--- |
| **Create** | `POST` | 201 Created | Add a new record. |
| **Read** | `GET` | 200 OK | View one or all records. |
| **Update** | `PUT` | 200 OK | Replace a record entirely. |
| **Delete** | `DELETE` | 204 No Content | Remove a record. |

---

## 3. Handling Errors (`HTTPException`)

If a user tries to delete a Task ID that doesn't exist, you shouldn't crash. You should return a **404 Not Found**. FastAPI uses `raise HTTPException(status_code=404)` to do this cleanly.

---