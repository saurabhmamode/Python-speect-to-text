from google.cloud import speech
import io

client = speech.SpeechClient()

# path = 'resources/commercial_mono.wav'
with open(r"c:\Users\saura\Desktop\python-codes\asynchronus\commercial_mono.wav", "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code="en-US",
    # Enable automatic punctuation
    enable_automatic_punctuation=True,
)

response = client.recognize(config=config, audio=audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("-" * 20)
    print("First alternative of result {}".format(i))
    print("Transcript: {}".format(alternative.transcript))