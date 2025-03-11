#Voice-Powered Medical Consultation with AI
This repository contains a Python application that simulates a medical consultation using voice input, speech-to-text transcription, AI-powered analysis, and text-to-speech output. Users can speak their medical complaints, which are then transcribed, analyzed by Google's Gemini AI, and the AI's response is spoken back to the user.

# Key Features:

Voice Input: Captures user's voice using the speech_recognition library.
Speech-to-Text Transcription: Utilizes faster-whisper for fast and accurate audio transcription.
AI-Powered Analysis: Leverages Google's Gemini AI (google-generativeai) to analyze the transcribed text and provide medical advice.
Text-to-Speech Output: Converts the AI's response to speech using gTTS and plays it back to the user using pydub.
FastAPI Integration: Includes a basic FastAPI endpoint for potential future web integration.
Performance Metrics: Provides detailed timing metrics for each stage of the process, including audio capture, transcription, AI analysis, and text-to-speech.
Environment Variable Management: Uses .env file and python-dotenv to manage the Google API key securely.
CUDA acceleration: Uses GPU acceleration when available, and falls back to CPU when a GPU is not available.

# Dependencies:

torch
faster-whisper
google-generativeai
speech_recognition
gTTS
pydub
python-dotenv
fastapi
uvicorn (if running locally)

# Code Explanation:


# Import Libraries: 
Imports necessary libraries for audio processing, AI interaction, and web service.
Environment Variable Loading: Loads the Google API key from the .env file.
FastAPI Setup: Initializes a FastAPI application for potential web integration.
Device Configuration: Configures the device (CPU or CUDA) and data type for faster-whisper.
Whisper Model Initialization: Loads the faster-whisper model.
capture_audio() Function: Captures audio from the microphone using speech_recognition.
transcribe_audio() Function: Transcribes the captured audio using faster-whisper.
analyze_text_with_ai() Function: Sends the transcribed text to Google's Gemini AI for analysis and retrieves the response.
speak_text() Function: Converts the AI's response to speech using gTTS and plays it back.

# Main Execution Block:
Captures audio.
Transcribes the audio.
Analyzes the transcribed text using Gemini AI.
Speaks the AI's response.
Prints performance metrics.

# Potential Improvements:
Error Handling: Enhance error handling for more robust performance.
Web Interface: Expand the FastAPI integration to create a web-based user interface.
User Interface: Create a Graphical User Interface using Tkinter, PyQt or other libraries.
Multi-language support: expand the language support for the speech to text and text to speech.
More complex Prompts: Add more complexity to the gemini prompt to get more accurate responses.
Persistent Storage: implement a database to store conversation history.
Real Time Transcriptions: Implement real time transcriptions.
More model options: Add the ability to change the whisper model size, or gemini model.

# Error Handling: 
Enhance error handling for more robust performance.
Web Interface: Expand the FastAPI integration to create a web-based user interface.
User Interface: Create a Graphical User Interface using Tkinter, PyQt or other libraries.
Multi-language support: expand the language support for the speech to text and text to speech.
More complex Prompts: Add more complexity to the gemini prompt to get more accurate responses.
Persistent Storage: implement a database to store conversation history.
Real Time Transcriptions: Implement real time transcriptions.
More model options: Add the ability to change the whisper model size, or gemini model.
