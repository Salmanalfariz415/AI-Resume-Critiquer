# 📄 AI Resume Critiquer

An AI-powered resume analysis tool that provides smart feedback, improvement suggestions, and ATS optimization tips using OpenAI.

Built with a modular Streamlit architecture for better scalability and clean code structure.

---

## 🚀 Features

* 📄 Upload PDF resumes
* 🧠 AI-powered analysis using OpenAI
* 📊 Detailed feedback:

  * Strengths & weaknesses
  * Resume improvement suggestions
  * ATS optimization tips
* ⚡ Fast and interactive UI with Streamlit
* 🧩 Modular code structure (multi-page logic)

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI API
* PyPDF2
* python-dotenv

---

## 📂 Project Structure

```bash
ai-chatbot/
│── app.py          # Main entry point
│── home.py         # Home page UI
│── resume.py       # Resume analysis logic
│── .env            # API keys (not pushed)
│── .gitignore
│── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-critiquer.git
cd ai-resume-critiquer
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. Text is extracted using PyPDF2
3. Resume content is sent to OpenAI
4. AI returns structured feedback
5. Results are displayed in Streamlit UI

---

## 🎯 Use Cases

* Students preparing for placements
* Job seekers improving resumes
* Quick ATS-friendly optimization

---

## ⚠️ Important Notes

* Avoid uploading sensitive personal data
* OpenAI API usage may incur charges

---

## 🔥 Future Improvements

* DOCX support
* Resume scoring system
* Job description matching
* Downloadable feedback report
* Multi-role resume analysis (SDE / Data / DevOps)

---

## 🤝 Contributing

Pull requests are welcome. Feel free to improve UI, features, or performance.

---

## 📜 License

MIT License
