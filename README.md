# 🤖 AI Customer Support CRM

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite">
<img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge">
<img src="https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge">
<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn">
<img src="https://img.shields.io/badge/TF--IDF-NLP-yellow?style=for-the-badge">
<img src="https://img.shields.io/badge/Logistic%20Regression-Classifier-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Joblib-Model%20Serialization-brightgreen?style=for-the-badge">

</p>

<p align="center">

<img src="https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-Logic-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/Bootstrap-UI-7952B3?style=for-the-badge&logo=bootstrap">

</p>

<p align="center">

<img src="https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git">
<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github">
<img src="https://img.shields.io/badge/Render-Backend%20Hosting-46E3B7?style=for-the-badge">
<img src="https://img.shields.io/badge/Vercel-Frontend%20Hosting-black?style=for-the-badge&logo=vercel">

</p>

<p align="center">
<b>🚀 AI-Powered Customer Support CRM with Automated Ticket Classification, Ticket Lifecycle Management, Search, Filtering, Analytics Dashboard, and Full Deployment.</b>
</p>

---

## 🏆 Highlights

✅ Full-Stack Web Application

✅ Machine Learning Powered Ticket Classification

✅ FastAPI REST API Backend

✅ SQLite Database Integration

✅ Search & Filtering Functionality

✅ Ticket Lifecycle Management

✅ Status Tracking (Open → In Progress → Closed)

✅ Delete Closed Tickets

✅ Public Deployment on Render & Vercel
# 🤖 AI Customer Support CRM

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/Machine%20Learning-TF--IDF%20%2B%20Logistic%20Regression-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Database-SQLite-blueviolet?style=for-the-badge">
</p>

<p align="center">
  <b>An AI-Powered Customer Support CRM that automatically classifies support tickets, manages customer requests, tracks ticket lifecycles, and streamlines support operations.</b>
</p>

---

## 🌟 Project Overview

Customer support teams receive hundreds of tickets daily, making manual classification and tracking inefficient and time-consuming.

This project solves that challenge by integrating **Machine Learning** with a modern CRM system.

The system automatically predicts the category of a support ticket based on the customer's issue description and helps support teams efficiently manage tickets through their lifecycle.

### 🎯 Key Objectives

* Automate ticket categorization using AI.
* Reduce manual effort in ticket routing.
* Improve customer support workflow.
* Track ticket progress from creation to closure.
* Provide a clean and responsive dashboard for support agents.

---

## 🚀 Live Demo

### Frontend

```text
(https://ai-customer-support-crm.vercel.app/)
```

### Backend API

```text
(https://ai-customer-support-crm.onrender.com/)
```

### Swagger Documentation

```text
(https://ai-customer-support-crm.onrender.com/docs)
```

---

## 🧠 Machine Learning Pipeline

The AI engine uses Natural Language Processing (NLP) techniques to classify support tickets into predefined categories.

### Ticket Categories

* Technical Issue
* Billing Inquiry
* Product Inquiry
* Refund Request
* Cancellation Request

### ML Workflow

```text
Customer Ticket
       │
       ▼
Text Preprocessing
       │
       ▼
TF-IDF Vectorization
       │
       ▼
Logistic Regression
       │
       ▼
Predicted Ticket Category
```

### Technologies Used

* TF-IDF Vectorizer
* Logistic Regression
* Scikit-Learn
* Joblib Model Persistence

---

## ✨ Features

### 🤖 AI Ticket Classification

Automatically predicts the ticket category using a trained Machine Learning model.

### 🎫 Ticket Management

* Create Tickets
* View Tickets
* Update Ticket Status
* Delete Closed Tickets

### 📊 Dashboard Analytics

Real-time dashboard displaying:

* Total Tickets
* Open Tickets
* Closed Tickets

### 🔍 Search & Filtering

Search tickets by:

* Ticket ID
* Customer Name
* Email
* Subject
* Description

Filter tickets by:

* Open
* In Progress
* Closed

### 📱 Responsive UI

* Modern dashboard design
* Mobile-friendly interface
* Interactive workflow

---

## 🏗️ System Architecture

```text
┌───────────────────────┐
│      Frontend         │
│  HTML • CSS • JS      │
└──────────┬────────────┘
           │ REST API
           ▼
┌───────────────────────┐
│      FastAPI          │
│      Backend          │
└──────────┬────────────┘
           │
           ▼
┌───────────────────────┐
│   ML Classification   │
│ TF-IDF + Logistic Reg │
└──────────┬────────────┘
           │
           ▼
┌───────────────────────┐
│      SQLite DB        │
└───────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Logistic Regression
* Joblib

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

### Deployment

* Render (Backend)
* Vercel (Frontend)
* GitHub

---

## 📂 Project Structure

```text
AI_CUSTOMER_SUPPORT_CRM
│
├── backend
│   ├── app.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── ticket_classifier.pkl
│   ├── tickets.db
│   └── requirements.txt
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── train.py
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_CUSTOMER_SUPPORT_CRM.git

cd AI_CUSTOMER_SUPPORT_CRM
```

### Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

### Frontend Setup

Open:

```text
frontend/index.html
```

or use Live Server.

---

## 📸 Example Workflow

### Create Ticket

```text
Subject:
Refund not received

Description:
I cancelled my order but have not received my refund.
```

### AI Prediction

```text
Refund Request
```

### Ticket Lifecycle

```text
Open
   ↓
In Progress
   ↓
Closed
   ↓
Delete
```

---

## 🎯 Future Improvements

* Email Notifications
* User Authentication
* Role-Based Access Control
* PostgreSQL Integration
* Advanced NLP Models
* Ticket Priority Prediction
* Customer Satisfaction Analytics

---

## 👨‍💻 Developer

### Manvith Mogaveera

Electronics & Telecommunication Engineering Student

Passionate about:

* Artificial Intelligence
* Machine Learning
* Computer Vision
* Full Stack AI Applications

---

## ⭐ If you found this project useful

Give this repository a star and support the project!

```text
⭐ Star this repository
🍴 Fork the project
🚀 Build something amazing
```


✅ Professional Dashboard UI

---
