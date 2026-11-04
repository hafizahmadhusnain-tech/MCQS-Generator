import streamlit as st
from PIL import Image
from transformers import pipeline, VitsModel, AutoTokenizer
import torch
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import numpy as np
import io
from scipy.io.wavfile import write
import asyncio
import sys
import warnings

if sys.platform == 'win32':
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="asyncio")
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except Exception:
        pass

load_dotenv()

st.set_page_config(page_title="AI Multimodal Pipeline", layout="wide")
st.title("🖼️ ➔ 📝 ➔ 🔊 Multimodal AI Pipeline")
st.markdown("This pipeline uses **VQA (Hugging Face)** to analyze an image, **Gemini (LangChain)** to write a story about it, and **MMS-TTS (Hugging Face)** to read the story out loud.")

@st.cache_resource(show_spinner=False)
def load_vqa_model():
    return pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")

@st.cache_resource(show_spinner=False)
def load_tts_model():
    model = VitsModel.from_pretrained("facebook/mms-tts-eng")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")
    return model, tokenizer

with st.spinner("Loading Hugging Face models into memory..."):
    img_pipe = load_vqa_model()
    tts_model, tts_tokenizer = load_tts_model()

st.sidebar.header("Pipeline Inputs")
uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
question = st.sidebar.text_input("Ask a question about the image:", value="what is in this img ?")

api_key_to_use = os.getenv("GOOGLE_API_KEY")

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", width=400)
    
    if st.button("Run Pipeline", type="primary"):
        if not api_key_to_use:
            st.error("⚠️ Google API Key not found! Please make sure it is added in your .env file as GOOGLE_API_KEY=your_key_here")
        else:
            st.subheader("Step 1: Visual Question Answering (VQA)")
            with st.spinner("Analyzing image..."):
                vqa_result = img_pipe(img, question, top_k=1)
                topic = vqa_result[0]['answer']
            
            st.success(f"**Question:** {question}  \n**Answer (Detected Topic):** {topic.capitalize()}")
            
            st.subheader("Step 2: Text Generation")
            with st.spinner("Generating note based on the topic..."):
                llm = ChatGoogleGenerativeAI(
                    model='gemini-3.8-flash', 
                    api_key=api_key_to_use,
                    temperature=0.2,
                    max_tokens=1024
                )           
                llm_result = llm.invoke(f"Write a short, engaging 2-sentence note on topic: {topic}")
                generated_text = llm_result.text
                
            st.info(generated_text)
            
            st.subheader("Step 3: Audio Generation (TTS)")
            with st.spinner("Synthesizing speech..."):
                inputs = tts_tokenizer(generated_text, return_tensors="pt")
                
                with torch.no_grad():
                    output = tts_model(**inputs).waveform
                
                audio_data = output.squeeze().numpy()
                sample_rate = tts_model.config.sampling_rate
                max_amp = np.max(np.abs(audio_data))
                if max_amp > 0:
                    audio_data = audio_data / max_amp
                
                audio_data = audio_data.astype(np.float32)
                
                wav_io = io.BytesIO()
                write(wav_io, sample_rate, audio_data)
                wav_io.seek(0)                
            st.audio(wav_io, format="audio/wav")
            st.success("✅ Pipeline completed successfully!")