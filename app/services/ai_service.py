from app.ai.preprocessing import clean_text
from app.ai.inference import predict
from app.ai.postprocessing import build_soap
from app.ai.speech_to_text import transcribe_audio


def generate_soap(transcript: str):

    cleaned = clean_text(transcript)

    prediction = predict(cleaned)

    soap = build_soap(prediction)

    return soap

import os

def transcribe(audio_path: str):

    try:
        transcript = transcribe_audio(audio_path)

        return {
            "transcript": transcript
        }

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)