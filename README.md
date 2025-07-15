# 🚀 AI Startup Forecast Dashboard

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Live-Online-brightgreen?logo=rocket)

> A dynamic and interactive Streamlit dashboard that analyzes India's startup funding ecosystem, tracks investment trends, identifies top sectors and cities, and forecasts future funding using machine learning with **Prophet**.

🌐 **Live App:** [Click to Launch 🚀](https://swathixx-ai-startup-forecast.streamlit.app/)

---

## 📊 Key Features

- ✅ **Real-time filtering** by industry, city, and year
- 📍 **Top cities** and **industry trends** by funding amount
- 💼 **Top investors** with frequency of investments
- 📈 **Time series investment analysis**
- 🔮 **AI-Powered Forecasting** using [Facebook Prophet](https://facebook.github.io/prophet/)
- 📥 **Download forecast results** as CSV
- 🧠 Clear KPIs: Total startups, top-funded city, and total investments
- 🌙 Modern dark UI with bold fonts & animations

---




---

## 🗂️ Project Structure
📦startup-ecosystem-dashboard
┣ 📄 startup_dashboard.py # Streamlit App code
┣ 📄 startup_funding.csv # Dataset
┣ 📄 requirements.txt # Required Python libraries
┗ 📄 README.md # Project documentation


---

## ⚙️ Tech Stack

| Layer | Tools |
|-------|-------|
| 💻 Frontend | Streamlit, HTML-in-Markdown, CSS |
| 📊 Visualization | Plotly, AgGrid |
| 🧮 Data Handling | Pandas |
| 🔮 Forecasting | Prophet (from Meta/Facebook) |
| 📦 Deployment | Streamlit Cloud |

---

## 🚀 Run the App Locally

To run this project on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/swathixx/startup-ecosystem-dashboard.git
cd startup-ecosystem-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run startup_dashboard.py

