from youtube_transcript_api import YouTubeTranscriptApi
ytt_api = YouTubeTranscriptApi()

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq
import streamlit as st

def get_video_id(url):
    if "youtube.com/watch?v=" in url        return url.split("v=")[1]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    

def get_transcript_text(video_id):
    raw_transcript = ytt_api.fetch(video_id)
    transcript_text = ""
    for snippet in raw_transcript:
        transcript_text += snippet.text + " "
    return transcript_text


llm = ChatGroq(
        model_name="llama3-8b-8192",
        temperature=0.3,
        groq_api_key=api_key
    )

def get_summary(transcript_text):
    prompt = """Please generate a bulleted summary/notes
      of the given transcript from a youtube video. keep it short and crisp as required. Start off by saying
      Here is the detailed summary of the provided youtube video:""" + transcript_text
    return llm.invoke(prompt).content



st.title("YouTube Video Summarizer")
video_url = st.text_input("Paste YouTube video URL: ")


if st.button("Summarize"):
    vid_id = get_video_id(video_url)
    ttext = get_transcript_text(vid_id)
    if video_url:
        st.info("Fetching transcript and summarizing...")

        st.subheader("Summary: ")
        st.markdown(get_summary(ttext))
    else:
        st.warning("Please enter a URL.")
    