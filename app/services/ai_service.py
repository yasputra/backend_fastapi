from app.ai.preprocessing import clean_text
from app.ai.inference import predict
from app.ai.postprocessing import build_soap


def generate_soap(transcript: str):

    cleaned = clean_text(transcript)

    prediction = predict(cleaned)

    soap = build_soap(prediction)

    return soap