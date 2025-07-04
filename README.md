# TailorTalk – AI Meeting Scheduler Bot

TailorTalk is an AI-powered meeting scheduler that understands natural language input and automatically creates events in your Google Calendar. Just tell it something like _"Book a meeting with the client tomorrow at 3PM"_ and it handles the rest!

---

## 🚀 Features

- ✅ Natural language input (e.g., "Schedule dentist appointment at 5PM")
- ✅ Uses LLM (OpenAI / Gemini) via LangChain for intent extraction
- ✅ Creates events in **Google Calendar** via Service Account
- ✅ Returns a **clickable calendar event link**
- ✅ FastAPI backend with `/chat` endpoint
- ✅ Simple and beautiful frontend built using **Streamlit**

---

## 🛠️ Tech Stack

| Layer       | Tools Used                                      |
|-------------|-------------------------------------------------|
| Frontend    | Streamlit                                       |
| Backend     | FastAPI, Uvicorn                                |
| NLP Engine  | LangChain + OpenAI API                          |
| Calendar    | Google Calendar API (OAuth via Service Account) |
| Deployment  | Backend: Render    Frontend: Streamlit Cloud    |

---

## 📦 Installation

### 1. Clone the repository
git clone https://github.com/keerthipriyab134/TailorTalk.git
cd TailorTalk
**2. Install dependencies**
pip install -r requirements.txt
**3. Add your .env file**
Create a .env file in the root directory with:
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CALENDAR_ID=your_calendar_id_here
Also, place your Google service account JSON file (e.g., service_account.json) in the project root.


![ss3](https://github.com/user-attachments/assets/3d9e36c5-9cf8-4919-8563-2a1756fd1958)
![ss2](https://github.com/user-attachments/assets/a9e10381-117b-4e77-b61a-30496501ffc4)
![ss1](https://github.com/user-attachments/assets/c828f6ca-b37d-47b9-8eaa-b62ce874a60e)
