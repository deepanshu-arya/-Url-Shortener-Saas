# 🚀 URL Shortener SaaS

A full-stack URL Shortener SaaS built using **FastAPI (Backend)** and **React (Frontend)**.  
This project allows users to shorten long URLs, redirect them, and track usage.

---

## 🌐 Live Features

- 🔗 Shorten long URLs instantly
- 🚀 Fast redirection using short links
- 📊 Track number of clicks
- 👤 User signup system
- ⚡ REST API with FastAPI
- 🎨 Clean UI with React

---

## 🛠️ Tech Stack

### Backend:
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

### Frontend:
- React.js
- CSS

---

## 📁 Project Structure
url-shortener-saas/
│
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── crud.py
│ ├── schemas.py
│ ├── auth.py
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ ├── public/
│ └── package.json



---

## ⚙️ Installation & Setup

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
