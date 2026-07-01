from faster_whisper import WhisperModel

# Model di-load sekali saat FastAPI startup
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path: str) -> str:
    """
    Mengubah file audio menjadi teks menggunakan Faster-Whisper.
    """

    segments, info = model.transcribe(
        audio_path,
        language="id"
    )

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()