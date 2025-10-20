import streamlit as st
import pdfplumber
import pytesseract
from PIL import Image
from io import BytesIO
import re
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ------------------ CONFIG -------------------
MODEL_NAME = "llama-3.1-8b-instant"  # Fast & accurate model
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="AI Smart PDF Summarizer", layout="wide")

# ------------------ LOAD MODEL -------------------
@st.cache_resource
def load_groq_model():
    return ChatGroq(api_key=GROQ_API_KEY, model=MODEL_NAME)

groq_model = load_groq_model()

# ------------------ HELPERS -------------------
def clean_text(text):
    text = text.replace('\x0c', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def detect_content_type(text):
    """Detect whether the text chunk is code, math, or plain text."""
    if re.search(r'\b(def |class |import |#|;|{|\}|console\.log)', text):
        return "code"
    elif re.search(r'[\+\-\*/=<>√∑π∞∫Δθ]', text):
        return "math"
    elif len(text.split()) < 20 and len(re.findall(r'[A-Za-z]', text)) < 30:
        return "image"
    else:
        return "text"

def extract_pdf_text(pdf_bytes):
    pages = []
    with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text and text.strip():
                pages.append(text)
            else:
                try:
                    img = page.to_image(resolution=300).original
                    text = pytesseract.image_to_string(img)
                    pages.append(text)
                except Exception:
                    pages.append("")
    return [clean_text(p) for p in pages if p.strip()]

def summarize_chunk(chunk, content_type):
    """Send prompt to Groq based on detected content type."""
    if content_type == "code":
        prompt = f"Explain this code in simple terms, covering logic and purpose:\n\n{chunk}"
    elif content_type == "math":
        prompt = f"Summarize this mathematical content. Extract formulas, results, and explanations:\n\n{chunk}"
    elif content_type == "image":
        prompt = f"This text was extracted from an image. Describe what the image might represent and summarize it:\n\n{chunk}"
    else:
        prompt = f"Summarize this text concisely, keeping all important details:\n\n{chunk}"

    try:
        response = groq_model.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"⚠️ Error during summarization: {e}"

# ------------------ STREAMLIT UI -------------------
st.title("🧠 AI-Powered Smart PDF Summarizer")
st.caption("Understands and summarizes code, math, text, and images intelligently.")

uploaded_pdf = st.file_uploader("📂 Upload PDF", type=["pdf"])

if uploaded_pdf:
    with st.spinner("Extracting text from PDF..."):
        pdf_texts = extract_pdf_text(uploaded_pdf.read())

    if not pdf_texts:
        st.error("No text detected. Try uploading a clearer PDF or scanned copy.")
    else:
        st.success(f"✅ Extracted {len(pdf_texts)} pages.")
        st.markdown("### 🔍 Smart Content Classification & Summarization")
        
        all_results = []
        for i, page_text in enumerate(pdf_texts):
            if not page_text.strip():
                continue

            content_type = detect_content_type(page_text)
            st.markdown(f"**Page {i+1} → Detected Type:** `{content_type}`")
            with st.spinner(f"Summarizing page {i+1} ({content_type})..."):
                summary = summarize_chunk(page_text[:1800], content_type)
                all_results.append(f"### Page {i+1} ({content_type.capitalize()})\n{summary}\n")

        final_summary = "\n\n".join(all_results)
        st.markdown("## 🧾 Final Smart Summary")
        st.write(final_summary)

        st.download_button("📥 Download Summary", final_summary, file_name="smart_summary.txt")
else:
    st.info("Please upload a PDF file to start summarizing.")
