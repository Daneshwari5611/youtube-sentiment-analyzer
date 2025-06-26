# app.py
import streamlit as st
from youtube_api import get_comments
from sentiment import analyze_sentiment
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
st.title("📺 YouTube Video Sentiment Analyzer")

video_url = st.text_input("🔗 Paste YouTube Video URL", "https://www.youtube.com/watch?v=YOUR_ID")

def extract_video_id(url):
    import re
    match = re.search(r"(?:v=|be/)([\w-]{11})", url)
    return match.group(1) if match else None

if st.button("Analyze Comments"):
    video_id = extract_video_id(video_url)
    
    if not video_id:
        st.error("Invalid YouTube URL.")
    else:
        with st.spinner("Fetching comments..."):
            comments = get_comments(video_id)
        
        if not comments:
            st.warning("No comments found or comments disabled.")
        else:
            df = analyze_sentiment(comments)
            st.success(f"Analyzed {len(df)} comments.")
            st.dataframe(df)

            st.subheader("📊 Sentiment Distribution")
            # Add spacing and center chart using columns
            left, center, right = st.columns([1, 2, 1])

            with center:
                fig, ax = plt.subplots(figsize=(6, 4))
                sns.countplot(data=df, x='Sentiment', ax=ax, palette='pastel')
                ax.set_title("Sentiment Overview", fontsize=14)
                st.pyplot(fig)
