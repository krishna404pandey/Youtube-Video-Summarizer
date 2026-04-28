# YouTube Video Summarizer

A Streamlit application that fetches transcripts from YouTube videos and uses the **Llama3-8b** model (via Groq) to generate concise, bulleted summaries.

## Features
- Extracts transcripts automatically using `youtube-transcript-api`.
- Summarizes long videos into short, crisp notes.
- Fast inference using the Groq LPU™ Inference Engine.
- Simple and intuitive UI built with Streamlit.

## Tech Stack
- **Frontend:** Streamlit
- **LLM:** Groq (Llama3-8b-8192)
- **Framework:** LangChain
- **API:** YouTube Transcript API

## Prerequisites
- A Groq API Key (Get it at [://groq.com](https://://groq.com/))
- Python 3.9+

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Youtube-Video-Summarizer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_actual_api_key_here
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage
1. Paste a YouTube URL (e.g., `https://youtube.com...`).
2. Click the **Summarize** button.
3. View the AI-generated bulleted notes.