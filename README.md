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


![ss3](https://github.com/user-attachments/assets/14bddfb9-8b3e-4db3-8c22-345134de15da)
![ss2](https://github.com/user-attachments/assets/2b6acda7-9ce0-4587-8af9-82956228e8fc)
![ss1](https://github.com/user-attachments/assets/4f98618e-f528-4204-9c9e-a103db11fb3d)
