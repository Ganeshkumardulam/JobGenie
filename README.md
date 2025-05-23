# 💼 JobGenie – AI-Powered Interview Simulator

**JobGenie** is an open-source, intelligent interview simulation platform that prepares users for real-world job interviews based on their role, experience level, selected skills, and even uploaded resumes.

Built using **FastAPI**, **AutoGen**, and **OpenLLaMA (via Ollama)**, it replicates multiple interview rounds—HR, Managerial, Technical, and DSA—with contextual question generation and real-time AI feedback.

---

## 🔥 Key Features

- 🎯 **Role-Based Interview** – Tailored questions for roles like Backend Developer, Data Analyst, DevOps, etc.
- 🧠 **Experience Level Adaptation** – Adjusts question difficulty for Freshers, Mid-level, and Senior candidates.
- 📝 **Resume Upload** – Parse `.pdf` or `.docx` resumes to generate personalized questions.
- 🧩 **Skill-Based Questions** – Select specific skills (e.g., Python, FastAPI, DSA) to focus the interview.
- 🗣️ **Round Selection** – Choose the type of round: HR, Technical, Managerial, or DSA.
- 🧾 **AI Feedback** – Real-time evaluation of your answers: relevance, confidence, clarity, and suggestions.
- 📊 **Performance Summary** – End-of-interview report with strengths and improvement areas.

---

## 🛠️ Tech Stack

| Layer         | Tool/Library            |
|---------------|--------------------------|
| Backend API   | FastAPI                  |
| AI Agents     | AutoGen + OpenLLaMA (Ollama) |
| Resume Parser | PyMuPDF / python-docx    |
| Frontend      | HTML/JS or React (optional) |
| Storage       | SQLite / JSON            |
| Hosting       | Local / Render / Vercel (for UI) |

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
git clone https://github.com/yourusername/jobgenie.git
cd jobgenie
pip install -r requirements.txt
