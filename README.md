# 🎥 YouTube Comment Sentiment Analyzer

A real-time web app to analyze viewer sentiment on any YouTube video using Python, Streamlit, and the YouTube Data API.

## 🚀 Features
- Paste a YouTube video URL
- Fetches the top comments live
- Analyzes each comment as Positive, Negative, or Neutral using VADER
- Displays a clean sentiment distribution chart
- View full comment sentiment breakdown
- Publicly accessible via Streamlit Cloud

## 🔧 Tech Stack
- Python
- Streamlit
- YouTube Data API v3
- NLTK (VADER Sentiment)
- Pandas, Seaborn, Matplotlib

## 🖥️ Try It Live
👉 [Click here to open the app](https://youtube-sentiment-analyzer-2kvkncdcryzna7c7s7qwcq.streamlit.app/)  
*(Works best on Chrome or Edge — mobile-friendly UI)*

## 🖼️ App Screenshot

![App Screenshot](assets/screenshot1.png)
![App Screenshot](assets/screenshot2.png)

## 📥 Installation (For Developers)
```bash
git clone https://github.com/Daneshwari5611/youtube-sentiment-analyzer.git
cd youtube-sentiment-analyzer
pip install -r requirements.txt
python -m streamlit run app.py

