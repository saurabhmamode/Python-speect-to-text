from unittest import result
from google.cloud import speech_v1p1beta1 as speech
import os

def sample_recognize(storage_uri, phrase):
    client = speech.SpeechClient()

    phrase = 'Savya is learning math'
    phrases = [phrase]

    boost = 10.0
    speech_contexts_element = {"phrases": phrases, "boost": boost}
    speech_contexts = [speech_contexts_element]

    sample_rate_hertz = 44100
    language_code = "en-IN"

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats
    encoding = speech.RecognitionConfig.AudioEncoding.MP3
    # encoding = speech.types.RecognitionConfig.AudioEncoding
    print(speech_contexts)
    config = {
        "speech_contexts": speech_contexts,
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": encoding,
    }
    audio = "./recording.mp3" #{"uri": storage_uri}

    with open(audio, 'rb') as mp3_file:
        file_bytes_mp3 = mp3_file.read()

    audio_recognition = speech.RecognitionAudio(content=file_bytes_mp3)
    response = client.recognize(config=config, audio=audio_recognition)

    for result in response.results:
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
    # transcripts_by_name[name] = {
    #     "hypothesis": "".join([result.alternatives[0].transcript
    #                            for result in response.results]),
    #     "reference": "".join(words[1:0])
    # }

    return response

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--storage_uri",type=str,default="./recording.mp3")
    parser.add_argument("--phrase", type=str, default="Savya")
    args = parser.parse_args()
    print(args)
    sample_recognize(args.storage_uri, args.phrase)

if __name__ == "__main__":
    main()