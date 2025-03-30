# 💬 AI Chatbot Research Prototype

A multi-platform conversational AI assistant built for the banking industry using:
- 🔹 OpenAI GPT (via Streamlit)
- 🔹 IBM Watson Assistant
- 🔹 ChatGPT Custom GPT

This project explores responsible AI development aligned with the **AI Act** and **GDPR**, including privacy safeguards, fallback handling, and compliant conversational design.

---

## 🌐 Live Demo

 **Visit the full live demo site:**  
 [https://gabrijelam1.github.io/ai-chatbot-research/](https://gabrijelam1.github.io/ai-chatbot-research/)

The site includes:
-  GPT Prototype (ChatGPT Custom GPT)
-  IBM Watson Assistant (embedded)
-  Streamlit Chatbot using OpenAI API

---

##  Chatbot Use Cases

- Report a lost bank card
- Check account balance (simulated)
- Report fraud
- Loop between actions with fallback support
- Receive GDPR-compliant privacy reminders

---

##  Tech Stack

| Component         | Tool                  |
|------------------|-----------------------|
| Natural Language | OpenAI GPT-3.5 Turbo  |
| No-code Builder  | ChatGPT Custom GPT    |
| Assistant Flow   | IBM Watson Assistant  |
| UI Framework     | Streamlit             |
| Hosting          | GitHub Pages, Streamlit Cloud |
| Privacy          | `.env` + Streamlit Secrets |
| Governance       | AI Act, GDPR principles |

---

##  AI Ethics + Prompt Engineering

This assistant is designed with:
- ✅ **Prompt Engineering Techniques**
- ✅ **Regulatory Mapping** (GDPR & AI Act)
- ✅ **Bias Mitigation** (neutral tone & fallback messages)
- ✅ **No PII Storage** or sensitive data collection

---

## 📂 Repository Contents

```
ai-chatbot-research/
├── app.py              # OpenAI Streamlit chatbot
├── index.html          # GitHub Pages homepage
├── requirements.txt    # Python dependencies
├── README.md           # This file
```

---

##  Getting Started (Local)

1. Clone this repo:
```bash
git clone https://github.com/gabrijelam1/ai-chatbot-research.git
cd ai-chatbot-research
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:
```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

4. Run the app:
```bash
streamlit run app.py
```

---

##  Author

**Gabrijela Marić**  
 AI & Data Analyst | Chatbots · Compliance · Insights
 [Project Page](https://gabrijelam1.github.io/ai-chatbot-research/)  

---

## 📜 License

This project is for academic and portfolio use only.  
All trademarks, company names, and scenarios are fictional and for demonstration purposes only.
