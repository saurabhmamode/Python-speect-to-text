from google.cloud import speech_v1p1beta1 as speech
import io
client = speech.SpeechClient()

speech_file = r"c:\Users\saura\Desktop\python-codes\asynchronus\audio.wav" 

with io.open(speech_file, "rb") as audio_file:
    content = audio_file.read()

# Here we construct a recognition metadata object.
# Most metadata fields are specified as enums that can be found
# in speech.enums.RecognitionMetadata
metadata = speech.RecognitionMetadata()
metadata.interaction_type = speech.RecognitionMetadata.InteractionType.DISCUSSION
metadata.microphone_distance = (
    speech.RecognitionMetadata.MicrophoneDistance.NEARFIELD
)
metadata.recording_device_type = (
    speech.RecognitionMetadata.RecordingDeviceType.SMARTPHONE
)

# Some metadata fields are free form strings
metadata.recording_device_name = "Pixel 2 XL"
# And some are integers, for instance the 6 digit NAICS code
# https://www.naics.com/search/
metadata.industry_naics_code_of_audio = 519190

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code="en-US",
    # Add this in the request to send metadata.
    metadata=metadata,
)

response = client.recognize(config=config, audio=audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("-" * 20)
    print(u"First alternative of result {}".format(i))
    print(u"Transcript: {}".format(alternative.transcript))