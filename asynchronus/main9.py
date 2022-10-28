from google.cloud import speech_v1p1beta1 as speech
import io


client = speech.SpeechClient()

speech_file = "c:\\Users\\saura\\Desktop\\python-codes\\asynchronus\\audio.wav"

with io.open(speech_file, "rb") as audio_file:
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
    print(u"First alternative of result {}".format(i))
    print(u"Transcript: {}".format(alternative.transcript))