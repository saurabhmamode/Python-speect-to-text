from google.cloud import speech
import io
client = speech.SpeechClient()

audio = speech.RecognitionAudio(uri="gs://cloud-samples-tests/speech/multi.wav")

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="en-US",
    audio_channel_count=2,
    enable_separate_recognition_per_channel=True,
)

response = client.recognize(config=config, audio=audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("-" * 20)
    print("First alternative of result {}".format(i))
    print(u"Transcript: {}".format(alternative.transcript))
    print(u"Channel Tag: {}".format(result.channel_tag))
