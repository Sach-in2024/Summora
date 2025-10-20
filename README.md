# 🌙 Summora --- AI-Powered Smart PDF Summarizer

> **"From visuals to variables, Summora sees it all."**
> <img width="935" height="909" alt="Screenshot 2025-10-20 115610" src="https://github.com/user-attachments/assets/5d8e1e5a-bb8f-4115-b4e2-7dde7c61c49d" />


Summora is an **AI-powered PDF summarizer** that understands and
summarizes **text, code, math, and images** from your documents.\
Powered by **Groq LLM (LLaMA 3.1)** and integrated with **Streamlit**,
it delivers fast, intelligent, and context-aware summaries with stunning
accuracy.

------------------------------------------------------------------------

## ✨ Features

-   🧠 **Smart Content Detection** --- Automatically identifies text,
    code, math, and image-based content.
-   ⚙️ **AI Summarization** --- Uses Groq's *llama-3.1-8b-instant* model
    for concise and meaningful summaries.
-   🖼️ **Image OCR Support** --- Extracts text from images using
    *Tesseract OCR*.
-   📄 **Multi-Page PDF Support** --- Summarizes each page individually
    with classified context.
-   💾 **Downloadable Summary** --- Export all summaries as a neatly
    formatted `.txt` file.
-   ⚡ **Fast and Lightweight** --- Powered by the Groq API for near
    real-time summarization.

------------------------------------------------------------------------

## 🚀 Tech Stack

  Component            Description
  -------------------- ----------------------------------
  **Python**           Core programming language
  **Streamlit**        Web interface for interaction
  **LangChain Groq**   Connects with Groq's LLM API
  **pdfplumber**       Extracts text from PDF pages
  **pytesseract**      Performs OCR on image-based PDFs
  **dotenv**           Manages environment variables

------------------------------------------------------------------------

## 🧩 Installation

``` bash
# Clone the repository
git clone https://github.com/yourusername/Summora.git
cd Summora

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🔑 Environment Setup

Create a `.env` file in the project root and add your Groq API key:

    GROQ_API_KEY=your_groq_api_key_here

------------------------------------------------------------------------

## 🧠 Run the App

``` bash
streamlit run app.py
```

Then open your browser and navigate to:

    http://localhost:8501

------------------------------------------------------------------------

## 🖋️ Example Output

  -----------------------------------------------------------------------
  Type               Example Summary
  ------------------ ----------------------------------------------------
  **Text**           Summarizes articles or paragraphs clearly and
                     concisely.

  **Code**           Explains the logic and functionality of code blocks.

  **Math**           Extracts formulas and simplifies mathematical
                     expressions.

  **Image**          Describes extracted image text and its possible
                     meaning.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🌟 Screenshots

*(Add screenshots of your Streamlit interface here for better visuals.)*

------------------------------------------------------------------------

## 🧰 Requirements

``` bash
streamlit
pdfplumber
pytesseract
langchain_groq
langchain_core
python-dotenv
Pillow
```

------------------------------------------------------------------------

## 🤖 Future Improvements

-   Add multilingual summarization support 🌐\
-   Enable direct PDF-to-Audio summaries 🎧\
-   Introduce cloud storage integration ☁️

------------------------------------------------------------------------

## 🪄 Author

**Sachin Kumar**\
📍 IPU College, Delhi\
💬 *AI & Data Science Enthusiast*

------------------------------------------------------------------------

### ⭐ If you like this project, give it a star on GitHub!

> **Summora --- Illuminate Every Page.**
