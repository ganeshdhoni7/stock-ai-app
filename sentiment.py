import streamlit as st
from textblob import TextBlob
import nltk

nltk.download('punkt')

def show_sentiment():
    st.subheader("📰 Market Sentiment Analysis")

    news = st.text_area("Paste Latest News Headlines or Article Here")

    if st.button("Analyze"):
        blob = TextBlob(news)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            st.success(f"🙂 Positive Sentiment (Polarity: {polarity:.2f})")
        elif polarity < 0:
            st.error(f"☹️ Negative Sentiment (Polarity: {polarity:.2f})")
        else:
            st.info("😐 Neutral Sentiment")

        st.markdown("**Sentence-wise Sentiment:**")
        for sentence in blob.sentences:
            st.write(f"- {sentence}: {TextBlob(str(sentence)).sentiment.polarity:.2f}")
