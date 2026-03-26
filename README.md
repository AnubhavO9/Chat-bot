# 🤖 AI Chatbot (Python + OpenAI)

A simple yet powerful AI chatbot built using **Python** and the **OpenAI API**.
This project demonstrates how to create a conversational assistant with memory, environment-based configuration, and optional UI support.

---

## 🚀 Features

* 💬 Interactive chatbot (CLI & Streamlit UI)
* 🧠 Maintains conversation history (context-aware)
* 🔐 Secure API key handling using `.env`
* ⚡ Fast and lightweight setup
* 🖥️ Optional web UI using Streamlit (no HTML required)

---

## 🛠️ Tech Stack

* Python 3.x
* OpenAI API
* Streamlit (for UI)
* python-dotenv

---

## 📁 Project Structure

```
ai-chatbot/
│── venv/
│── app.py          # Streamlit UI chatbot
│── main.py         # CLI chatbot
│── .env            # API key (not pushed to GitHub)
│── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

👉 Get your API key from: https://platform.openai.com/api-keys

---

## ▶️ Run the Chatbot

### 🔹 CLI Version

```bash
python main.py
```

---

### 🔹 Web UI (Streamlit)

```bash
streamlit run app.py
```

---

## ⚠️ Common Issues

### ❌ 429 Error (Quota Exceeded)

* Add billing at: https://platform.openai.com/account/billing
* Ensure your API key is valid

---

## 💡 Future Enhancements

* 📄 PDF / Document-based Q&A (RAG)
* 🧠 Memory persistence (database)
* 🔌 FastAPI backend integration
* ☁️ Cloud deployment (Docker / GCP / AWS)
* 🤖 Multi-agent workflows

---

## 🧠 Learnings

This project demonstrates:

* API integration with OpenAI
* Stateful conversation handling
* Environment variable management
* Building AI apps without frontend frameworks

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* OpenAI API
* Streamlit
* Python community

---

## 👨‍💻 Author

**Anubhav Sengar**

---

⭐ If you found this helpful, consider giving it a star!
