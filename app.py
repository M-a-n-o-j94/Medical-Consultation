import torch
import faster_whisper
import google.generativeai as genai
import os
import time
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv
from fastapi import FastAPI

import warnings
warnings.simplefilter("ignore", FutureWarning)

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("❌ Google API Key is missing! Set GOOGLE_API_KEY in your .env file.")
genai.configure(api_key=GOOGLE_API_KEY)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32  
print(f"✅ Using device: {device} | Data type: {dtype}")

model = faster_whisper.WhisperModel("small", device=device, compute_type="float16" if device == "cuda" else "float32")

def capture_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        start_time = time.time()
        audio = recognizer.listen(source)
        capture_time = time.time() - start_time
    return audio, capture_time

def transcribe_audio(audio):
    start_time = time.time()
    try:
        audio_data = audio.get_wav_data()
        temp_audio_path = "temp_audio.wav"
        
        with open(temp_audio_path, "wb") as f:
            f.write(audio_data)
        
        segments, _ = model.transcribe(temp_audio_path)
        os.remove(temp_audio_path)  
        
        transcribed_text = " ".join([segment.text for segment in segments])
        elapsed_time = time.time() - start_time
        print(f"✅ Transcription Time: {elapsed_time:.2f} sec")
        return transcribed_text, elapsed_time
    except Exception as e:
        print(f"❌ Transcription Error: {e}")
        return None, None

def analyze_text_with_ai(text):
    print(f"DEBUG: Sending text to Google Gemini - {text}")
    start_time = time.time()
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(
            f"You are a doctor. Analyze the patient's complaint and give a precise response (brief and to the point):\n\n{text}"
        )
        elapsed_time = time.time() - start_time
        result = getattr(response, "text", "").strip()
        
        print(f"✅ AI Analysis Time: {elapsed_time:.2f} sec")
        return result or "AI did not return a valid response.", elapsed_time
    except Exception as e:
        print(f"❌ Error in AI Analysis: {e}")
        return "Error: AI processing failed.", None

def speak_text(text):
    start_time = time.time()
    try:
        tts = gTTS(text=text, lang='en')
        response_audio_path = "response.mp3"
        tts.save(response_audio_path)
        audio = AudioSegment.from_mp3(response_audio_path)
        play(audio)
        os.remove(response_audio_path)  
        speak_time = time.time() - start_time
        print(f"✅ Text-to-Speech Time: {speak_time:.2f} sec")
        return speak_time
    except Exception as e:
        print(f"❌ Error in Text-to-Speech: {e}")
        return None

if __name__ == "__main__":
    total_start_time = time.time()
    audio, capture_time = capture_audio()
    transcribed_text, transcription_time = transcribe_audio(audio)
    if not transcribed_text:
        print("⚠️ No transcription detected. Retrying...")
    else:
        ai_response, ai_analysis_time = analyze_text_with_ai(transcribed_text)
        print(f"🗣️ AI Response: {ai_response}")
        speak_time = speak_text(ai_response)
        
        total_time = time.time() - total_start_time
        print("\n📊 Performance Metrics:")
        print(f"🎤 Audio Capture Time: {capture_time:.2f} sec")
        print(f"📝 Transcription Time: {transcription_time:.2f} sec")
        print(f"🤖 AI Analysis Time: {ai_analysis_time:.2f} sec")
        print(f"🔊 Text-to-Speech Time: {speak_time:.2f} sec")
        print(f"⏱️ Total Processing Time: {total_time:.2f} sec")
