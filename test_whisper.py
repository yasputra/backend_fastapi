from faster_whisper import WhisperModel

print("Loading model...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

print("Model loaded!")

segments, info = model.transcribe(
    "audio.wav",
    language="id"
)

print(f"Detected language: {info.language}")

print("\nTranscript:")

for segment in segments:
    print(segment.text)